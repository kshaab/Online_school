from django.contrib import admin

from users.models import User, Payments

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "town")
    list_filter = ("town",)
    search_fields = ("email", "town")

@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("user", "payment_amount")
    list_filter = ("user", "payment_method")
    search_fields = ("payment_date",)


