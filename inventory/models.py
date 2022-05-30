from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length = 100)
    contact = models.IntegerField()
    dateOfJoining = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField(max_length= 100)
    contact_number= models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Producttype(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    producttype = models.ForeignKey("Producttype", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)
    purchase = models.ForeignKey("Purchase", on_delete=models.CASCADE)
        
    
class Warranty(models.Model):
    product = models.ForeignKey("product", on_delete=models.CASCADE)
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)
    purchase = models.ForeignKey("Purchase", on_delete=models.CASCADE)
    
class Transaction(models.Model):
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    product_issuedate = models.DateTimeField(auto_now_add=True)
    
class Purchase(models.Model):
    dateofpurchase = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField() 