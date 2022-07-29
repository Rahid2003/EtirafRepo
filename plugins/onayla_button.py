from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    InputMediaAnimation
)
from config import Config

ETIRAF_BOT_BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton(text='💭 Səndə öz etirafını yaz ', url="https://t.me/MultiEtirafBot")]])
ETIRAF_CHANNEL = InlineKeyboardMarkup([[InlineKeyboardButton(text='📣 Etiraf Kanalımız', url='http://t.me/MultiEtiraf')]])

@Client.on_callback_query(filters.regex(r'onayla'))
async def _onaylama(bot, query):
        user = query.data.split()[1]
        await bot.send_message(Config.ETIRAF_CHANNEL, text=query.message.text, reply_markup=ETIRAF_BOT_BUTTON)
        await query.edit_message_caption('✅ Etiraf kanalına göndərildi')
        await bot.send_message(user, text=f"📣 Sənin etirafın qəbul olundu.", 
        reply_markup=ETIRAF_CHANNEL)