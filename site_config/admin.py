from django.contrib import admin
from site_config.models import SiteConfig


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description', 'warning',
    list_display_links = 'id', 'title',

    # Se já existir um site_config registrado o ADICIONAR no painel de administrador, ficará oculto

    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()
