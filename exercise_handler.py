from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters import Command
import db_service

# ⚡ Сначала создаём router
router = Router()

@router.message(Command("exercise"))
async def exercise_command(message: types.Message):
    try:
        # Разделяем команду и аргумент вручную
        args = message.text.split()  # ['/exercise', '30']
        if len(args) < 2:
            raise ValueError("Нет аргумента")
        minutes = int(args[1])
        db_service.update_user(message.from_user.id, exercise=minutes)
        await message.answer(f"Отмечено {minutes} минут упражнений на сегодня!")
    except Exception:
        await message.answer("Используй команду так: /exercise 30")
