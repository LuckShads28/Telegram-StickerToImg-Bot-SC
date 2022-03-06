from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image
import logging

TOKEN = "YOUR_BOT_TOKEN"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def error(update, context):
    logger.warning('Update "%s" caused error "%s" ', update, context.error)

def start(update, context):
    update.message.reply_text("Telegram sticker to image converter bot \nBy: luckshads28\n\nSend sticker to convert\nNote: Can't convert animated sticker!")

def stickers(update, context):
	username = update.message.from_user['username']
	chat_id = update.message.chat_id
	msg_id = update.message.message_id
	caption = "Sucessfully convert sticker to image!"

	print("Get sticker from "+username)
	print("Message id: "+str(msg_id))
	usr_sticker = update.message.sticker.get_file()
	stickerID = update.message.sticker['file_id']

	print("Downloading sticker...")
	usr_sticker.download('sticker.webp')

	print("Converting sticker to image...")
	image = Image.open("sticker.webp").convert("RGB")
	image.save("sticker.png", "png")

	print("Sending image to user")
	context.bot.sendPhoto(chat_id = chat_id, photo = open('sticker.png', 'rb'), reply_to_message_id = msg_id, caption = caption)
	print("Image send sucessfull!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.sticker, stickers))

    dp.add_error_handler(error)

    updater.start_polling()
    print("Bot Successfully Started!")
    updater.idle()


if __name__ == '__main__':
    main()