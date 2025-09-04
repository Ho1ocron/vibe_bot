from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.types import(
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
)
from states import WaitForText

router = Router(name=__name__) 



@router.callback_query(F.data == "achievements")
async def where_to_go(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Достижение 1", callback_data="ach1"), 
             InlineKeyboardButton(text="Достижение 2", callback_data="ach2"),
             InlineKeyboardButton(text="Достижение 3", callback_data="ach3")],
             [InlineKeyboardButton(text="Назад", callback_data="backach")]
        ]
    )

    await callback.message.edit_text(
        inline_message_id=callback.inline_message_id,
        reply_markup=keyboard,
        text="👋 <b>Привет, дорогой Друг!</b> 👋\nТут ты можешь ознакомиться со всеми достижениями!\nВ данный момент у тебя вот столько баллов: 0"
    )

@router.callback_query(F.data == "ach1")
async def where_to_go(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
             [InlineKeyboardButton(text="Назад", callback_data="backach")]
        ]
    )

    await callback.message.edit_text(
        inline_message_id=callback.inline_message_id,
        reply_markup=keyboard,
        text="Опис 1"
    )

@router.callback_query(F.data == "ach2")
async def where_to_go(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
             [InlineKeyboardButton(text="Назад", callback_data="backach")]
        ]
    )

    await callback.message.edit_text(
        inline_message_id=callback.inline_message_id,
        reply_markup=keyboard,
        text="Опис 2"
    )

@router.callback_query(F.data == "ach3")
async def where_to_go(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
             [InlineKeyboardButton(text="Назад", callback_data="backach")]
        ]
    )

    await callback.message.edit_text(
        inline_message_id=callback.inline_message_id,
        reply_markup=keyboard,
        text="Опис 3"
    )

@router.callback_query(F.data == "backach")
async def where_to_go(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
             [InlineKeyboardButton(text="Достижение 1", callback_data="ach1"), 
             InlineKeyboardButton(text="Достижение 2", callback_data="ach2"),
             InlineKeyboardButton(text="Достижение 3", callback_data="ach3")],
             [InlineKeyboardButton(text="Назад", callback_data="backmain")]
        ]
    )

    await callback.message.edit_text(
        inline_message_id=callback.inline_message_id,
        reply_markup=keyboard,
        text="👋 <b>Привет, дорогой Друг!</b> 👋\nТут ты можешь ознакомиться со всеми достижениями!\nВ данный момент у тебя вот столько баллов: 0"
    )

@router.callback_query(F.data == "backmain")
async def where_to_go(callback: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
            InlineKeyboardButton(text="Куда идти?", callback_data="go"), 
            InlineKeyboardButton(text="Достижения", callback_data="achievements")
            ],
            [InlineKeyboardButton(text="Настройки", callback_data="settings")]
        ]
    )

    await callback.message.edit_text(
        inline_message_id=callback.inline_message_id,
        reply_markup=keyboard,
        text="👋 <b>Привет, дорогой Друг!</b> 👋\n \n Я помогу тебе сориентироваться в новом кампусе ИРИТ-РтФ УрФУ в Новокольцовском.\n Пожалуйста, выбери действие: "
    )

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