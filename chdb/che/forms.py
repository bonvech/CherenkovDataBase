from django import forms

class HistogramForm(forms.Form):
    height_from = forms.IntegerField(label='Height from', required=False)
    height_to = forms.IntegerField(label='Height to', required=False)

    COLNAME_CHOICES = [
        ('energy', 'energy'),
        ('height', 'height'),
        ('phip', 'phip'),
        ('theta', 'theta'),
        ('thetap', 'thetap'),
    ]
    colname = forms.ChoiceField(choices=COLNAME_CHOICES, initial='height', label='Column')
