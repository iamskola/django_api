from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer,ProductSerializer,CreateProductSerializer, UserCreateSerializer
from rest_framework import status, exceptions, permissions
from django.contrib.auth. models import User
from .models import Category, Product
from rest_framework import generics
# Create your views here.

# class CategoryEndPoint(APIView):
#     def get(self, request, *args, **kwargs):
#         category=Category.objects.all()
#         serializer=CategorySerializer(category, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

#     def post(self, request, *args, **kwargs):
#         serializer=CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()    #calls the create or update method depend on the request made.
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UpgradedCategoryEndpoint(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class SingleCategoryEndpoint(generics.RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='pk'


class CategoryDeleteEndpoint(generics.DestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='pk'



class UpgradedProductEndpoint(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #permission_classes=(permissions.IsAuthenticated)



# class ProductEndpoint(APIView):
#     def get(self, request, *args, **kwargs):
#         products=Product.objects.all()
#         serializer=ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
       
class ProductListEndpoint(generics.ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

    def get_queryset(self):
        queryset=super().get_queryset()
        category=self.request.query_params.get('category')
        if category is not None:
            queryset=queryset.filter(category__name=category)
        return queryset
    


class ProductDetailEndpoint(APIView):
        def get_object(self, pk):
            try:
                product=Product.objects.get(id=pk)
                return product
            except Product.DoesNotExist:
                raise exceptions.NotFound(f'product with this id: {pk} does not exist')

        def get(self, request, *args, **kwargs):
            product=self.get_object(self.kwargs['product_id'])
            serializer=ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        def put(self, request, *args, **kwargs):
            product=self.get_object(self.kwargs['product_id'])
            serializer=CreateProductSerializer(instance=product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


        def delete(self, request, *args, **kwargs):
            product=self.get_object(self.kwargs['product_id'])
            product.delete()
            return Response({'message':'product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        


# class UserRegisterviewEndpoint(generics.CreateAPIView):
#     queryset=User.objects.all()
#     permission_classes=[permissions.AllowAny]
#     serializer_class=UserCreateSerializer

#     def login(self, request, *args, **kwargs):
#         queryset=User.objects.all()
#         permission_classes=[permissions.AllowAny]
#         # serializer_class=UserloginSerializer