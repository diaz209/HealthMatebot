from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters import Command
import db_service

# ⚡ Создаём Router
router = Router()

@router.message(Command("sleep"))
async def sleep_command(message: types.Message):
    try:
        # Разделяем команду и аргумент вручную
        args = message.text.split()  # ['/sleep', '7.5']
        if len(args) < 2:
            raise ValueError("Нет аргумента")
        hours = float(args[1])
        db_service.update_user(message.from_user.id, sleep=hours)
        await message.answer(f"Отмечено {hours} часов сна на сегодня!")
    except Exception:
        await message.answer("Используй команду так: /sleep 7.5")
