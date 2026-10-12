import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
TOKEN = os.environ.get("BOT_TOKEN")
PRODUCTS = {
    "hoodie": {"name": "Худи Shymkent", "price": "12 990 тг"},
    "cap": {"name": "Кепка", "price": "4 990 тг"},
    "tshirt": {"name": "Футболка", "price": "5 990 тг"},
}
async def start(update, context):
    kb = [[InlineKeyboardButton("🧥 Худи - 12 990 тг", callback_data='hoodie')],[InlineKeyboardButton("🧢 Кепка - 4 990 тг", callback_data='cap')],[InlineKeyboardButton("👕 Футболка - 5 990 тг", callback_data='tshirt')]]
    await update.message.reply_text("Сәлем! Shym-Shop! Тауар таңда 👇", reply_markup=InlineKeyboardMarkup(kb))
async def button(update, context):
    q=update.callback_query; await q.answer()
    if q.data in PRODUCTS:
        p=PRODUCTS[q.data]
        kb2=[[InlineKeyboardButton("✅ Тапсырыс беру", callback_data=f'order_{q.data}')]]
        await q.message.reply_text(f"{p['name']}\n{p['price']}", reply_markup=InlineKeyboardMarkup(kb2))
    else:
        await q.message.reply_text("Тапсырыс қабылданды! Менеджер [@seydakhan0v_](https://www.threads.net/@seydakhan0v_) 5 мин жазады!")
app=Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
