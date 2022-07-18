from django.shortcuts import render
from .models import *
# from .models import Employee, Customer, Vendor, Product, Producttype, Category, Transaction, Purchase, Warranty
# from .serializers import VendorSerializer, CustomerSerializer, EmployeeSerializer, ProductSerializer, PurchaseSerializer, TransactionSerializer, WarrantySerializer, CategorySerializer, ProducttypeSerializer
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse



# Create your views here.

class VendorModel(APIView):
    def get(self,request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)
    
    def post(self,request): 
        serializer = VendorSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VendorDetailView(APIView):
    def get_object(self, id):
        try:
            return Vendor.objects.get(id=id)
        
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        vendor = self.get_object(id)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    
    def put(self, request, id):
        vendor = self.get_object(id)
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        vendor = self.get_object(id)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EmployeeModel(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetailView(APIView):    
    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        
        except Employee.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee)    
        return Response(serializer.data)
    
    def put(self, request, id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee = self.get_object(id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomerModel(APIView):
    def get(self,request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CustomerSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView):    
    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        
        except Customer.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        customer = self.get_object(id)
        serializer = CustomerSerializer(customer)    
        return Response(serializer.data)
    
    def put(self, request, id):
        customer = self.get_object(id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        customer = self.get_object(id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CategoryModel(APIView):
    def get(self,request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetailView(APIView):    
    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        
        except Category.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        category = self.get_object(id)
        serializer = CategorySerializer(category)    
        return Response(serializer.data)
    
    def put(self, request, id):
        category = self.get_object(id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProducttypeModel(APIView):
    def get(self, request):
        producttypes = Producttype.objects.all()
        serializer = ProducttypeSerializer(producttypes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProducttypeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProducttypeDetailView(APIView):
    def get_object(self, id):
        try:
            return Producttype.objects.get(id=id)
        
        except Producttype.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        producttype = self.get_object(id)
        serializer = ProducttypeSerializer(producttype)
        return Response(serializer.data)
    
    def put(self, request, id):
        producttype = self.get_object(id)
        serializer = ProducttypeSerializer(producttype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        producttype = self.get_object(id)
        producttype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductModel(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailView(APIView):
    def get_object(self, request, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class WarrantyModel(APIView):
    def get(self, request):
        warranties = Warranty.objects.all()
        serializer = WarrantySerializer(warranties, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WarrantySerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WarrantyDetailView(APIView):
    def get_object(self, id):
        try:
            return Warrant.objects.get(id=id)
        except WarrantyDoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        warranty = self.get_object(id)
        serializer = WarrantySerializer(warranty)
        return Response(serializer)
    
    def put(self, request, id):
        warranty = self.get_object(id)
        serializer = WarrantySerializer(warranty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        warranty = self.get_object(id)
        warranty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class PurchaseModel(APIView):
#     def get(self, request):
#         purchases = Purchase.objects.all()
#         serializer = PurchaseSerializer(purchases, many = True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = PurchaseSerializer(data=request.data)  
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class PurchaseDetailView(APIView):
    def get_object(self, id):
        try:
            return Purchase.objects.get(id=id)
        except Purchase.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        warranty = self.get_object(id)
        serializer = PurchaseSerializer(warranty)
        return Response(serializer.data)
    
    def put(self, request, id):
        warranty = self.get_object(id)
        serializer = PurchaseSerializer(warranty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        purchase = self.get_object(id)
        purchase.delete()
        
class TransactionModel(APIView):
    def get(self, request):
        transactions = Transaction.object.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TransactionDetailView(APIView):
    def get_object(self, id):
        try:
            return Transaction.objects.get(id=id)
        except Transaction.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        transaction = self.get_object(id)
        serializer = TransactionSerializer(warranty)
        return Response(serializer.data)
    
    def put(self, request, id):
        transaction = self.get_object(id)
        serializer = TransactionSerializer(transaction, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        transaction = self.get_object(id)
        transaction.delete()
