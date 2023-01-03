from django.contrib import messages
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CustomerForm, OrderForm
from .models import Customer, Order


def create_customer(request):

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Customer.objects.create(
                **form.cleaned_data
            )
            obj.save()
    else:
        form = CustomerForm()
    return render(request, 'orders/create.html', {'form': form})


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = Order.objects.create(
                **form.cleaned_data
            )
            obj.save()
    else:
        form = OrderForm()
    return render(request, 'orders/create.html', {'form': form})


class OrderAPIViewSet(APIView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']

        if Order.objects.filter(customer_id=pk).exists():
            orders_price = [order.price for order in Order.objects.filter(customer_id=pk)]
            price = sum(orders_price)
            count = len(orders_price)
            avg = price/count
            context = {
                'price': price,
                'count': count,
                'avg': avg
            }
            return Response(context)
        else:
            return Response('No orders')
