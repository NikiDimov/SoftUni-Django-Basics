import os

from django import forms

from expenses_tracker.expenses_app.models import Profile, Expense


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'profile_image': 'Profile Image'}
        # widgets = {
        #     'profile_image': forms.ClearableFileInput({'attrs': {'class': 'form-file'}})
        # }


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = ('title', 'description', 'expense_image', 'price')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'profile_image': 'Profile Image'}


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.profile_image.path
        self.instance.delete()
        Expense.objects.all().delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()
