from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images', null=True, blank=True)


    def __str__(self):
        return self.title


class ProductType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель продукта

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    duration = models.IntegerField()  # Длительность в месяцах или других единицах измерения
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skin = models.ImageField(upload_to='skins', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)


class Purchase(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def is_active(self):
        # Проверка активности покупки, например, сравнение с текущей датой
        # в соответствии с длительностью product
        if self.product.duration > 0:
            expiration_date = self.purchase_date + timezone.timedelta(days=self.product.duration * 30)
            return expiration_date > timezone.now()
        else:
            # Если длительность равна 0, подписка действительна бессрочно
            return True