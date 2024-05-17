from django.shortcuts import render,redirect
from .models import Cars
from django.http import HttpResponse
def getAllCars(request):
    carlist = Cars.objects.all()
    return render(request, 'crudapi/home.html', {'carls' : carlist})
def addcar(request):
    if request.method == "POST":
        print("Added")
        s = Cars()
        s.modelname = request.POST.get('modelname')
        s.colour = request.POST.get('colour')
        s.year = request.POST.get('year')
        s.engine = request.POST.get('engine')
        s.save()
        return redirect("/api/home")

    return render(request, 'crudapi/addcar.html')

def detailcar( request, car_id):
    car = Cars.objects.filter(pk = car_id)
    print(car.modelname)
    return render(request, 'crudapi/Detail.html',{'car': car })