from django.shortcuts import render
import json 
from .models import Etudiant, Cours
from django.http import JsonResponse
from .forms import EtudiantRegistrationForm
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def register_etudiant(request):
#     if request.method == 'POST':
#         form = EtudiantRegistrationForm(request.POST)
#         if form.is_valid():
#             etudiant = form.save()
#             response_data = {'message': 'Registration successful', 'idEtud': etudiant.idEtud}
#             return JsonResponse(response_data)
#         else:
#             errors = form.errors.as_json()
#             return JsonResponse({'errors': errors}, status=400)
#     else:
#         form = EtudiantRegistrationForm()
#     return render(request, 'registration_form.html', {'form': form})


@csrf_exempt
def register_etudiant(request):
    if request.method == 'POST':
        try:
   
            data = json.loads(request.body.decode('utf-8'))

            nom = data.get('nomEtud')
            prenom = data.get('prenomEtud')
            username = data.get('username')
            motdepasse = data.get('motdepasse')
            Filiere = data.get('Filiere')
            Wilaya = data.get('Wilaya')

            
            etudiant = Etudiant(
                nomEtud=nom,
                prenomEtud=prenom,
                username=username,
                motdepasse=motdepasse,
                Filiere=Filiere,
                Wilaya=Wilaya
            )
            etudiant.save()

            response_data = {'message': 'Registration successful', 'idEtud': etudiant.idEtud}
            return JsonResponse(response_data)
        except Exception as e:
            # Handle any exceptions that may occur during registration
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)




@csrf_exempt
def get_all_etudiants(request):
    if request.method == 'GET':
        try:
            # Query the database to get all Etudiant instances
            etudiants = Etudiant.objects.all()

            # Serialize the data into JSON format
            etudiants_data = [
                {
                    'idEtud': etudiant.idEtud,
                    'nom': etudiant.nomEtud,
                    'prenom': etudiant.prenomEtud,
                    'username': etudiant.username,
                    'Filiere': etudiant.Filiere,
                    'Wilaya': etudiant.Wilaya,
                }
                for etudiant in etudiants
            ]

            # Return a JSON response with the serialized data
            return JsonResponse(etudiants_data, safe=False)
        except Exception as e:
            # Handle any exceptions that may occur during data retrieval
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


from django.http import JsonResponse
from .models import Cours
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_all_cours(request):
    if request.method == 'GET':
        try:
            # Query the database to get all Cours instances
            cours = Cours.objects.all()

            # Serialize the data into JSON format
            cours_data = [
                {
                    'id': cour.id,
                    'titre': cour.titre,
                    'description': cour.description,
                    'matiere': cour.matiere.nom,  
                    'prix': float(cour.prix), 
                    'nbheures': float(cour.nbheures), 
                    'nbvieux': float(cour.nbvieux),  
                    'enseignant': f"{cour.enseignant.nomEnsei} {cour.enseignant.prenomEnsei}",  # Concatenate nomEnsei and prenomEnsei
                }
                for cour in cours
            ]

            # Return a JSON response with the serialized data
            return JsonResponse(cours_data, safe=False)
        except Exception as e:
            # Handle any exceptions that may occur during data retrieval
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
