from django import forms
from django.contrib.auth.models import User
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'email', 'password']
        widgets = {
            'password' : forms.PasswordInput()
        }


class depForm(forms.ModelForm):
    class Meta:
        model = models.Dep
        fields = '__all__'

class entreForm(forms.ModelForm):
    class Meta:
        model = models.Entre
        fields = '__all__'



class etudForm(forms.ModelForm):
    class Meta:
        model = models.Etud
        fields = '__all__'        



class Type_EncadrantForm(forms.ModelForm):
    class Meta:
        model = models.Type_Encadrant
        fields = '__all__'   




class simesterForm(forms.ModelForm):
    class Meta:
        model = models.Simester
        fields = '__all__'   

        

class Type_stageForm(forms.ModelForm):
    class Meta:
        model = models.Type_stage
        fields = '__all__'  



class encadrantForm(forms.ModelForm):
    class Meta:
        model = models.Encadrent
        fields = '__all__'  


 


class grpForm(forms.ModelForm):
    class Meta:
        model = models.grp
        fields = ['idSimester', 'idEtud', 'libele', 'membres']

        widgets = {
           'membres': forms.TextInput(attrs={'id': 'membres-input'}),
        }
