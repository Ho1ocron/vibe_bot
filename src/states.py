from aiogram.fsm.state import StatesGroup, State

class WaitForText(StatesGroup):
    waiting_for_text = State()
    waiting_for_second = State()
