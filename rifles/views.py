from django.shortcuts import render, get_object_or_404
from .models import Rifle

def rifle_list(request):
    rifles = Rifle.objects.all()
    return render(request, "rifles/list.html", {"rifles": rifles})

def rifle_detail(request, id):
    rifle = get_object_or_404(Rifle, id=id)
    return render(request, "rifles/detail.html", {"rifle": rifle})

def compare(request):
    ids = request.GET.getlist("ids")
    rifles = Rifle.objects.filter(id__in=ids)
    return render(request, "rifles/compare.html", {"rifles": rifles})