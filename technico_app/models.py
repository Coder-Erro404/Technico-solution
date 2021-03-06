from django.db import models
from ckeditor.fields import RichTextField

Catagory_CHOICES =(
    ("1", "hardware"),
    ("2", "Laptop"),
    ("3", "Computer"),
    ("4", "Web Design"),
    ("5", "Accessories"),
    ("6", "Refurbished"),
    ("7", "CCTV"),
    ("8", "Repairing")
)

class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     F_name= models.CharField(max_length=255)
     L_name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "Message from " + self.F_name + ' - ' + self.email

class project(models.Model):
     sno= models.AutoField(primary_key=True)
     p_name= models.CharField(max_length=255)
     author= models.CharField(max_length=225)
     content= models.TextField()
     Decri= models.CharField(max_length=255)
     p_url= models.CharField(max_length=255)
     Img = models.ImageField(upload_to='add_images')
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "Project_Name"+ " :  "+ self.p_name 

class blog(models.Model):
     sno= models.AutoField(primary_key=True)
     header= models.CharField(max_length=500)
     cat= models.CharField( max_length=1,choices = Catagory_CHOICES)
     Author= models.CharField(max_length=255)
     Img = models.FileField(upload_to='add_images')
     content= RichTextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "header"+ " :  "+ self.header 

class product(models.Model):
     sno= models.AutoField(primary_key=True)
     cat= models.CharField( max_length=1,choices = Catagory_CHOICES)
     product_name= models.CharField(max_length=500)
     product_price= models.CharField(max_length=100)
     product_image = models.FileField(upload_to='add_images')
     content= RichTextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "product_name"+ " :  "+ self.product_name 

class Document(models.Model):
     sno= models.AutoField(primary_key=True)
     header= models.CharField(max_length=500)
     document_img = models.ImageField(upload_to='add_images') 
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "header"+ " :  "+ self.header 
class impotantImage(models.Model):
     sno= models.AutoField(primary_key=True)
     header= models.CharField(max_length=500)
     document_img = models.ImageField(upload_to='add_images') 
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "header"+ " :  "+ self.header 
     

class addnote(models.Model):
     sno= models.AutoField(primary_key=True)
     header= models.CharField(max_length=500)
     Author= models.CharField(max_length=255)
     content= RichTextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
      return "header"+ " :  "+ self.header 