from django.contrib import admin
from site_config.models import Links, SiteConfig

# Register your models here.

# @admin.register(Links)
# class LinksAdmin(admin.ModelAdmin):
#     list_display = 'id', 'text', 'url', 'open_new_tab',
#     list_display_links = 'id', 'text',


# Exibe os Links dentro do site_configs, (apenas para praticidade)
class LinksInLine(admin.TabularInline):
    model = Links
    extra = 2


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description', 'warning',
    list_display_links = 'id', 'title',
    inlines = LinksInLine,

    # Se já existir um site_config registrado o ADICIONAR no painel de administrador, ficará oculto
    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()
