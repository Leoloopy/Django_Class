from django.urls import path, include
from .models import Book
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

# urlpatterns = [
#     path('', views.index, name='index'),
#     path("<int:pk>/", views.publisher_details, name="publisher-details"),
#     path("book-index/", views.book_index, name="book-index"),
#     path("book-create/", views.book_create, name="book-create"),
#     path("<slug:slug>/", views.book_details, name="book-details"),
#
# ]


router = DefaultRouter()
router.register('books', viewset=views.BookViewSet, basename='book')
router.register('publishers', viewset=views.PublisherViewSet, basename="publisher")

# this or down
# urlpatterns = [
#     #     path("books/", views.BookList.as_view(), name="book-list"),
#     #     path("books/<int:pk>/", views.Book_Detail.as_view(), name="book-details"),
#     #     path("publishers/", views.Publisher_List.as_view(), name="publisher-list"),
#     #     path("publishers/<int:id>/", views.Publisher_Details.as_view(), name="publisher-details")
#     path('', include(router.urls)),
# ]

urlpatterns = router.urls
