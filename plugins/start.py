from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    InputMediaAnimation
)
from config import Config

BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton(text='Etiraf et', callback_data="etiraf_button")],
                                [InlineKeyboardButton(text='Güncəlləmə Kanalımız', url='http://t.me/MultiAzOfficial'), 
                                InlineKeyboardButton(text='Etiraf Kanalımız', url='http://t.me/MultiEtiraf')]])

@Client.on_message(filters.command(['start'], ['/', '!']))
async def start(_, msg: Message):
    await _.send_animation(chat_id=msg.chat.id, 
    animation=f"https://te.legra.ph/file/2ec7302acc70ea68d7ad3.gif",
    caption=f"👋 Salam {msg.from_user.mention}\nℹ️ Mən etiraf botuyam\n💁 Aşağıdakı `Etiraf et` düyməsinə vuraraq etiraf et", 
    reply_markup=BUTTON)
    await _.send_message(chat_id=-1001683015698, text=f"[LOG] {msg.from_user.first_name} start etdi")
    print(f'{msg.from_user.first_name} start etdi')

@Client.on_message(filters.command(['etiraf'], ['/', '!']))
async def etiraf(_, msg: Message):
        await msg.reply(
            text=f"💁 Necə etiraf edəcəksən?",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Açıq etiraf', callback_data="etiraf_aciq"), 
                                InlineKeyboardButton(text='Gizli etiraf', callback_data="etiraf_gizli")]]),
        )        

@Client.on_callback_query(filters.regex("etiraf_button"))
async def cb_info(bot: Client, query: CallbackQuery):
    await query.edit_message_media(
    media=InputMediaAnimation(f"https://te.legra.ph/file/796e259cd8d37c4f85d32.gif"),
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Açıq etiraf', callback_data="etiraf_aciq"), 
                                        InlineKeyboardButton(text='Gizli Etiraf', callback_data="etiraf_gizli")]]))
    await query.edit_message_caption(
    caption=f"💁 Necə etiraf edəcəksən?",
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Açıq etiraf', callback_data="etiraf_aciq"), 
                                        InlineKeyboardButton(text='Gizli Etiraf', callback_data="etiraf_gizli")]]))                                         


@Client.on_callback_query(filters.regex(r'kapat'))
async def _onaylama(bot, query):
    await bot.send_message(Config.LOG_SILINMIS, text=f'🔽 Aşağıdakı Etiraf {query.from_user.mention} tərəfindən silindi 🔽')
    await bot.send_message(Config.LOG_SILINMIS, text=query.message.text)
    await query.edit_message_caption(f'🗑 Etiraf {query.from_user.mention} tərəfindən silindi')
    user = query.data.split()[1]
    await bot.send_message(user, text=f"📣 Sənin etirafın qəbul olunmadı.")