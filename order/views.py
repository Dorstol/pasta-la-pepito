from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from order.models import CartOrder
from order.serializers import CartOrderSerializer


class OrderViewSet(ViewSet):
    def get_queryset(self):
        return CartOrder.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CartOrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        order = get_object_or_404(queryset, pk=pk)
        serializer = CartOrderSerializer(order)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CartOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
