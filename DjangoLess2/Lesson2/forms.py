from .models import ClientModel, GoodModel, OrderModel, OrderListModel
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
        fields = ('id_client',)


class OrderListForm(ModelForm):
    class Meta:
        model = OrderListModel
        fields = ('id_good', 'id_order', 'count')
