from .models import ClientModel, GoodModel, OrderModel
from django.forms import ModelForm


class ClientForm(ModelForm):
    class Meta:
        model = ClientModel
        fields = ('name', 'email', 'phone', 'address')


class GoodForm(ModelForm):
    class Meta:
        model = GoodModel
        fields = ('name', 'description', 'price_good', 'quantity_good')


class OrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ('id_client', 'id_good', 'total_price')
