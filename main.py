import os
print("Bot Started...")
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
SOURCE_ID = int(os.environ.get("SOURCE_ID", "0"))
DEST_ID = int(os.environ.get("DEST_ID", "0"))

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
if update.effective_chat and update.effective_chat.id == SOURCE_ID:
try:
await context.bot.copy_message(
chat_id=DEST_ID,
from_chat_id=SOURCE_ID,
message_id=update.message.message_id
)
except Exception as e:
print(f"Error: {e}")

def main():
print("Bot Started...")
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()

if name == "main":
main(/)
