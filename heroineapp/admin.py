from django.contrib import admin
from .models import CustomUser, SubUser, Brand, Category, Product

# from django.contrib.admin.models import LogEntry
# LogEntry.objects.all().delete()


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "gender", "age"]


@admin.register(SubUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "age"]

@admin.register(Brand)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["brand_name", "discount"]

@admin.register(Category)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["name", "brand"]

@admin.register(Product)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
