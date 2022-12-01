from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import Publisher
from .serializers import BookSerializers, PublisherSerializer
from .models import Book
from .filters import BookFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# class BookList(ListCreateAPIView):
#     queryset = Book.objects.select_related('publisher').all()
#     serializer_class = BookSerializers

# def get_serializer_context(self):
#     return {"return": self.request}
#
# def get_queryset(self):
#     pass


# class BookList(APIView):
#     def get(self, request):
#         queryset = Book.objects.select_related('publisher').all()
#         serializer = BookSerializers(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         queryset = Book.objects.select_related('publisher').all()
#         serializer = BookSerializers(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BookSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class Book_Detail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers


# class Publisher_List(ListCreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer


# class Publisher_Details(RetrieveUpdateDestroyAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#         serializer = BookSerializers(book, context={"request": request})
#         return Response(serializer.data)
#     elif request.method in ('PUT', 'PATCH'):
#         serializer = BookSerializers(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     if request.method == 'GET':
#         queryset = Publisher.objects.annotate(
#             numbers_of_books_publsihed=Count('books')
#         ).all()
#         serializer = PublisherSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()


# @api_view(['GET', 'PATCH', 'DELETE'])
# def publisher_details(request, pk):
#     publisher = Publisher.objects.annotate(
#         numbers_of_books_publsihed=Count('books')
#     ).all()
#     if request.method == 'GET':
#         serializer = PublisherSerializer(publisher)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = PublisherSerializer(publisher, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view()
# def publisher_list(request):
#     queryset = Publisher.objects.all()
#     serializer = PublisherSerializers(queryset, many=True, context={'request': request})
#     return Response(serializer.data)
#
#
# @api_view()
# def publisher_details(request, id):
#     publisher = get_object_or_404(Publisher, pk=id)
#     serializer = PublisherSerializer(publisher)
#     return Response(serializer.data)


# finally
class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('publisher').all()
    serializer_class = BookSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title']
    ordering_fields = ['title']


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.annotate(
        number_of_books_published=Count('books')
    ).all()
    serializer_class = PublisherSerializer
    filter_backends = [DjangoFilterBackend]

