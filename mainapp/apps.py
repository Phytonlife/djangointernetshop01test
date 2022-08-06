from django.apps import AppConfig
#Изменить названия в приложения в админке

class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'
    verbose_name="Новости"
