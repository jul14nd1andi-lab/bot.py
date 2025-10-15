from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8225492759:AAF8nqnO53PE_sjILnNQaMw-7oa1jyxVQIk"

async def visit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://docs.google.com/spreadsheets/d/1m5vV9TrO1OMUxMgcdeGsQ6DhdCUE7cCqakqfedED8ow/edit?hl=id&gid=0#gid=0&range=N1")

async def status_visit (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("https://docs.google.com/spreadsheets/d/1m5vV9TrO1OMUxMgcdeGsQ6DhdCUE7cCqakqfedED8ow/edit?hl=id&gid=0#gid=0&range=M:M")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Perintah:\n/visit - mulai visit\n/status_visit - mulai status visit")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Perintah:\n/visit - mulai visit\n/status_visit - mulai status visit")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)



app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("visit", visit))
app.add_handler(CommandHandler("status_visit", status_visit))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("start", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot sedang berjalan...")
app.run_polling()
