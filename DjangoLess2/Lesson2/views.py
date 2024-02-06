from django.shortcuts import render, redirect, get_object_or_404
from .models import ClientModel, GoodModel, OrderModel
from .forms import ClientForm, GoodForm, OrderForm
from django.http import Http404


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


def read_good(request):
    dataset = GoodModel.objects.all()
    return render(request, 'listview.html', context={'dataset': dataset})


def create_good(request):
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/goods')
    else:
        return render(request, 'create.html', context={'form': GoodForm})


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
            return redirect('/orders')
    else:
        return render(request, 'create.html', context={'form': OrderForm})


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