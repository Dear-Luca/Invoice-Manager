from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name="home"),
    path('invoice/', views.invoice, name="invoice"),
    path('supplier/', views.supplier, name="supplier"),
    path('invoice/<int:id_code>/', views.details_invoice, name='details_invoice'),
    path('supplier/<str:id_code>/', views.details_supplier, name="details_supplier"),
    path('edit-invoice/', views.edit_invoice, name='edit_invoice'),
    path('edit-lines/', views.edit_lines, name="edit_lines"),
    path('add-lines', views.add_lines, name='add_lines')

]