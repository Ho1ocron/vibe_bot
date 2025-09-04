from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import(
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
)


router = Router(name=__name__) 


@router.callback_query(F.data == "settings")
async def where_to_go(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back")]
        ]
    )

    await callback.message.edit_reply_markup(
        inline_message_id=callback.inline_message_id,
        reply_markup=keyboard
    )