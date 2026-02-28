import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from config import BOT_TOKEN

# Импорт роутеров обработчиков
from start_handler import router as start_router
from water_handler import router as water_router
from sleep_handler import router as sleep_router
from exercise_handler import router as exercise_router
from advice_handler import router as advice_router
from help_handler import router as help_router

# Создаём бота с правильными свойствами
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

# Диспетчер
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(start_router)
dp.include_router(water_router)
dp.include_router(sleep_router)
dp.include_router(exercise_router)
dp.include_router(advice_router)
dp.include_router(help_router)

# Запуск бота
async def main():
    print("Бот запущен...")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
