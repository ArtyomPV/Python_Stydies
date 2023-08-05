from django.shortcuts import render
from django.views.generic import ListView
from .models import Product


class ProductsList(ListView):
    model = Product  # модель, объекты которой необходимо выводить
    template_name = 'fastfood/products.html'  # указывает имя шаблона,
    # в котором будет лежать HTML, в нем будет инструкция о том как будут
    # выводиться наши объекты
    context_object_name = 'products'  # имя списка в котором лежат все объекты,
    # его нужно указать, чтобы обратиться к самому списку через HTML шаблон

