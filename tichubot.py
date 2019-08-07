import telegram  # make sure that python-telegram-bot 12 or newer is installed 
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import threading
import datetime

key = open("botkey.txt").readlines()[0].strip()
DEVID = int(open("botkey.txt").readlines()[1].strip()) 


# Enable logging #TODO how does this work and what does it do?
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(messages', level=logging.INFO)

logger = logging.getLogger(__name__)

def tichu3():
    # call something
def tichu4():
    # call something else

def team(player1 , player2, currentPoints, allTimePoints, currentTichuRate, currentTichuSuccessRate, allTimeTichuRate, allTimeTichuSuccessRate)
	# tja, wie geht den der scheiß mit klassen eigentlich richtig?
	# save stats in txt file for keeping

def counter(name):
    # get number panel and add number if valid to counter, then write to team? 
	# make sure the right team's tichu points is assigned to A/B
	addPoints = inputPoints + tichuPointsA
	autoPoints = 100 - inputPoints + tichuPointsB
    return count


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
	"""Send a message when the command /start is issued."""
	update.message.reply_text('Hi!') 
	update.message.reply_text('TichuBot is ready')
    update.message.reply_text('How many players?') 
    # TODO make button for 3 or 4 players and call function

def help(update, context):
	"""Send a message when the command /help is issued."""
	
	update.message.reply_text('/start to start the bot')

def error(update, context):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)
	#TODO find out how this works

def main():
	"""Start the bot."""
	# Create the Updater and pass it your bot's token.
	# Make sure to set use_context=True to use the new context based callbacks
	# Post version 12 this will no longer be necessary
	updater = Updater(key, use_context=True)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))

	# on noncommand - send help info:
	dp.add_handler(MessageHandler(Filters.text, help))  #does not trigger on typos in commands e.g. /tomorow

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()

if __name__ == '__main__':
	main()
