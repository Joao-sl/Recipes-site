# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from PIL import Image
# from io import BytesIO
# from django.core.files.base import ContentFile
# from recipes.models import Category


# def resize_image(image_field, height, width, quality=60, optimize=True):
#     if image_field:
#         img = Image.open(image_field)
#         img_resized = img.resize((width, height))

#         # Permite que possamos trabalhar com a imagem redimensionada sem salvar no disco.
#         img_io = BytesIO()

#         # Salvamos a imagem redimensionada no buffer (criado acima) em memória
#         img_resized.save(img_io, format=img.format)

#         # Ponteiro do arquivo volta para o começo.
#         img_io.seek(0)

#         # Substituir a imagem original com a redimensionada
#         image_field.save(
#             # Manter o nome original do arquivo
#             image_field.name,

#             # Salva o conteúdo da imagem no campo
#             ContentFile(img_io.read()),

#             # Não salvar o modelo ainda, pois estamos manipulando o campo
#             save=False
#         )


# # receiver: Decorador do Django usado para conectar a função a um sinal específico.
# # pre_save: É um sinal do Django que é disparado antes de um objeto ser salvo no banco de dados.
# @receiver(pre_save, sender=Category)
# def resize_category_image(sender, instance, **kwargs):

#     if instance.category_image:
#         resize_image(
#             instance.category_image,
#             height=168,
#             width=168,
#             quality=80,
#         )
