from django.shortcuts import render
from django.views import generic
from kitchen.models import Dish, Cook


def index(request):
    return render(request, "restaurant/index.html")


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "restaurant/dish_list.html"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "restaurant/dish_detail.html"


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    template_name = "restaurant/dish_form.html"
    success_url = "/dishes/"


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "restaurant/dish_form.html"
    success_url = "/dishes/"


class DishDeleteView(generic.DeleteView):
    model = Dish
    template_name = "restaurant/dish_confirm_delete.html"
    success_url = "/dishes/"


class CookListView(generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "restaurant/cook_list.html"


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "restaurant/cook_detail.html"


class CookCreateView(generic.CreateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "email", "years_of_experience")
    template_name = "restaurant/cook_form.html"
    success_url = "/cooks/"


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "email", "years_of_experience")
    template_name = "restaurant/cook_form.html"
    success_url = "/cooks/"


class CookDeleteView(generic.DeleteView):
    model = Cook
    template_name = "restaurant/cook_confirm_delete.html"
    success_url = "/cooks/"
