from django.contrib import admin
from .models import PokemonCard

# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name",)

admin.site.register(PokemonCard, PokemonAdmin)
