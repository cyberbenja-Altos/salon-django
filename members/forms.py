from django import forms
from members.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname','lastname','eventDay','phone',)
        widgets = {
            'eventDay': forms.DateInput(attrs={'type': 'date'}),
        }