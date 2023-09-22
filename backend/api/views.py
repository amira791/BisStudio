from django.shortcuts import render
import json 
from .models import Etudiant, Cours , Payment
from django.http import JsonResponse
from .forms import EtudiantRegistrationForm
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime 

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
from django.views.decorators.csrf import csrf_exempt
from .models import Cours

@csrf_exempt
def get_course(request, id_cours):
    if request.method == 'GET':
        try:
            # Query the database to get the course with the specified id_cours
            cours = Cours.objects.get(id=id_cours)  # Use get() instead of filter()

            # Serialize the data into JSON format
            cours_data = {
                'id': cours.id,  
                'titre': cours.titre,
                'description': cours.description,
                'matiere': cours.matiere.nom,
                'prix': float(cours.prix),
                'nbheures': float(cours.nbheures),
                'nbvieux': float(cours.nbvieux),
                'enseignant': f"{cours.enseignant.nomEnsei} {cours.enseignant.prenomEnsei}",
            }

            # Return a JSON response with the serialized data
            return JsonResponse(cours_data)
        except Cours.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
        except Exception as e:
            # Handle any exceptions that may occur during data retrieval
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


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
                    'enseignant': f"{cour.enseignant.nomEnsei} {cour.enseignant.prenomEnsei}" # Concatenate nomEnsei and prenomEnsei
                }
                for cour in cours
            ]

            # Return a JSON response with the serialized data
            return JsonResponse(cours_data, safe=False)
        except Exception as e:
            # Handle any exceptions that may occur during data retrieval
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)






@csrf_exempt
def make_payment(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))

            # Extract payment data
            etudiant_id = data.get('etudiant_id')
            cours_id = data.get('cours_id')
            montant = data.get('montant')

            # Get the current date and time
            current_datetime = datetime.now()

            # Create a Payment instance with the current date and time and save it to the database
            payment = Payment(
                etudiant_id=etudiant_id,
                cours_id=cours_id,
                montant=montant,
                date_paiement=current_datetime  # Set the date_paiement field to the current date and time
            )
            payment.save()

            # Return a JSON response indicating success
            response_data = {'message': 'Payment successful', 'payment_id': payment.id}
            return JsonResponse(response_data)
        except Exception as e:
            # Handle any exceptions that may occur during payment processing
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
