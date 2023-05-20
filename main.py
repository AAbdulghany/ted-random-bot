import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Application
import pandas as pd
from Token import TELEGRAM_BOT_TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the TED Talks data
df = pd.read_excel("ted_talks.xlsx")


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Use /random to get a random TED Talk.')


async def random_talk(update: Update, context: CallbackContext) -> None:
    # df.sample(1) returns a new DataFrame with one random row
    # iloc[0] gets the first (and only) row from that DataFrame
    talk = df.sample(1).iloc[0]
    await update.message.reply_text(f"{talk['Title']}\n{talk['Link']}")


def main() -> None:
    bot = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    bot.add_handler(CommandHandler("start", start))
    bot.add_handler(CommandHandler("random", random_talk))

    bot.run_polling()
    logger.info('Bot started')

    bot.idle()


if __name__ == '__main__':
    main()
