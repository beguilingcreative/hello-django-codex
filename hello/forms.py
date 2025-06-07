from django import forms


class MessageForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)


class FactorialForm(forms.Form):
    number = forms.IntegerField(
        min_value=0,
        max_value=12,
        help_text="Enter a number between 0 and 12",
    )
