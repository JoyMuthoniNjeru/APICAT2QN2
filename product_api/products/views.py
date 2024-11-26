from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self, request):
        # Retrieve all products from the database
        products = Product.objects.all()

        # Serialize the data
        serializer = ProductSerializer(products, many=True)

        # Return the serialized data as JSON
        return Response(serializer.data)

    def post(self, request):
        # Deserialize the incoming data
        serializer = ProductSerializer(data=request.data)

        # Check if the data is valid
        if serializer.is_valid():
            # If valid, save the product to the database
            serializer.save()

            # Respond with the serialized data and 201 Created status code
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # If the data is invalid, return errors and 400 Bad Request status code
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
