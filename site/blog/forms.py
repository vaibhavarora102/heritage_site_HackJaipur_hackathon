from django.forms import ModelForm
from .models import Take_Img

# Create the form class.
class ImageForm(ModelForm):
    class Meta:
        model = Take_Img
        fields = ['image']