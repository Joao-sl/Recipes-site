from site_config.models import SiteConfig


#  Context processor, ele injeta valores em todos os templates, basta registrar-lo no settings.py
def site_configs(request):
    data = SiteConfig.objects.first()
    return {
        'site_config': data
    }
