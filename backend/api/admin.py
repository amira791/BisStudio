from django.contrib import admin
from .models import Etudiant, Enseignant, Matiere, Cours, Payment, Commentaire, Favori

# Register your models here.
class EtudiantAdmin(admin.ModelAdmin):
    list = ('idEtud', 'nomEtud', 'prenomEtud', 'username', ' motdepasset', 'Filiere', 'Wilaya', 'favoris','cours_completes')

    admin.site.register(Etudiant)

class EnseignantAdmin(admin.ModelAdmin):
    list = ('idEnsei', 'nomEnsei', 'prenomEnsei', 'email')

    admin.site.register(Enseignant)

class MatiereAdmin(admin.ModelAdmin):
    list = ('idM', 'nom', 'enseignant')

    admin.site.register(Matiere)

class CoursAdmin(admin.ModelAdmin):
    list = ('idC', 'titre', 'nomEnsei', 'description', 'prix', 'nbheures', 'nbvieux', 'matiere', 'enseignan' )

    admin.site.register(Cours)

class PaymentAdmin(admin.ModelAdmin):
    list = ('idP', 'etudiant', 'cours', ' montant', 'date_paiement')

    admin.site.register(Payment)

class CommentaireAdmin(admin.ModelAdmin):
    list = ('idCom', 'cours', 'etudiant', ' texte', 'date_commentaire')

    admin.site.register(Commentaire)

class FavoriAdmin(admin.ModelAdmin):
    list = ('idFav', 'etudiant', 'cours')

    admin.site.register(Favori)

# admin.site.register(Enseignant)
# admin.site.register(Matiere)
# admin.site.register(Cours)
# admin.site.register(Payment)
# admin.site.register(Commentaire)
# admin.site.register(Favori)