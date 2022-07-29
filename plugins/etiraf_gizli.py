from pyrogram import Client, filters
from main import app
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from config import Config

ETIRAF_CHANNEL = InlineKeyboardMarkup([[InlineKeyboardButton(text='📣 Etiraf kanalımız', url="https://t.me/MultiEtiraf")]]) 

@Client.on_callback_query(filters.regex("etiraf_gizli"))
async def etiraf_aciq(bot: Client, query: CallbackQuery):
    chat_id = query.message.chat.id
    etiraf_mesaj = await bot.ask(chat_id, 'Etirafını yazın:')
    await bot.send_message(chat_id, text=f"✅ Etiraf bizə çatdı. Təsdiq olunduğunda kanala göndəriləcək.\n\nİstifadəçi: {query.from_user.mention}\nEtiraf növü: Gizli\nEtiraf mesajı: {etiraf_mesaj.text}", reply_markup=ETIRAF_CHANNEL)
    await bot.send_message(Config.LOG_ADMINS, text=f"İstifadəçi: {query.from_user.mention}\nİstifadəçi İD:{query.from_user.id}\n\n🔽 Kanal üçün mesaj aşağıda avtomatik yazıldı 🔽")
    await bot.send_message(Config.LOG_ADMINS, text=f"📣 Etiraf növü: Gizli\n🕵️ İstifadəçi: Anonim\n\n💬 Etiraf mesajı: {etiraf_mesaj.text}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='✅ Təsdiqlə', callback_data=f"onayla {query.from_user.id}"),
                                      InlineKeyboardButton(text='🗑 Sil', callback_data=f"kapat {query.from_user.id}")]]))
    print(f'{query.from_user.first_name} gizli etiraf yazdı')