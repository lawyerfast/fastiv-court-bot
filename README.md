# 🤖 Fastiv Court Monitor Bot

Цей Telegram-бот автоматично перевіряє сайт [court.gov.ua](https://court.gov.ua/assignments/) на наявність судових засідань, у яких учасником є **Фастівська міська рада**, та надсилає їх користувачу після команди `/start`.

## 📦 Що міститься

- `bot.py` — код Telegram-бота
- `requirements.txt` — бібліотеки Python
- `README.md` — ця інструкція

---

## 🚀 Як розгорнути на [Render](https://render.com)

### 1. Створіть репозиторій на [GitHub](https://github.com)

Завантажте ці файли до нового репозиторію.

### 2. Перейдіть на [render.com](https://render.com)

- Створіть обліковий запис або увійдіть
- Натисніть **"New" → "Web Service"**
- Підключіть GitHub та оберіть репозиторій

### 3. Заповніть параметри

- **Environment**: Python 3
- **Build Command**:
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command**:
  ```bash
  python bot.py
  ```

### 4. Додайте свій Telegram токен

У Render → Settings → Environment:
```
KEY: BOT_TOKEN
VALUE: ваш токен з @BotFather
```

---

## 🧪 Локальний запуск

```bash
pip install -r requirements.txt
python bot.py
```

---

## 📩 Автор

Створено з ❤️ для моніторингу судових засідань Фастівської міської ради.