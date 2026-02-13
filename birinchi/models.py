from django.db import models

# Create your models here.

class Salom1(models.Model):
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="salom1/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Salom2(models.Model):
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="salom2/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Salom3(models.Model):
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="salom3/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Salom4(models.Model):
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="salom4/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Salom5(models.Model):
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="salom5/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name