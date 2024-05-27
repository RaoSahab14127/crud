from django.shortcuts import get_object_or_404, render,redirect
from .models import Actors
from django.views.generic import View
from django.views.generic.edit import DeleteView

class ActorsList(View):


    def get(self, request, *args, **kwargs): 
        products = Actors.objects.all()
        context  = {'carls':products}
        return render(request, 'crudapi/home.html', context)
    def post(self, request, *args, **kwargs):
        s = Actors()
        s.fullname = request.POST.get('fullname')
        s.dob = request.POST.get('dob')
        s.nationality = request.POST.get('nationality')
        s.save()
        return redirect("/api/")
class ActorsDetail(View):
    def get(self, request,actor_id):
        actor = Actors.objects.filter(pk = actor_id).values()
        return render(request, 'crudapi/Detail.html',{'cars': actor })

class DeleteView(DeleteView):
    model = Actors
    success_url ="/api/"

class Update(View):
    def get(self, request,actor_id):
        return render(request, 'crudapi/update.html',{'cars': actor_id })
    def post(self, request, actor_id):
        actor = get_object_or_404(Actors, pk=actor_id)
        actor.fullname = request.POST.get('fullname')
        actor.dob = request.POST.get('dob')
        actor.nationality = request.POST.get('nationality')
        actor.save() 

        return redirect("/api/")