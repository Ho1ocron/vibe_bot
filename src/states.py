from aiogram.fsm.state import StatesGroup, State

class WaitForText(StatesGroup):
    waiting_for_text = State()
