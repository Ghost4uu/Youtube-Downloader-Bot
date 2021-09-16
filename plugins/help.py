from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f" if you want help join our offical group t.me/YTAudio_Group"
    await message.reply_text(helptxt)
