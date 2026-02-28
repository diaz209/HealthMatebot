from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    text = (
        "Привет! Я твой Health Tracker Bot 🏃‍♂️💧😴\n\n"
        "Команды:\n"
        "/water <мл> - отметь сколько воды выпил\n"
        "/sleep <часы> - отметь сколько спал\n"
        "/exercise <мин> - отметь упражнения\n"
        "/advice - получи советы по улучшению здоровья"
    )
    await message.answer(text)
