from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import(
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
)
from states import WaitForText

router = Router(name=__name__) 


@router.callback_query(F.data == "settings")
async def open_settings(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back")]
        ]
    )
    await callback.message.edit_text("Настройки пока недоступны.", )
    await callback.message.edit_reply_markup(
        inline_message_id=callback.inline_message_id,
        reply_markup=keyboard
    )


@router.callback_query(F.data == "go")
async def find_auditory(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.message.answer("Пожалуйста, введите номер аудитории, около которой вы сейчас находитесь:") 
    await state.set_state(WaitForText.waiting_for_text)