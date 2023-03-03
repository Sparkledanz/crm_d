from django.forms import ModelForm
from .models import Employee,Employer,Partner,Settlement,Document,Travel
from django import forms
from django import forms
from .models import Message, Partner

class PartnerMessageForm(forms.ModelForm):
    partner_name = forms.ModelChoiceField(queryset=Partner.objects.all(), empty_label=None)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Message
        fields = ['partner_name', 'message']


"""class AdminMessageForm(forms.Form):
    partner = forms.ModelChoiceField(queryset=Partner.objects.all())
    message = forms.CharField(widget=forms.Textarea)
"""

class ReplyForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'field1': 'Label for Field 1',
            'field2': 'Label for Field 2',
            # ...
        }
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control'}),
            'field2': forms.TextInput(attrs={'class': 'form-control'}),
            # ...
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''



class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        labels = {
            'field1': 'Label for Field 1',
            'field2': 'Label for Field 2',
            # ...
        }
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control'}),
            'field2': forms.TextInput(attrs={'class': 'form-control'}),
            # ...
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
        labels = {
            'field1': 'Label for Field 1',
            'field2': 'Label for Field 2',
            # ...
        }
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control'}),
            'field2': forms.TextInput(attrs={'class': 'form-control'}),
            # ...
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''


class SettlementForm(forms.ModelForm):
    class Meta:
        model = Settlement
        fields = '__all__'
        labels = {
            'field1': 'Label for Field 1',
            'field2': 'Label for Field 2',
            # ...
        }
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control'}),
            'field2': forms.TextInput(attrs={'class': 'form-control'}),
            # ...
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        labels = {
            'field1': 'Label for Field 1',
            'field2': 'Label for Field 2',
            # ...
        }
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control'}),
            'field2': forms.TextInput(attrs={'class': 'form-control'}),
            # ...
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'
        labels = {
            'field1': 'Label for Field 1',
            'field2': 'Label for Field 2',
            # ...
        }
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control'}),
            'field2': forms.TextInput(attrs={'class': 'form-control'}),
            # ...
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
