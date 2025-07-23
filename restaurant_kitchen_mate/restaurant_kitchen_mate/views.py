from django.shortcuts import render
from django.views import generic
from .models import Dish, Cook

def index(request):
    return render(request, "your_app/index.html")


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "your_app/dish_list.html"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "your_app/dish_detail.html"


class CookListView(generic.ListView):
    model = Cook
    template_name = "your_app/cook_list.html"
