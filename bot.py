from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters
from handlers.report_panel import (
    handle_report_callback,
    report_menu,
    handle_date_input
)

BOT_TOKEN = '8448304483:AAFUB8sHKTK2tDPah5jiqE158szQzRTIyLY'

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📊 پنل گزارش کار", callback_data='report_panel')],
        [InlineKeyboardButton("👤 پنل پروفایل", callback_data='profile_panel')],
        [InlineKeyboardButton("🛠 ابزارها", callback_data='tools')],
        [InlineKeyboardButton("📅 روز شمار کنکور", callback_data='countdown')],
        [InlineKeyboardButton("📝 ساخت آزمون آنلاین", callback_data='make_exam')],
        [InlineKeyboardButton("📞 ارتباط با ما", callback_data='contact')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("سلام! یکی از گزینه‌ها را انتخاب کن:", reply_markup=reply_markup)

def handle_callbacks(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    if data.startswith("report_") or data.startswith("study_") or data.startswith("test_") or data in ["go_to_tests", "submit_report", "analyze_weekly", "analyze_monthly", "analyze_total"]:
        handle_report_callback(update, context)
    else:
        query.answer()
        query.edit_message_text("❗ این گزینه فعلاً فعال نیست.")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_callbacks))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_date_input))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
