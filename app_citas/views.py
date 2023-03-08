from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm

from .form import  RegisterForms, QuoteForm, UpdateUser

from django.contrib.auth.models import User 

from django.contrib import messages #import messages
#libreria para autenticar usuarios
from django.contrib.auth import login, logout, authenticate
#libreria para crear formulario de login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#Importar modelo
from.models import Quotes

from django.shortcuts import get_object_or_404
# Create your views here.
def wep_page(request):
    register_form = RegisterForms()
    login_form = AuthenticationForm
    if request.method == 'GET':
        return render(request, 'index.html',{'register_form' :register_form,
                                             'login_form':login_form})
    else:
        if 'register' in request.POST:
            register_form = RegisterForms(request.POST)
           
            if register_form.is_valid():
                register_form.save()
                
                messages.add_message(request=request, level=messages.SUCCESS, message="Usuario creado correctamente")

                return redirect(wep_page)
            else:
                if request.POST['password1'] != request.POST['password2']:
                    messages.add_message(request=request, level=messages.ERROR, message="Las contraseñas no coinciden" )
                elif request.POST['username'] != None:
                    messages.add_message(request=request, level=messages.ERROR, message="El Email ingresado ya existe" )
                else:
                    return render(request, 'index.html',{'register_form' :register_form,
                                                         'login_form':login_form})

                return render(request, 'index.html',{'register_form' :register_form,
                                                     'login_form':login_form})
        elif 'login' in request.POST:
            user = authenticate(request, username= request.POST['username'],
                                password=request.POST['password'])
            if user is None:    
                messages.add_message(request=request, level=messages.ERROR, message="Email o contraseña incorrecta" )
                return redirect(wep_page)
            elif user != None:
                login(request, user)
                return redirect(usuarios)
            


def usuarios(request):
    nombre = User.objects.all().filter(username=request.user).values_list('first_name', flat=True)[0]
    apellido = User.objects.all().filter(username=request.user).values_list('last_name', flat=True)[0]
    citas = Quotes.objects.all()
    quote_form = QuoteForm
    if request.method == 'GET':
        return render(request, 'usuarios.html',{'nombre':nombre,
                                            'citas':citas,
                                            'quote_form':quote_form,
                                            'apellido':apellido})
    else:
        quote_form = QuoteForm(request.POST)
        new_quote=quote_form.save(commit=False)
        new_quote.user = request.user
        new_quote.save()
        return redirect('usuarios')
        
def cerrar_sesion(request):
    logout(request)
    return redirect(wep_page)

def del_quote(request, quote_id):
    quote = get_object_or_404(Quotes.objects.all().filter(pk=quote_id), pk=quote_id, user=request.user)
    if request.method == 'POST':
        quote.delete()
    return redirect(usuarios)

def perfil(request, username=None):
    nombre = User.objects.all().filter(username=request.user).values_list('first_name', flat=True)[0]
    apellido = User.objects.all().filter(username=request.user).values_list('last_name', flat=True)[0]
    user = User.objects.get(username=username)
    citas = Quotes.objects.all().filter(user=user)
    return render(request,'perfil.html',{'citas':citas,
                                         'nombre':nombre,
                                         'apellido':apellido})

def update_user(request):
    update_form=UpdateUser
    if request.method == 'POST':
        update_form = UpdateUser(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect(update_user)
        else:
            messages.add_message(request=request, level=messages.ERROR, message="El Email ingresado ya existe" )

    else:
        return render(request,'update_user.html',{'update_form':update_form})
    return render(request,'update_user.html',{'update_form':update_form})