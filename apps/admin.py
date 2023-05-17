from django.contrib import admin

from apps.models import Poll, Choice


# Register your models here.
@admin.register(Poll)
class ModelAdminPoll(admin.ModelAdmin):
    pass


@admin.register(Choice)
class ModelAdminChoice(admin.ModelAdmin):
    pass
