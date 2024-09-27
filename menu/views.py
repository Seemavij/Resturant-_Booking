from django.shortcuts import render
from .models import Menu, Category


def menu_list(request):
    """
    Creates menu
    """
    menu_list = Menu.objects.all()
    categories = Category.objects.all()

    context = {
        'menu_list': menu_list,
        'categories': categories,
    }

    return render(request, '../templates/menu.html', context)
