from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('about', views.about_page),
    path('film', views.film),
    path('category/<int:pk>', views.get_category_products),
    path('product/<str:name>/<int:pk>', views.get_pr),
    path("add-product-to-cart/<int:pk>", views.add_pr_to_cart),
    path('cart/', views.get_user_cart),
    path('del_item/<int:pk>', views.delete_from_cart),
    path('-'),
]
