from django import forms
from django.core.exceptions import ValidationError
from django.forms import models
from item.models import Item

class InputForm(forms.Form):
    param1 = forms.CharField()

class SampleForm(forms.Form):
    p1 = forms.CharField()
    p2 = forms.CharField(widget=forms.Textarea)
    p3 = forms.MultipleChoiceField(choices=(('1', '赤'), ('2', '黄色'),('3', '青')),
                                   widget=forms.CheckboxSelectMultiple)
    p4 = forms.ChoiceField(choices=(('1', '赤'), ('2', '黄色'),('3', '青')),
                           widget=forms.RadioSelect)
    p5 = forms.ChoiceField(choices=(('1', '赤'), ('2', '黄色'),('3', '青')),
                           widget=forms.Select)
    p6 = forms.FileField()

class InputForm2(forms.Form):
    param1 = forms.IntegerField()

    def clean_param1(self):
        param1 = self.cleaned_data['param1']
        if not (0 < param1 < 10):
            raise ValidationError('範囲エラー')
        return param1

class InputForm3(forms.Form):
    param1 = forms.IntegerField(
            max_value=10,
            error_messages={
                    'required': '必須入力です',
                    'max_value': '最大値を超えています'})

class InputFormValid(forms.Form):
    param1 = forms.IntegerField(max_value=10)
    param2 = forms.CharField(required=False)
    
class ItemForm(models.ModelForm):
    name = forms.CharField(label='名前')
    price = forms.IntegerField(label='価格')
    class Meta:
        model = Item
        fields = ('name', 'price')