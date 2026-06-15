import sqlite3

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#from boxforsport.polls.models import Habit

class log(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('app')
        return render(request, 'index.html')

    def post(self, request):
        # .strip() прибирає випадкові приховані пробіли
        username_to_login = request.POST.get('username', '').strip()
        password_to_login = request.POST.get('password', '')

        user = authenticate(request, username=username_to_login, password=password_to_login)

        if user is not None:
            login(request, user)
            return redirect('app')
        else:
            return render(request, 'index.html', {'error': "Невірне ім'я користувача або пароль."})


class reg(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('app')
        return render(request, 'register.html')

    def post(self, request):
        username_to_reg = request.POST.get('username', '').strip()
        pass1 = request.POST.get('password1', '')
        pass2 = request.POST.get('password2', '')

        if pass1 != pass2:
            error = "Паролі не збігаються!"
        elif len(pass1) < 3:
            error = "Пароль має бути не менше 3 символів!"
        elif User.objects.filter(username=username_to_reg).exists():
            error = "Користувач з таким ім'ям вже існує."
        else:
            new_user = User.objects.create_user(username=username_to_reg, password=pass1)
            login(request, new_user)
            return redirect('app')

        return render(request, 'register.html', {'error': error})


class main(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM polls_habit")
        rows = cursor.fetchall()

        conn.close()
        #habits = Habit.objects.all()
        print(rows[0])
        return render(request, 'app.html', {'habits': rows})
        #return render(request, 'app.html')


# Обов'язково додаємо функціонал для виходу з системи
def logout_view(request):
    logout(request)
    return redirect('login')

class profile_view(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'profile.html', {'user': request.user})

class stats_view(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'stats.html')