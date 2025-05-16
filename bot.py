import logging
import datetime
import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = 'YOUR_BOT_TOKEN'  # 🔁 Вставте свій токен сюди

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    today = datetime.datetime.now().strftime('%d.%m.%Y')

    await context.bot.send_message(chat_id=chat_id, text=f"🔍 Пошук судових засідань за {today}...")

    url = f"https://court.gov.ua/assignments/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    table = soup.find("table")
    results = []

    if table:
        rows = table.find_all("tr")
        for row in rows:
            if "Фастівська міська рада" in row.text and today in row.text:
                results.append(row.text.strip())

    if results:
        message = "\n\n".join(results[:10])
        await context.bot.send_message(chat_id=chat_id, text=f"🧾 Знайдено засідання:\n\n{message}")
    else:
        await context.bot.send_message(chat_id=chat_id, text="❌ Засідань не знайдено на сьогодні.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущено...")
    app.run_polling()