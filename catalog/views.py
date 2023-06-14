from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import handler
# Create your views here.


def main(request):
    # показ контента из html файла
    all_category = models.Category.objects.all()
    all_products = models.Product.objects.all()
    # получить переменую из фронта, если она есть
    search_value_from_front = request.GET.get('search')
    if search_value_from_front:
        all_products = models.Product.objects.filter(name__contains=search_value_from_front)
    print(search_value_from_front)
    # передача переменых бэка на фронт
    contex = {'all_categories': all_category, 'all_products': all_products}
    return render(request, 'index.html', contex)


def about_page(request):
    return HttpResponse(' привет мое имя самир <br>добро пожаловать на мой первый сайт ')


def film(request):
    return HttpResponse('какой фильм вы бы посмотрели')


def get_category_products(request, pk):
    # получить все товары из конкретной категории
    exact_category_products = models.Product.objects.filter(category__id=pk)
    # получить переменных из бэка на фронт
    contex = {"category_products": exact_category_products}
    return render(request, 'category.html', contex)


def get_pr(request, name, pk):
    # получить все товары из конкретной категории
    exact_products = models.Product.objects.get(id=pk, name=name)
    # получить переменных из бэка на фронт
    contex = {"product": exact_products}
    return render(request, 'product.html', contex)


def add_pr_to_cart(request, pk):
    # получить выбранныое количество продукта из фронт части
    quan = request.POST.get('pr_count')
    # находим сам продукт
    product_to_add = models.Product.objects.get(id=pk)
    # добавление данных
    models.UserCart.objects.create(user_id=request.user.id,
                                   user_product=product_to_add, user_product_quantity=quan,
                                   user_pr_price=int(quan)*product_to_add.price)
    return redirect('/')


def get_user_cart(request):
    # получить все товары из корзины
    cart = models.UserCart.objects.filter(user_id=request.user.id)
    # получить переменных из бэка на фронт
    contex = {"cart": cart}
    return render(request, 'user_cart.html', contex)


def complete_order(request):
    # вызываем корзину пользователя
    user_cart = models.UserCart.objects.filter(user_id=request.user.id)
    result_message = 'новый заказ(из сайта)\n\n'
    total = 0
    if request.method == 'POST':
        for cart in user_cart:
            result_message += f"название товара:{cart.user_product}\n" \
                          f"количество:{cart.user_product_quantity}\n"
            total += cart.user_product.price * cart.user_product_quantity
        result_message += f'итог: {total}'
        handler.bot.send_message(-1001982414088, result_message)
        user_cart.delete()
        return redirect('/')
    return render(request, 'user_cart.html', {"user_cart": user_cart})


def delete_from_cart(request, pk):
    product_to_delete = models.Product.objects.get(id=pk)
    models.UserCart.objects.filter(user_id=request.user.id, user_product=product_to_delete).delete()
    return redirect('/')
