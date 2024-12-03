import string
import random

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .models import TelegramUser


def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))


def home(request):
    telegram_username = request.session.get('telegram_username')
    return render(request, 'home.html', {'telegram_username': telegram_username})


@login_required
def get_user_info(request):
    telegram_username = request.session.get('telegram_username')
    return JsonResponse({'telegram_username': telegram_username})


def telegram_login_callback(request, token):
    telegram_user = TelegramUser.objects.filter(telegram_id=token).first()

    if telegram_user:
        user = telegram_user.user
        login(request, user)

        request.session['telegram_username'] = telegram_user.telegram_username
        return redirect('home')

    return HttpResponse("Ошибка авторизации через Telegram", status=400)


def login_with_telegram(request):
    token = generate_token()
    request.session['telegram_token'] = token
    bot_url = f'https://t.me/your_telegram_bot?start={token}'
    return redirect(bot_url)