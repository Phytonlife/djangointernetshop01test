from django.contrib import admin
from mainapp.models import MainPageBD
# Register your models here.


#Можно создать класс редактор для улучшения видимости админки


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id","title","created_news","updated_news","public") # можно добавить видимость обьектов в админке
    list_display_links=("id","title") # сделать ссылкой разные поля в админке
    search_fields = ("title","content") # добавить поиск в админку и указать каие поля нужны для поиска
    list_editable= ("public",) # делать изменений прямо в таблице
    list_filter = ("title","created_news") # добавить фильтры в админку
    actions = ("public",)

admin.site.register(MainPageBD,NewsAdmin)