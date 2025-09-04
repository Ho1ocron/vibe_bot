from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from settings import ADMIN_IDS

router = Router(name=__name__)

router.message.filter(
    F.from_user.id.in_(ADMIN_IDS),
)