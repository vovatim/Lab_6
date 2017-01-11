from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import TovarModel


def index(request):
    return HttpResponse("Hello, world!")

class ExampleView(View):
    def get(self, reguest):
        return render(reguest, 'example.html', {'my_variable':'Здесь объявляется переменная', 'list': [1,2,3]})

class OrdersView(View):
    def get(self, request):
        data = {

            'orders': TovarModel.objects.all()

        }
        return render (request, 'orders.html', data)

class OrderView(View):
    def get(self, request, id):
        data = \
        {
            'orders':TovarModel.objects.filter(pk=id)
        }
        print(data)
        return render(request, 'orders.html', data)