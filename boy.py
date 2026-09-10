import os
import asyncio
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '8783616591:AAEYGC43fEZjspF_SQ8-qWyjLPzfxfMAPYw'  # BotFather এর টোকেন
WEB_APP_URL = 'https://gmailtaskminiapp.netlify.app'  # আপনার Mini App লিংক

# Render Keep-Alive Server
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is active!")

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), DummyHandler)
    server.serve_forever()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    keyboard = [
        [InlineKeyboardButton(text="🚀 Open Mini App", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message_text = f"হ্যালো {first_name}! 👋\n\nআমাদের বোটে আপনাকে স্বাগতম। কাজ শুরু করতে এবং সব ফিচার ব্যবহার করতে নিচের বাটনটি চাপুন।"
    await update.message.reply_text(message_text, reply_markup=reply_markup)

if __name__ == '__main__':
    Thread(target=run_health_server, daemon=True).start()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
