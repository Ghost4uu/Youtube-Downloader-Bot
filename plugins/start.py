from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/YTAudio_Channel")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Tizwizlik")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b> welcome🙂 Please Send Me YouTube Link This will Help You Download Audio & Video.\n/help for More info"

    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
