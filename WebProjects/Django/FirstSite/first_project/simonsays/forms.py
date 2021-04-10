from django import forms

class PlayerLogin(forms.Form):
    name = forms.CharField(max_length=150, label="Player name")
