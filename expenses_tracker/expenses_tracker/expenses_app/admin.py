from django.contrib import admin

from expenses_tracker.expenses_app.models import Profile, Expense


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    pass


@admin.register(Expense)
class AdminExpense(admin.ModelAdmin):
    pass
