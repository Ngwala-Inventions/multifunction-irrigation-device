from django import forms
from .models import *


class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = [
            'farm_id','location','owner'
        ]

class IrrigationForm(forms.ModelForm):
    class Meta:
        model = Irrigation
        fields = [
            'farm','volume_used'
        ]

class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = [
            'farm','type','quantity'
        ]

class PestControlForm(forms.ModelForm):
    class Meta:
        model = PestControl
        fields = [
            'farm','type','quantity'
        ]

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = [
            'user','message'
        ]