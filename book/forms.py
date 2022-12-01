from django import forms

from book.models import Book


class BookForm(forms.ModelForm):
    # title = forms.CharField(max_length=225, required=False, label="My title")
    # isbn = forms.CharField(max_length=225)
    # price = forms.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Book
        fields = "__all__"
        # exclude = ['authors', 'slug']

