from django.db import models
import uuid


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Subcategories(BaseModel):

    subcategory_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=20)
    order = models.IntegerField(default=0)

    class Meta:
        db_table = 'Subcategories'

class Categories(BaseModel):

    category_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    subcategory = models.ManyToManyField(Subcategories)
    title = models.CharField(max_length=20)
    order = models.IntegerField(default=0)

    class Meta:
        db_table = 'Categories'

class Product(BaseModel):

    product_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.ManyToManyField(Categories)

    class Meta:
        db_table = 'Product'

