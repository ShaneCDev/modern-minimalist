from django import forms
from .models import Product, Category
from .widgets import CustomClearableFileInput
from django.utils.text import slugify

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     cleaned_name = cleaned_data.get('name')
    #     if cleaned_name:
    #         cleaned_data['slug'] = slugify(cleaned_name)
    #     return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-light rounded-0'
