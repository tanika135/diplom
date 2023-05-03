# from django.http import JsonResponse
# from app_goods.entities import Item
# from app_goods.serializers import ItemSerializer
#
#
# def items_list(request):
#     if request.method == 'GET':
#         items_for_sale = [
#             Item(
#                 name='Кофеварка',
#                 description='Варит отличный кофе',
#                 weight=100
#             ),
#             Item(
#                 name='Беспроводные наушники',
#                 description='Отличный звук',
#                 weight=100
#             ),
#         ]
#         return JsonResponse(ItemSerializer(items_for_sale, many=True).data, safe=False)
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from app_goods.models import Item
from app_goods.serializers import ItemSerializer
from rest_framework.generics import GenericAPIView


class ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка товаров и создания нового товара."""
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class ItemDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о товаре,
    а также для его редактирования и удаления"""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def get(self, request):
    #     items = Item.objects.all()
    #     serializer = ItemSerializer(items, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = ItemSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)