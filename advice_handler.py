from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters import Command
import db_service

router = Router()

@router.message(Command("advice"))
async def advice_command(message: types.Message):
    user_data = db_service.get_user(message.from_user.id)
    if not user_data:
        await message.answer("Сначала добавьте данные через /water, /sleep и /exercise.")
        return

    water, sleep, exercise = user_data
    advice_messages = []

    # Логика для воды
    if water < 1500:
        advice_messages.append(f"Ты выпил {water} мл воды. Пей больше воды, минимум 1.5–2 литра в день.")
    elif water > 3000:
        advice_messages.append(f"Ты выпил {water} мл воды. Не переусердствуй с водой, держи баланс.")
    else:
        advice_messages.append(f"Ты выпил {water} мл воды. Отлично, норма воды соблюдена!")

    # Логика для сна
    if sleep < 7:
        advice_messages.append(f"Ты спал {sleep} часов. Попробуй спать хотя бы 7–8 часов для восстановления.")
    elif sleep > 9:
        advice_messages.append(f"Ты спал {sleep} часов. Слишком много сна может мешать бодрости, держи баланс.")
    else:
        advice_messages.append(f"Ты спал {sleep} часов. Отлично, сон в норме!")

    # Логика для упражнений
    if exercise < 20:
        advice_messages.append(f"Ты сделал {exercise} минут упражнений. Добавь активности, хотя бы 30 минут в день.")
    elif exercise > 90:
        advice_messages.append(f"Ты сделал {exercise} минут упражнений. Не перенапрягайся, отдых тоже важен.")
    else:
        advice_messages.append(f"Ты сделал {exercise} минут упражнений. Отлично, держи ритм!")

    # Отправляем советы
    await message.answer("\n".join(advice_messages))
