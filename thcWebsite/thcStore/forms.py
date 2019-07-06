from .models import Product
from django.forms import ModelForm

class ProductCreateForm(ModelForm):
    class Meta:
        fields = ( "name", "image",  "description", "price")

        model = Product

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
