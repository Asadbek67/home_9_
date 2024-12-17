from django.shortcuts import render, get_object_or_404
from .models import Types, Flower


def index(request):
    flowers = Flower.objects.all()
    return render(request, 'index.html', {'flowers': flowers})


def type_detail(request, types_id):
    type_fw = get_object_or_404(Types, id=types_id)
    flowers = type_fw.flower.all()

    return render(request, 'types_detail.html', {'type_fw': type_fw, 'flowers': flowers})


def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flower_detail.html', {'flower': flower})


