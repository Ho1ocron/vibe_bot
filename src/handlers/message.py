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
)
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router(name=__name__)
router.message.filter(F.chat.type.in_({ChatType.PRIVATE}),)


@router.message(Command(commands=["start"]))
async def start(message: Message) -> None:

    keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Куда идти?", callback_data="go"), InlineKeyboardButton(text="Достижения", callback_data="achievements")],
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