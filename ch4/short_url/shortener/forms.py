from django import forms

from shortener.models import ShortURL

class ShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ["original_url"]
        labes = {
            "original_url": "Redirect URL",
        }
