from django.contrib import admin

# Register your models here.
from .models import ClientModel, GoodModel, OrderModel, OrderListModel


class ClientModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'date_registration')


class GoodModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price_good', 'quantity_good', 'date_add', 'image')
    fields = [('name', 'price_good', 'quantity_good'), 'description', 'image', 'date_add']


class OrderListModelAdmin(admin.TabularInline):
    model = OrderListModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id_client', 'total_price', 'date')
    inlines = [OrderListModelAdmin]


# admin.site.register(ClientModel)
# admin.site.register(GoodModel)
# admin.site.register(OrderModel)
# admin.site.register(OrderListModel)
admin.site.register(ClientModel, ClientModelAdmin)
admin.site.register(GoodModel, GoodModelAdmin)
# admin.site.register(OrderModel, OrderModelAdmin)
# admin.site.register(OrderListModel, OrderListModelAdmin)
