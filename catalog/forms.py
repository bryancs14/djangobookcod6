from django.forms import fields
from catalog.models import Author, Book
from django import forms
from django.forms.models import ModelForm

class BookForm(forms.Form):
    title = forms.CharField(label="Title")
    autor = forms.ModelChoiceField(queryset=Author.objects.all(), label="Author")
    editorial = forms.CharField(label="Editorial")
    year = forms.IntegerField(label="Year")
    volume = forms.IntegerField(label="Volume")


class ModelBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','editorial', 'year', 'volume']

