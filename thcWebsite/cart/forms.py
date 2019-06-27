from django import forms

limit= 21
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, limit)]

class CartAddProductForm(forms.Form):

    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int) #converts to an int

    #backend Boolean field to let us know if we need to update the cart.
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
