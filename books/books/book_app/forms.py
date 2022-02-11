from django import forms
from django.core.exceptions import ValidationError

from books.book_app.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    bot_catcher = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if len(value) > 0:
            raise ValidationError('You are a bot')
        return value

    def clean(self):
        if self.cleaned_data['pages'] <= 0:
            raise ValidationError('Pages cannot be 0 or negative!')
