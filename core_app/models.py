from django.db import models


class Company_Story(models.Model):
    title = models.CharField(max_length=200)
    p1 = models.CharField(max_length=250, blank=True)
    p2 = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to="uploads/company")


class Team(models.Model):
    member_name = models.CharField(max_length=150)
    job = models.CharField(max_length=250)
    image = models.ImageField(upload_to="team/")
    is_manager = models.BooleanField(default=False)
    first_member = models.BooleanField(default=False)


class Dashboard(models.Model):
    clients = models.IntegerField()
    products = models.IntegerField()
    services = models.IntegerField()
    employees = models.IntegerField()


class Stories(models.Model):
    story_title = models.CharField(max_length=250)
    body = models.CharField(max_length=250)
    story_image = models.ImageField(upload_to="story/images", blank=True)


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=250)
    product_image = models.ImageField(upload_to="products/", blank=True)
