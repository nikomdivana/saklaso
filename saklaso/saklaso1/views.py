from django.shortcuts import render, redirect, get_object_or_404
from .models import City
from .forms import CityForm

def home(request):
    city = City.objects.all()
    return render(request,'home.html',context ={'cities': city})

def create_city(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'create_city.html',
                  context={'form': CityForm()})
def update_city(request, pk):
    city = City.objects.get(id=pk)
    if request.method == "POST":
        form = CityForm(request.POST,instance=city)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render (request, 'update_city.html',
                   context={'form': CityForm(instance=city)})
def delete_city(request, pk):
    city = get_object_or_404(city, pk=pk)
    city.delete()
    return redirect('home')