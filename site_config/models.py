from utils.img_resizer import resize_image, if_image_changed_favicon
from django.db import models


class SiteConfig(models.Model):
    verbose_name = 'Site Config'
    verbose_name_plural = 'Site Config'

    title = models.CharField(max_length=78)
    site_name = models.CharField(max_length=78)
    description = models.CharField(max_length=278)
    tiktok = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        help_text='Cole o link completo do perfil, Exemplo: https://www.tiktok.com/@exemplo'
    )
    twitter = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)

    domain = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text='Não insira o "https://" apenas o domínio, Exemplo nomedosite.com'
    )

    warning = models.CharField(
        default='BE CAREFUL IF YOU DELETE THIS SITE CONFIG YOU WILL DELETE EVERYTHING',
        editable=False,
        max_length=78,
    )

    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m',
        null=True,
    )

    footer_logo = models.ImageField(
        upload_to='assets/footer_logo/%Y/%m',
        null=True,
    )

    def save(self, *args, **kwargs):
        if self.favicon and if_image_changed_favicon(self):
            resized_favicon = resize_image(
                self.favicon,
                height=32,
                width=32,
                quality=100,
                optimize=True
            )
            self.favicon = resized_favicon
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
