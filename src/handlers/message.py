from aiogram import F, Router
from aiogram.enums.chat_type import ChatType
from aiogram.fsm.context import FSMContext
from aiogram.filters import(
    Command, 
    CommandStart, 
    CommandObject,
)
from aiogram.types import(
    Message, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
    FSInputFile
)
from states import WaitForText
from settings import get_maps_path, CODE
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router(name=__name__)
router.message.filter(F.chat.type.in_({ChatType.PRIVATE}),)


@router.message(Command(commands=["start"]))
async def start(message: Message, state: FSMContext) -> None:
    await state.clear()
    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Куда идти?", callback_data="go"), 
            InlineKeyboardButton(text="Достижения", callback_data="achievements")
        ],
        [InlineKeyboardButton(text="Настройки", callback_data="settings")]
    ]
)
    
    await message.answer(
        (
            f"👋 <b>Привет, дорогой Друг!</b> 👋\n\n"
            f"Я помогу тебе сориентироваться в новом кампусе ИРИТ-РтФ УрФУ в Новокольцовском.\n"
            f"Пожалуйста, выбери действие: "
        ), reply_markup=keyboard
    )

@router.message(WaitForText.waiting_for_text, ~F.text.startswith("/"))
async def process_user_text(message: Message, state: FSMContext):
    await message.answer(
        "Пожалуйста, введите номер аудитории, куда вы хотите прийти (к примеру Р-1):"
    ) 
    await state.clear()
    await state.set_state(WaitForText.waiting_for_second)


@router.message(WaitForText.waiting_for_second, ~F.text.startswith("/"))
async def send_map(message: Message, state: FSMContext):
    user_text = message.text.strip()

    try:
        photo_path = await get_maps_path(user_text)
        photo = FSInputFile(photo_path)

        await message.answer_photo(photo=photo)
        await message.answer(text=(
            "У входа в аудиторию вы должны увидеть QR-code.\n\n"
            "Пожалуйста, отсканируйте полученный код и отправте его боту, чтобы получить достижение и балл."
        ))

        # await message.answer(f"✅ Вы ввели: {user_text}")
    except (ValueError, FileNotFoundError) as e:
        await message.answer(f"Ошибка: {e}")

    await state.clear()
    await state.set_state(WaitForText.waiting_for_code)


@router.message(WaitForText.waiting_for_code, ~F.text.startswith("/"))
async def code_reaction(message: Message, state: FSMContext) -> None:
    if message.text == CODE:
        await message.answer("Поздравляю! Вы получили 1 балл.")
        await state.clear()
        return
    await message.answer("К сожалению, этот код не является валидным, попробуйте еще раз.")
    