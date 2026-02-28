from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_command(message: types.Message):
    help_text = (
        "Список команд Health Tracker Bot:\n\n"
        "/start — Запуск бота и приветствие\n"
        "/help — Показать список команд\n"
        "/water [мл] — Добавить количество выпитой воды\n"
        "/sleep [часы] — Добавить количество сна\n"
        "/exercise [мин] — Добавить время упражнений\n"
        "/advice — Получить персональные советы"
    )
    await message.answer(help_text)
