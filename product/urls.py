from django.urls import path 
from . import views

app_name = 'product'
urlpatterns = [

    path('', views.index , name='index'),
    path('add', views.add , name='add'),
    path('delete/<int:productId>', views.delete , name='delete'),
    path('view/<int:productId>', views.view , name='view'),
]