from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput

class FrontendModelForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(FrontendModelForm,self).__init__(*args,**kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if type(visible.field) is forms.fields.DateField:
                visible.field.widget = DatePickerInput(format="'%Y-%m-%d'")
                visible.field.widget.attrs['class'] = 'form-control datepicker'




class AllowedIPCreateForm(FrontendModelForm):
    class Meta:
        model = AllowedIP
        exclude = ('created','modified','deleted')
        widgets = {
            'description': forms.Textarea(attrs={'rows':4})
        }


class BlockedIPCreateForm(FrontendModelForm):
    class Meta:
        model = BlockedIP
        exclude = ('created','modified','deleted')
        widgets = {
            'description': forms.Textarea(attrs={'rows':4})
        }


