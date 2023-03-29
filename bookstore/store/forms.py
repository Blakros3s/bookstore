from django import forms
from .models import Book, Category

class BookAddForm(forms.ModelForm):
    class Meta:
        # fields = "__all__" #for all fields
        fields = ("title", "author", "description", "price", "category", "quantity")
        model = Book

class CategoryAddForm(forms.ModelForm):
    class Meta:
        fields = ("category_name",)
        model = Category