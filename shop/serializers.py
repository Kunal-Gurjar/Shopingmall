from rest_framework import serializers

from shop.models import Product, Categories


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'