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
from settings import get_maps_path
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router(name=__name__)
router.message.filter(F.chat.type.in_({ChatType.PRIVATE}),)


@router.message(Command(commands=["start"]))
async def start(message: Message) -> None:

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

@router.message(WaitForText.waiting_for_text)
async def process_user_text(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, введите номер аудитории, куда вы хотите прийти (к примеру Р-1):") 
    await state.clear()
    await state.set_state(WaitForText.waiting_for_second)


@router.message(WaitForText.waiting_for_second)
async def send_map(message: Message, state: FSMContext):
    user_text = message.text.strip()

    try:
        photo_path = await get_maps_path(user_text)
        photo = FSInputFile(photo_path)

        await message.answer_photo(photo=photo)

        # await message.answer(f"✅ Вы ввели: {user_text}")
    except (ValueError, FileNotFoundError) as e:
        await message.answer(f"Ошибка: {e}")

    await state.clear()