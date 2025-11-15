from django import forms

class HistogramForm(forms.Form):
    energy_from = forms.FloatField(label='Energy from', required=False)
    energy_to = forms.FloatField(label='Energy to', required=False)

    height_from = forms.IntegerField(label='Height from', required=False)
    height_to = forms.IntegerField(label='Height to', required=False)

    phip_from = forms.FloatField(label='Phip from', required=False)
    phip_to = forms.FloatField(label='Phip to', required=False)

    theta_from = forms.FloatField(label='Theta from', required=False)
    theta_to = forms.FloatField(label='Theta to', required=False)

    thetap_from = forms.FloatField(label='Thetap from', required=False)
    thetap_to = forms.FloatField(label='Thetap to', required=False)

    COLNAME_CHOICES = [
        ('energy', 'energy'),
        ('height', 'height'),
        ('phip', 'phip'),
        ('theta', 'theta'),
        ('thetap', 'thetap'),
    ]
    colname = forms.ChoiceField(choices=COLNAME_CHOICES, initial='height', label='Column')
