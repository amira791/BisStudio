

# Create your models here.
from django.db import models

# Create your models here.
#    filiere = (
#       ('Science', 'Science'),
#       ('Math', 'Math'),
#       ('Litterature', 'Litterature'),
#       ('Genie Civil', 'Suppression lieu'),
#       ('Genie Electrique', 'Genie Electrique'),
#       ('Genie des procedes ', 'Genie des procedes'),
#       ('Langues', 'Langues'),
#       ('Economie', 'Economie'),
#         )


 #  is_authenticated = models.BooleanField(default=False)

class Etudiant(models.Model):
   idEtud = models.AutoField(primary_key=True)
   nomEtud = models.CharField(max_length=100)
   prenomEtud = models.CharField(max_length=100)
   username = models.CharField(max_length=100)
   motdepasse = models.CharField(max_length=100)
   Filiere = models.CharField(max_length=100)
   Wilaya = models.CharField(max_length=100)
   favoris = models.ManyToManyField('Cours', through='Favori', related_name='etudiants_favoris')
   cours_completes = models.ManyToManyField('Cours', related_name='etudiants_completes', blank=True)


   def __str__(self) -> str:
        return (self.username)

class Enseignant (models.Model):
   idEnsei = models.AutoField(primary_key=True)
   nomEnsei = models.CharField(max_length=100)
   prenomEnsei = models.CharField(max_length=100)
   email = models.EmailField(unique=True)


   def __str__(self) -> str:
        return f"{self.nomEnsei} {self.prenomEnsei}"



class Matiere(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    enseignant= models.ForeignKey(Enseignant, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Cours(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    nbheures = models.DecimalField(max_digits=10, decimal_places=2)
    nbvieux = models.DecimalField(max_digits=10, decimal_places=2)
    enseignant = models.OneToOneField(Enseignant, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.titre

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours_id = models.ForeignKey(Cours, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Payment for {self.cours} by {self.etudiant}"

class Commentaire(models.Model):
    idCom = models.AutoField(primary_key=True)
    cours_id = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='commentaires')
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    texte = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.cours} by {self.etudiant}"

class Favori(models.Model):
    idFav = models.AutoField(primary_key=True)
    etudiant_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours_id = models.ForeignKey(Cours, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.etudiant} favorited {self.cours}"