from telegram import Update
from telegram.ext import CallbackContext
import django
django.setup()

from auth_app.models import TelegramUser

def start(update: Update, context: CallbackContext) -> None:
    try:
        token = update.message.text.split(' ')[1]  # Extract the token
    except IndexError:
        update.message.reply_text('Ошибка: Токен отсутствует. Попробуйте еще раз.')
        return

    user = update.message.from_user

    telegram_user, created = TelegramUser.objects.get_or_create(
        telegram_id=user.id,
        defaults={'telegram_username': user.username}
    )

    telegram_user.token = token
    telegram_user.save()

    update.message.reply_text(f'Привет, {user.username}! Вы успешно авторизовались через Telegram.')
