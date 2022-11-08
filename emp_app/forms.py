from django.forms import ModelForm
from .models import customer1
from django.forms import TextInput, Select, NumberInput



class customerform1(ModelForm):
    class Meta:
            
                model=customer1
                fields=['username','password']
                widgets={
                    'username':TextInput(attrs={'class':'form-control','placeholder':'Enter username' }),
                    
                    
                    'password':TextInput(attrs={'class':'form-control','placeholder':'Enter password'}),
                }
