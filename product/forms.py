from django import forms
import urllib3 
from django.core.exceptions import ValidationError

class addProductForm(forms.Form):
    product_price = forms.IntegerField(max_value=10000 , min_value=10 )
    product_name = forms.CharField(max_length=100 , min_length=1 , strip=False) 
    product_url = forms.URLField()

    def clean_product_url(self):
        data = self.cleaned_data['product_url']
        httpRequest = urllib3.PoolManager()
        res = httpRequest.request(method="GET" , url=data )
        if res.status == 200:
            if len(res.data) :
                return data
            else:
                raise ValidationError(message="The URL sent no response")
        else:
            raise ValidationError(message="Unable to establish connection")
