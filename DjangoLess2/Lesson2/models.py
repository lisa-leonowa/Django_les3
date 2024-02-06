import datetime

from django.db import models


class ClientModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date_registration = models.DateField(default=str(datetime.datetime.now()).split()[0])

    def __str__(self):
        return f'Клиент {self.name}, почта-{self.email}, телефон-{self.phone}'


class GoodModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price_good = models.IntegerField(default=1)
    quantity_good = models.IntegerField()
    date_add = models.DateField(default=str(datetime.datetime.now()).split()[0])

    def __str__(self):
        return f'Товар {self.name}, описание-{self.description}, стоимость-{self.price_good}'


class OrderModel(models.Model):
    id_client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    id_good = models.ForeignKey(GoodModel, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    date = models.DateField(default=str(datetime.datetime.now()).split()[0])

    def __str__(self):
        return f'Заказ: {self.id_client}, стоимость-{self.total_price}'
