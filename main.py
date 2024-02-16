import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from datetime import datetime

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6624239427:AAHJsmVbUEUYldSJGiqU28Ocb8rFXKOcr1I")
# Диспетчер
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

# Хэндлер на команду /startъ
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Бросить кубик"),
            types.KeyboardButton(text="Информация о боте")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Что хочешь сделать?"
    )
    await message.answer("Что хочешь сделать?", reply_markup=keyboard)

@dp.message(F.text.lower() == "бросить кубик")
async def with_puree(message: types.Message, bot: Bot):
    await bot.send_dice(message.chat.id, emoji=DiceEmoji.DICE)

@dp.message(F.text.lower() == "информация о боте")
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())