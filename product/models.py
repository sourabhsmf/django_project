from django.db import models
from django.core.validators import *

# Create your models here.


class Product(models.Model):
    name = models.SlugField(name="productName" , max_length=200 , unique=True , null = False , validators=[validate_slug])
    price = models.IntegerField(name="productPrice" , null = False , validators=[integer_validator])
    url = models.URLField(name="productURL" , max_length=2000 , unique=True , null = False )
    picture = models.ImageField(name="productImage" , max_length=1000 , upload_to = "assets/images/products/" , null = True , validators = [validate_image_file_extension])    
