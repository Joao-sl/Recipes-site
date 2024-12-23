import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from recipes import models


def resize_image(image_field, height, width, quality=80, optimize=True):
    if image_field:
        img = Image.open(image_field)
        img_resized = img.resize((width, height))

        # Cria uma 'sala' na memória para que possamos salvar a imagem.
        img_io = BytesIO()

        # Salvamos a imagem redimensionada no buffer (criado acima) em memória.
        img_resized.save(
            img_io,
            format=img.format,
            quality=quality,
            optimize=optimize,
        )

        # Ponteiro do arquivo volta para o começo.
        img_io.seek(0)

        # Separa Nome da imagem da extensão (Ex .png .jpeg), name= é necessário para o ContentFile.
        file_name, file_extension = os.path.splitext(image_field.name)
        new_file_name = f"{file_name}_resized{file_extension}"

        # ContentFile Converte a imagem em memória para um formato que o Django pode salvar.
        return ContentFile(img_io.read(), name=new_file_name)


def if_image_changed(recipe_instance):
    """
    Essa função apenas verifica se a imagem foi alterada ao salvar uma alteração qualquer no django admin, por exemplo se você apenas mudou apenas o nome da receita e não a imagem dela, isso para evitar que as pastas das imagens fiquem aninhadas todas vez que uma alteração for salva no django admin.
    """
    # from recipes.models import Recipe
    if not recipe_instance.pk:
        return True  # Se não tem pk, a imagem é nova.
    try:
        # Busca a receita antiga no banco de dados.
        original_recipe = models.Recipe.objects.get(pk=recipe_instance.pk)
        # Verifica se a imagem do banco de dados é diferente da imagem da instância que está sendo salva.
        return original_recipe.recipe_image.url != recipe_instance.recipe_image.url  # type: ignore
    except models.Recipe.DoesNotExist:
        return False


def if_image_changed_category(category_instance):
    """
    Essa função apenas verifica se a imagem foi alterada ao salvar uma alteração qualquer no django admin, por exemplo se você apenas mudou apenas o nome e não a imagem dela, isso para evitar que as pastas das imagens fiquem aninhadas todas vez que uma alteração for salva no django admin.
    """
    # from recipes.models import Category
    if not category_instance.pk:
        return True
    try:
        original_category = models.Category.objects.get(
            pk=category_instance.pk)
        return original_category.category_image.url != category_instance.category_image.url  # type: ignore
    except models.Category.DoesNotExist:
        return False


def if_image_changed_favicon(site_config_instance):
    """
    Essa função apenas verifica se a imagem foi alterada ao salvar uma alteração qualquer no django admin, por exemplo se você apenas mudou apenas o nome e não a imagem dela, isso para evitar que as pastas das imagens fiquem aninhadas todas vez que uma alteração for salva no django admin.
    """
    from site_config.models import SiteConfig
    if not site_config_instance.pk:
        return True
    try:
        original_site_config = SiteConfig.objects.get(
            pk=site_config_instance.pk)
        return original_site_config.favicon.url != site_config_instance.favicon.url  # type: ignore
    except SiteConfig.DoesNotExist:
        return False
