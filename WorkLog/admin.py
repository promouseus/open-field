from django.contrib import admin

from .models import Customer, Task, Logbook

admin.site.register(Customer)
admin.site.register(Task)
admin.site.register(Logbook)
