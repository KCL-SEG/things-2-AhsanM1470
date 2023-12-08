from django import forms

"""Forms of the project."""
class ThingForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(widget=forms.NumberInput)
