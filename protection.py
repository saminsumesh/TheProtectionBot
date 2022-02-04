from faulthandler import disable
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram.types import Message, User
from Config import API_ID, API_HASH, BOT_TOKEN, START_MSG, DB_URL

Client = Client(
    "Protection Bot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

@Client.on_message(filter.command("start"))
async def bot_start(bot, m:Message):
    await m.reply_text(
        text=START_MSG.format(m.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("Add me to your group", url="")
            ],[
                InlineKeyboardButton("Help", callback_data="help"),
                InlineKeyboardButton("About", callback_data="about")    
            ]]
        ),
        disable_web_page_preview=True
        )

@Client.on_message(filters.command("antiservice") & ~filters.private)
async def anti_service(_, message):
    if len(message.command) != 2:
        return await message.reply_text(
            "Usage: /antiservice [enable | disable]"
        )
    mode_on = ["yes", "on", "true"]
    mode_of = ["no", "off", "false"]

    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "enable":
        await mode_on(chat_id)
        await message.reply_text(
            "Enabled AntiService System. I will Delete Service Messages from Now on."
        )
    elif status == "disable":
        await mode_of(chat_id)
        await message.reply_text(
            "Disabled AntiService System. I won't Be Deleting Service Message from Now on."
        )
    else:
        await message.reply_text(
            "Unknown Suffix, Use /antiservice [enable|disable]"
        )
mongo_client = MongoClient(DB_URL)        
db = mongo_client
antiservicedb = db.antiservice


async def is_antiservice_on(chat_id: int) -> bool:
    chat = await antiservicedb.find_one({"chat_id": chat_id})
    if not chat:
        return True
    return False


@Client.on_message(filters.service, group=11)
async def delete_service(_, message):
    chat_id = message.chat.id
    try:
        if await (chat_id):
            return await message.delete()
    except Exception:
        pass
