from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters import Command
import db_service

router = Router()  # обязательно

@router.message(Command("water"))
async def water_command(message: types.Message):
    # Разделяем команду и аргумент вручную
    try:
        args = message.text.split()  # ['/water', '500']
        if len(args) < 2:
            raise ValueError("Нет аргумента")
        amount = int(args[1])
        db_service.update_user(message.from_user.id, water=amount)
        await message.answer(f"Отмечено {amount} мл воды на сегодня!")
    except Exception:
        await message.answer("Используй команду так: /water 500")
