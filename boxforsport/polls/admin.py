from django.contrib import admin
from .models import Habit

# Тепер звички з'являться в адмінці
admin.site.register(Habit)