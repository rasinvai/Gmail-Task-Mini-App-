import os
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ১. BotFather থেকে পাওয়া API Token বসান (উদ্ধৃতি চিহ্ন ' ' এর ভেতরে)
TOKEN = '8783616591:AAEYGC43fEZjspF_SQ8-qWyjLPzfxfMAPYw'

# ২. আপনার Mini App-এর HTTPS লিংক বসান
WEB_APP_URL = 'https://gmailtaskminiapp.netlify.app/'

# Render Keep-Alive Server
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is active!")

    def log_message(self, format, *args):
        return

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    server.serve_forever()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name if update.effective_user else "User"
    keyboard = [
        [InlineKeyboardButton(text="🚀 Open Mini App", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_text = f"হ্যালো {user_name}! 👋\n\nআমাদের বোটে আপনাকে স্বাগতম। কাজ শুরু করতে নিচে থাকা বাটনটি চাপুন।"
    await update.message.reply_text(message_text, reply_markup=reply_markup)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.error(f"Exception while handling an update: {context.error}")

if __name__ == '__main__':
    Thread(target=run_health_server, daemon=True).start()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_error_handler(error_handler)
    print("Bot is successfully running...")
    app.run_polling(drop_pending_updates=True)    user_name = update.effective_user.first_name if update.effective_user else "User"
    
    keyboard = [
        [InlineKeyboardButton(text="🚀 Open Mini App", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message_text = f"হ্যালো {first_name}! 👋\n\nআমাদের বোটে আপনাকে স্বাগতম। কাজ শুরু করতে নিচে থাকা বাটনটি চাপুন।"
    
    await update.message.reply_text(message_text, reply_markup=reply_markup)

# Error Handler (যাতে "No error handlers registered" এরর আর না আসে)
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.error(f"Exception while handling an update: {context.error}")

if __name__ == '__main__':
    # হেলথ সার্ভার আলাদা থ্রেডে চালু
    Thread(target=run_health_server, daemon=True).start()
    
    # বট অ্যাপ তৈরি
    app = ApplicationBuilder().token(TOKEN).build()
    
    # হ্যান্ডলার যুক্তকরণ
    app.add_handler(CommandHandler("start", start))
    app.add_error_handler(error_handler)
    
    print("Bot is successfully running...")
    app.run_polling(drop_pending_updates=True)
