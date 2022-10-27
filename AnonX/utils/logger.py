from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**🤖 𝐀𝐥𝐢𝐬𝐡𝐚 𝐌𝐮𝐬𝐢𝐜 **
**━━━━━━━━━━━━━━━**
**☘️ 𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞 : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**🥀 𝐍𝐚𝐦𝐞 : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**🌸 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**🌷 𝐈𝐃  : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**🌿 𝐂𝐡𝐚𝐭 𝐥𝐢𝐧𝐤: >** {chatusername}
**━━━━━━━━━━━━━━━**
**🍒 𝐒𝐞𝐚𝐫𝐜𝐡𝐞𝐝 𝐅𝐨𝐫:** {message.text}
**━━━━━━━━━━━━━━━**
**🍉 𝐒𝐭𝐫𝐞𝐚𝐦 𝐓𝐲𝐩𝐞:** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
