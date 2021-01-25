from django import forms
from .models import Game, Note

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["title", "platforms"]
