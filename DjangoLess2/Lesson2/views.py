import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import ClientModel, GoodModel, OrderModel, OrderListModel
from .forms import ClientForm, GoodForm, OrderForm, OrderListForm
from django.http import Http404
from django.db.models import Q


def read_client(request):
    dataset = ClientModel.objects.all()
    return render(request, 'listview.html', context={'dataset': dataset})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        return render(request, 'create.html', context={'form': ClientForm})


def client_detail_view(request, id):
    try:
        data = ClientModel.objects.get(id=id)
    except ClientModel.DoesNotExist:
        raise Http404('Клиент не существует')
    return render(request, 'detailview.html', context={'data': data})


def client_orders(request, id):
    try:
        order = OrderModel.objects.filter(id_client=id)
    except OrderModel.DoesNotExist:
        raise Http404('Клиент не существует')

    name_client = ClientModel.objects.get(id=id).name

    answer = []
    for i in order:
        answer.append(i.order_goods(id_order=i.id))
    context = {'data': answer,
               'name_client': name_client}
    return render(request, 'clients_orders.html', context=context)


def good_specified_date(time_delta, id_client):
    current_date = datetime.datetime.now()
    answer_date = current_date - datetime.timedelta(days=time_delta)
    try:
        data = OrderModel.objects.filter(Q(id_client=id_client) & Q(date__range=(answer_date, current_date)))
    except OrderModel.DoesNotExist:
        raise Http404('Клиент не существует')
    list_goods = []
    for i in data:
        goods = OrderListModel.objects.filter(id_order=i.id)
        for j in goods:
            list_goods.append(j)
        # list_goods.append(GoodModel.objects.get(id=i.id_good.id))
    return list(set(list_goods))


def client_goods(request, id_client):
    # — за последние 7 дней(неделю)
    answer_7 = good_specified_date(7, id_client)
    # — за последние 30 дней(месяц)
    answer_30 = good_specified_date(30, id_client)
    # — за последние 365 дней(год)
    answer_365 = good_specified_date(365, id_client)

    return render(request, 'clients_goods.html', context={'data_7': answer_7,
                                                          'data_30': answer_30,
                                                          'data_365': answer_365})


def read_good(request):
    dataset = GoodModel.objects.all()
    return render(request, 'listview.html', context={'dataset': dataset})


def create_good(request):
    if request.method == 'POST':
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # картинка сохраняется в папку Django_less2/DjangoLess2/media
            return redirect('/goods')
        else:
            return render(request, 'create_good.html', context={'form': GoodForm})
    else:
        return render(request, 'create_good.html', context={'form': GoodForm})


def update_good(request, id):
    try:
        old_data = get_object_or_404(GoodModel, id=id)
    except Exception:
        raise Http404('Такой товар не существует')
    if request.method == 'POST':
        form = GoodForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect(f'/goods')
    else:
        form = GoodForm(instance=old_data)
        return render(request, 'update.html', context={'form': form})


def read_order(request):
    dataset = OrderModel.objects.all()
    return render(request, 'listview.html', context={'dataset': dataset})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/orders/create/order_list')
    else:
        return render(request, 'create.html', context={'form': OrderForm})


def create_order_list(request):
    if request.method == 'POST':
        form = OrderListForm(request.POST)
        if form.is_valid():
            form.save()
            order_list = OrderListModel.objects.all().order_by('id').last()
            order_list.add_to_order()
            return redirect('/orders/create/order_list')
    else:
        return render(request, 'create.html', context={'form': OrderListForm})


def delete_order(request, id):
    try:
        data = get_object_or_404(OrderModel, id=id)
    except Exception:
        raise Http404('Такого заказа не существует')

    if request.method == 'POST':
        data.delete()
        return redirect('/orders')
    else:
        return render(request, 'delete.html')
