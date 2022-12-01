from django.contrib.admin.apps import AdminConfig


class BookStoreAdminConfig(AdminConfig):
    default_site = "book_store.admin.BookStoreAdminSite"
