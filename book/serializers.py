from _pydecimal import Decimal

from rest_framework import serializers
from .models import Publisher, Book


# class PublisherSerializers(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     email = serializers.EmailField()
#     website = serializers.URLField()
#
#
# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     isbn = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     # publisher = serializers.StringRelatedField()
#     publisher = serializers.HyperlinkedRelatedField(
#         queryset=Publisher.objects.all(),
#         view_name="publisher-details"
#     )

class BookSerializers(serializers.ModelSerializer):
    # publisher = serializers.HyperlinkedRelatedField(queryset=Publisher.objects.all(), view_name="publisher-details")

    # discounted_price = serializers.SerializerMethodField(method_name='discount', read_only=True)
    #
    # def discount(self, book):
    #     return book.price * Decimal(8)

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'genre', 'price', 'date_published', 'edition', 'publisher']


class PublisherSerializer(serializers.ModelSerializer):
    number_of_books_published = serializers.IntegerField(read_only=True)

    class Meta:
        model = Publisher
        fields = ['id', 'name', 'email', 'website', 'number_of_books_published']
