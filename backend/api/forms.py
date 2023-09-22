from django import forms
from .models import Etudiant

class EtudiantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nomEtud', 'prenomEtud', 'username', 'motdepasse', 'Filiere', 'Wilaya']