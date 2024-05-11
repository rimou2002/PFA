from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, default=None)
    description = models.ForeignKey('Description', on_delete=models.CASCADE, default=None)
    reviews = models.ForeignKey('Reviews', on_delete=models.CASCADE, default=None)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()
    image = models.ImageField(upload_to='produits/')
    image2 = models.ImageField(upload_to='produits/')
    image3 = models.ImageField(upload_to='produits/')
    size = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    effects = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    reference = models.CharField(max_length=255)

class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    reviewstexte = models.TextField()
    reviewsnumber = models.DecimalField(max_digits=3, decimal_places=1)

class Description(models.Model):
    id = models.AutoField(primary_key=True)
    descriptiontexte = models.TextField()
    Ingredients = models.TextField()
    Flavors = models.TextField()
    Recommendedusage = models.TextField()

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

class Admin(User):
    department = models.CharField(max_length=255)

class Manager(User):
    department = models.CharField(max_length=255)

class Client(User):
    address = models.TextField()
    tel = models.CharField(max_length=20)
    username = models.CharField(max_length=255)
    account_creation_date = models.DateField()
