from .models import ClientModel, GoodModel, OrderModel, OrderListModel
from django.forms import ModelForm


class ClientForm(ModelForm):
    class Meta:
        model = ClientModel
        fields = ('name', 'email', 'phone', 'address')
        labels = {'name': 'Наименование',
                  'email': 'Почта',
                  'phone': 'Номер телефона',
                  'address': 'Адрес'}


class GoodForm(ModelForm):
    class Meta:
        model = GoodModel
        fields = ('name', 'description', 'price_good', 'quantity_good', 'image')
        labels = {'name': 'Наименование',
                  'description': 'Описание',
                  'price_good': 'Стоимость',
                  'quantity_good': 'Кол-во осталось',
                  'image': 'Изображение'}


class OrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ('id_client',)
        labels = {'id_client': 'Клиент'}


class OrderListForm(ModelForm):
    class Meta:
        model = OrderListModel
        fields = ('id_good', 'id_order', 'count')
        labels = {'id_good': 'Товар',
                  'id_order': 'Заказ',
                  'count': 'Кол-во товара'}
