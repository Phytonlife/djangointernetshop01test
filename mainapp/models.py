from django.db import models
#Основные модели
#Product
#Category
#CartProduct vremennaya korzina
#Cart Korzina
#Order zakaz

#Customer покупатель
#Specification harakteristiki categorii

# class Category(models.Model):
#     name=models.CharField(max_length=250,verbose_name="Имя категории")
#     slug=models.SlugField(unique=True)
#
#     def __str__(self):
#         return self.name
# class Product(models.Model):
#     category=models.ForeignKey(Category,verbose_name="Категория",on_delete=models.CASCADE)
#     title=models.CharField(max_length=255,verbose_name="Наименования")
#     Slug=models.SlugField(unique=True)
#     image=models.ImageField(verbose_name="Изображение")
#     description = models.TextField(null=True,verbose_name="Описание")
#     price = models.DecimalField(max_digits=9,decimal_places=2,verbose_name="Цена")
#
#
#     def __str__(self):
#         return self.title
# class CartProduct(models.Model):
#     user = models.ForeignKey("Customer",verbose_name="Покупатель",on_delete=models.CASCADE)
#     Cart = models.ForeignKey("Cart",verbose_name="Корзина",on_delete=models.CASCADE)
#     product = models.ForeignKey(Product,verbose_name="Товар",on_delete=models.CASCADE)
#     qty = models.PositiveIntegerField(default=1)
#     final_price=models.DecimalField(max_digits=9,decimal_places=2,verbose_name="Общая цена")
#
#     def __str__(self):
#         return f"Продукт {self.product.title} (для корзины)"
# class Cart(models.Model):
#     owner = models.ForeignKey("Customer",verbose_name="Владелец",on_delete=models.CASCADE)
#     product = models.ManyToManyField(CartProduct,blank=True)
#     total_product = models.PositiveIntegerField(default=0)
#     final_price=models.DecimalField(max_digits=9,decimal_places=2,verbose_name="Общая цена")
#
#     def __str__(self):
#         return f"{str(self.id)}"
# Create your models here.
class MainPageBD(models.Model):
    #можно указать параметр verbose_name="Название" тобы видимость в админке была на русском языке по умолчанию стоит название переменной
    title=models.CharField(max_length=50,verbose_name="Название")
    content = models.TextField(blank=True,verbose_name="Описание")
    created_news=models.DateTimeField(auto_now_add=True,verbose_name="Дата публикаций")
    updated_news=models.DateTimeField(auto_now=True,verbose_name="Дата изменений")
    image=models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    public = models.BooleanField(default=True, verbose_name="Публикация новости")
    price=models.DecimalField(max_digits=7,decimal_places=2,blank=True,null=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Новость"
        verbose_name_plural = "Новости"

        ordering=["-created_news"]
# News.objects.all() взять все данные ,
# News.objects.get(pk=2) or News.objects.get(title="News 5") взять один обьект
# News.objects.filter(title="News 5") or News.objects.filter(public=True)
#News.objects.order_by("title") сортировка обьектов по тайтлу News.objects.order_by("-title") сортировка наоборот
# Чтобы изменить запись news2=News.objects.get(pk=2) надо взять ее , потом news2.title="News 2" затем news2.save() в 3 этапа меняется
# Чтобы удалить запись news3=News.objects.get(pk=3) надо взять ее ,news3.delete()  2 этапа
#News.objects.exlude(title= "News 5") исключение за исключение
# https://django.fun/docs/django/ru/3.1/ref/models/querysets/ здесь расписаны все qwerry set списки действия с обьектами бд в views
