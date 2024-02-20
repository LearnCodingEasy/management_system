from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # All Form In Model Book
        # fields = '__all__'
        # Get Single Input In Sild Form
        fields = [
            "title",
            "author",
            "book_photo",
            "author_photo",
            "pages",
            "price",
            "ratal_price_day",
            "ratal_period",
            "status",
            "category",
        ]
        widgets = {
          "title": forms.TextInput(attrs={'class':'form-control'}),
            "author": forms.TextInput(attrs={'class':'form-control'}),
            "book_photo": forms.FileInput(attrs={'class':'form-control'}),
            "author_photo": forms.FileInput(attrs={'class':'form-control'}),
            "pages": forms.NumberInput(attrs={'class':'form-control'}),
            "price": forms.NumberInput(attrs={'class':'form-control'}),
            "ratal_price_day": forms.NumberInput(attrs={'class':'form-control'}),
            "ratal_period": forms.NumberInput(attrs={'class':'form-control'}),
            "status": forms.Select(attrs={'class':'form-control'}),
            "category": forms.Select(attrs={'class':'form-control'}),
        }



# 
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # All Form In Model Book
        # fields = '__all__'
        # Get Single Input In Sild Form
        fields = [
            "name",
        ]
        # Add Attribute To Element 
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control'}),
        }