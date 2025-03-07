from django.db import models
from django import forms
# Create your models here.

class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    categorie = models.CharField(max_length=20)
    image = models.ImageField()
    description = models.CharField(max_length=500)
    quantite = models.IntegerField()


class User(models.Model):
    class Role:
        CLIENT = 1
        SELLER = 2


    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.IntegerField()

    @classmethod
    def authenticate(cls, username, password, role):
        result = cls.objects.filter(username=username, password=password, role=role)
        if result:
            return True, result[0] 
        return False, None
    
    @classmethod
    def create(cls, username, password, role):
        user = cls(username=username, password=password, role=role)
        user.save()
        return user

    @classmethod
    def get(cls, username):
        try:
            return cls.objects.get(username=username)
        except cls.DoesNotExist:
            return None
        
    def get_username(self):
        return self.username
    
    def get_role(self):
        return self.role
    
    def __str__(self) -> str:
        return self.username + " " + str(self.role)
    

class acheter(models.Model):
    id = models.AutoField(primary_key=True)
    id_product = models.CharField(max_length=100)
    id_client = models.CharField(max_length=10)
    total_amount = models.FloatField()