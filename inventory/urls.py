from django.urls import path, include
# from . views import VendorModel, CustomerModel, CustomerDetailView, VendorDetailView, EmployeeModel, EmployeeDetailView, CategoryModel, CategoryDetailView, ProductModel, ProductDetailView, ProducttypeModel, ProducttypeDetailView, WarrantyModel, WarrantyDetailView, PurchaseModel, PurchaseDetailView, TransactionModel, TransactionDetailView 
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register('vendor', VendorModel, basename='vendor')
# # router.register('customer', CustomerModel, basename='customer')


urlpatterns = [
    # path('api/', include(router.urls)),
    path('vendor/', VendorModel.as_view()),
    path('customer/', CustomerModel.as_view()),
    path('employee/', EmployeeModel.as_view()),
    path('category/', CategoryModel.as_view()),
    path('product/', ProductModel.as_view()),
    path('producttype/', ProducttypeModel.as_view()),
    path('warranty/', WarrantyModel.as_view()),
    path('transaction/', TransactionModel.as_view()),
    path('purchase/', PurchaseModel.as_view()),
    path('vendor/<int:id>', VendorDetailView.as_view()),
    path('customer/<int:id>', CustomerDetailView.as_view()),
    path('employee/<int:id>', EmployeeDetailView.as_view()),
    path('category/<int:id>', CategoryDetailView.as_view()),
    path('purchase/<int:id>', PurchaseDetailView.as_view()),
    path('producttype/<int:id>', ProducttypeDetailView.as_view()),
    path('transaction/<int:id>', TransactionDetailView.as_view()),
    path('product/<int:id>', ProductDetailView.as_view()),
    path('warranty/<int:id>', WarrantyDetailView.as_view())
]
