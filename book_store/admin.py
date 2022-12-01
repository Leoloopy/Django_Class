from django.contrib import admin


class BookStoreAdminSite(admin.AdminSite):
    site_header = "Book store site"
    site_title = 'Book Store'
    index_title = 'Book store Admin Interface'
    logout_template = 'my_logout.html'
