from django.db import models

# Create your models here.


class Links(models.Model):
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    text = models.CharField(max_length=78)
    url = models.CharField(max_length=2048)
    open_new_tab = models.BooleanField(default=False)

    # Relação de UM para MUITOS, UM SiteConfig tem vários Menu, O menu tem uma chave do SiteConfig
    site_config = models.ForeignKey(
        'SiteConfig', on_delete=models.CASCADE,
        default=None,
        null=True
    )

    def __str__(self):
        return self.text


class SiteConfig(models.Model):
    verbose_name = 'Site Config'
    verbose_name_plural = 'Site Config'

    title = models.CharField(max_length=78)
    site_name = models.CharField(max_length=78)
    description = models.CharField(max_length=278)

    warning = models.CharField(
        default='BE CAREFUL IF YOU DELETE THIS SITE CONFIG YOU WILL DELETE EVERYTHING',
        editable=False,
        max_length=78,
    )

    show_pagination = models.BooleanField(default=True)

    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
