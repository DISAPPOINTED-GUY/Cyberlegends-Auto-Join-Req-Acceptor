
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def start_command(tv, message):
    message_id=message.from_user.id
    greeting_message="Welcome to Tv Join Request Acceptor Bot \n I will accept Join Requests for your group/channel automatically✅."
    markup_keyboard=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Add me to your Group", url="https://t.me/TvCoinBot?startgroup=Cyberlegends_Network&admin=invite_users+manage_chat")],
            [InlineKeyboardButton("Add me to your Channel", url="https://t.me/TvCoinBot?startchannel=Cyberlegends_Network&admin=invite_users+manage_chat")]
        ])
    await tv.send_message(chat_id=message.chat.id,message=greeting_message,reply_markup=markup_keyboard )