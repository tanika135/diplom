from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class ReportCreateForm(forms.Form):
    # interval = forms.TypedChoiceField(choices=INTERVAL_CHOICES, coerce=int)
    date_report_from = forms.DateField(label='Enter Date', widget=DateInput, required=True)
    date_report_to = forms.DateField(label='Enter Date', widget=DateInput, required=True)
