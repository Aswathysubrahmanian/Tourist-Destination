from django.shortcuts import render,redirect
from rest_framework import generics,status
from rest_framework.permissions import AllowAny
from .models import Destinations
from .serializers import DestinationSerializer
from rest_framework.response import Response
from .forms import DestinationForms
import requests

class DestinationListView(generics.ListCreateAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestinationSerializer

def createDestination(request):
    api_url='http://127.0.0.1:8000/create/'
    if request.method=="POST":
        form=DestinationForms(request.POST,request.FILES)
        if form.is_valid():
            data = {
                    'name': form.cleaned_data['name'],
                    'description': form.cleaned_data['description'],
                    'palce': form.cleaned_data['place'],
                    'weather': form.cleaned_data['weather'],
                    'district': form.cleaned_data['district'],
                    'state': form.cleaned_data['state'],
                    'map_link': form.cleaned_data['map_link'],
                    'image': form.cleaned_data['image'],
                }
            form.save()
        image = request.FILES['image']
        files = {'images': (image.name, image.file, image.content_type)}

        response = requests.post(api_url,  files=files, data=data)
        print(response.status_code)
        if response.status_code == 400:  # Assuming 201 indicates a successful creation

            return redirect('listview')
        else:
            return render(request, 'create.html', {'error': 'API request failed'}, status=500)
    else:
          
        form = DestinationForms()
        return render(request, 'create.html', {'form': form})


def Home_page(request):
    destination=Destinations.objects.all()
    return render(request,'home.html',{'destination':destination})


class DestinationDetailView(generics.RetrieveAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestinationSerializer


def Detail_view(request,dest_id):
    api_url=f'http://127.0.0.1:8000/details/{dest_id}'
    response = requests.get(api_url)
    if response.status_code == 200:
        api_data = response.json()
        return render(request,'details.html',{"api_data":api_data})


class DestinationUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestinationSerializer

def Update_view(request, dest_id):
    api_url = f'http://127.0.0.1:8000/update/{dest_id}/'


        # Retrieve the existing recipe data
    response = requests.get(api_url)
    existing_recipe_data = response.json()

    if request.method == 'POST':
        form = DestinationForms(request.POST, request.FILES)
        if form.is_valid():
            multipart_form_data = {}
            for key, value in form.cleaned_data.items():
                multipart_form_data[key] = value

            image = request.FILES['image']
            multipart_form_data['image'] = (image.name, image, image.content_type)

               
            response = requests.put(api_url, data=multipart_form_data, files={'image': multipart_form_data['image']})

            if response.status_code == 200:
                    return redirect('listview')
            else:
                    return render(request, 'update.html', {'error': 'API request failed'}, status=500)
    else:
            # Pre-fill the form with the existing data
        form = DestinationForms(initial=existing_recipe_data)


    return render(request, 'update.html', {'form': form})

class DestinationDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestinationSerializer

def delete_view(request,dest_id):
    if request.method == 'POST':
        api_url=f'http://127.0.0.1:8000/delete/{dest_id}/'
        print(api_url)
        response = requests.delete(api_url)
        print(response)
        if response.status_code == 204:
            return redirect("listview")
    return render(request,'delete.html')
      

