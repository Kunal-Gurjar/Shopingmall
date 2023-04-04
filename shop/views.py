from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Categories, Product
from shop.serializers import ProductSerializer, CategorieSerializer
from shop.utils import responsedata


class ProductsView(APIView):

    def post(self, request):
        price = request.data.get('price')
        if price <= 0:
            return Response(responsedata(False, "price can't less zero"), status=status.HTTP_400_BAD_REQUEST)
        category = request.data.get('category_id')
        data = {
            'category': category,
            'name': request.data.get('name'),
            'price': request.data.get('price')
        }

        serializer = ProductSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(responsedata(True, 'Products created'), status=status.HTTP_200_OK)
        except:
            return Response(responsedata(False, 'something went wrong'), status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):

        pro_data = Product.objects.filter().values('product_id', 'name', 'price', 'category')

        return Response(responsedata(True, 'available Product', pro_data), status=status.HTTP_200_OK)


class ProductsList(APIView):

    def get(self, request, pk):
        try:
            records = Product.objects.filter(product_id=pk).values('product_id', 'name', 'price', 'category')
            data = {
                'Id': records[0]['product_id'],
                'Name': records[0]['name'],
                'Price': records[0]['price'],
                'Category': records[0]['category'],
            }
            return Response(responsedata(True, "Product Details", data),status=status.HTTP_200_OK)
        except:
            return Response(responsedata(True, "Product does not exist"),status=status.HTTP_200_OK)


class CategoryView(APIView):

    def post(self, request):

        data = {
            'subcategory': request.data.get('subcategory'),
            'title': request.data.get('title'),
            'order': request.data.get('order')
        }

        serializer = CategorieSerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(responsedata(True, 'Categorie created'), status=status.HTTP_200_OK)
        except:
            return Response(responsedata(False, 'something went wrong'), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        pro_data = Categories.objects.filter().values('category_id','title','order','product__product_id', 'subcategory')

        return Response(responsedata(True, 'available Product', pro_data), status=status.HTTP_200_OK)


class CategoryList(APIView):

    def get(self, request, pk):
        try:
            records = Categories.objects.filter(category_id=pk).values('category_id','title','order','product__product_id', 'subcategory')
            data = {
                'Id': records[0]['category_id'],
                'Name': records[0]['title'],
                'Order': records[0]['order'],
                'Product': records[0]['product__product_id'],
                'Subcategory': records[0]['subcategory'],
            }
            return Response(responsedata(True, "Category Details", data),status=status.HTTP_200_OK)
        except:
            return Response(responsedata(True, "Category does not exist"),status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            Categories.objects.get(category_id=pk).delete()

            return Response(responsedata(True, 'Category Celeted'), status=status.HTTP_200_OK)
        except:
            return Response(responsedata(True, "Category does not exist"),status=status.HTTP_400_BAD_REQUEST)

