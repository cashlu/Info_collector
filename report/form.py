from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        # fields = ('name', 'identity', 'decade', 'address', 'purpose', 'comment',
        #           'structure', 'security', 'groundsill', 'tilt', 'upon',
        #           'fence', 'assess_level',
        #           'advice', 'street_contract', 'street_contract_phone',
        #           'village_contract',
        #           'village_contract_phone', 'reviewer', 'appraiser',
        #           'creator', 'security_detail', 'groundsill_detail',
        #           'tilt_detail', 'upon_detail', 'fence_detail')
        fields = '__all__'
