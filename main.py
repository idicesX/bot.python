from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

app = Client("bot", bot_token="8266639592:AAGiCVpSwW0kUa_Rn-IPJz-VXMh3O0dIrhc")

VIDEO_FILE_ID = "AAMCBQADGQECY8TBaPrzpSGm5EDFMSW3gvoUaPJo0uEAAg8YAAJd1NhXd6V66ZXwGqEBAAdtAAM2BA"
VIDEO_CAPTION = "<b>🔥 Watch Before Joining!</b>"
MESSAGE_TEXT = "<b>⚠️ Must Join All Channels to Unlock Exclusive Content</b>\n\n✅ <b>After Joining, Click on 🟢 'Joined'</b>"

BUTTONS = [
    [
        InlineKeyboardButton("Must", url="https://t.me/+Acr_GLTFSCJiOWVl"),
        InlineKeyboardButton("Must", url="https://t.me/+yZVVK3L_IGdjYzQ9"),
    ],
    [
        InlineKeyboardButton("Must", url="https://t.me/EscrowMoon"),
        InlineKeyboardButton("Must", url="https://t.me/+Ogyz4Nzq4t9mMTk1"),
    ],
    [
        InlineKeyboardButton("🟢 Joined", callback_data="/joined")
    ]
]

@app.on_message(filters.command("start"))
async def start(client, message):
    try:
        await client.send_video(
            chat_id=message.chat.id,
            video=VIDEO_FILE_ID,
            caption=VIDEO_CAPTION,
            parse_mode="html"
        )

        await client.send_message(
            chat_id=message.chat.id,
            text=MESSAGE_TEXT,
            parse_mode="html",
            reply_markup=InlineKeyboardMarkup(BUTTONS)
        )

        print("✅ Video and message sent successfully!")

    except Exception as e:
        print("❌ Error sending video/message:", e)

app.run()
