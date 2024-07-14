from django import forms
from django.forms import ModelForm
from .models import Tournament, MyApply

class MyApplyForm(ModelForm):
    """
    def __init__(self, MyApplyForm, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tournament_name"].queryset = Tournament.objects.filter(finished=False)
    """
    class Meta:
        model = MyApply
        fields = ('FullName', 'PubgName', 'PubgID','tgusername', 'tournament_name')
        labels = {
            'FullName' : 'Full Name',
            'PubgName' : 'Pubg Name',
            'PubgID' : 'Pubg ID',
            'tgusername' : 'Tg Username',
            'tournament_name' : 'Choose tournament'
        }
        widgets = {
            'FullName':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Full Name'}),
            'PubgName':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Pubg Name'}),
            'PubgID':forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Pubg ID'}),
            'tgusername' : forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Telegram username'}),
            'tournament_name': forms.Select(attrs={'class':'form-control my-1', 'placeholder':'Tournament Name'}),
        }