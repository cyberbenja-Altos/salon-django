from gc import get_objects

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm
from django.db import models
from django.shortcuts import render
from .models import Member
from django.shortcuts import get_object_or_404, redirect


def members(request):
    mymembers = Member.objects.all()

    dias_ocupados = [member.eventDay for member in mymembers if member.eventDay]
    dias_ocupados = list(set(dias_ocupados))

    return render(request, 'all_members.html', {'mymembers': mymembers, 'dias_ocupados': dias_ocupados})

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')  # Solo 'main.html'
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['apple', 'banana','cherrys'],
    }
    return HttpResponse(template.render(context, request))

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')
        else:
            return render(request, 'add_member.html', {'form': form})
    else:
        # Si la solicitud es GET (cuando el usuario llega por primera vez a la página),
        # crea un formulario vacío
        form = MemberForm()
    # Renderiza la plantilla del formulario, ya sea vacía (GET) o con errores (POST inválido)
    return render(request, 'add_member.html', {'form': form})

def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('members')