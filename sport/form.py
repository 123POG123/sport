from django.forms import ModelForm
from .models import MyForm


# Create your models here.
class FormMyForm(ModelForm):
    class Meta:
        model = MyForm
        fields = '__all__'
