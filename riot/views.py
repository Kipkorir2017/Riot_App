from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from riot.forms import SignUpForm
from .models import Profile,Location
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.urls import reverse
# Create your views here.
def riot_home(request):

    profiles=Profile.objects.all()
    locations=Location.objects.all()
    return render(request,'index.html',{'profiles':profiles,'locations':locations})



def profile(request):
    current_user = request.user
    locations = Location.objects.filter(user=current_user.id).all
    return render(request, 'registration/profile.html', {"locations": locations})


def location(request, id):
    locations = Location.objects.get(id=id)
    return render(request, 'location.html', {"locations": locations})



def view_location(request, id):
    locations = Location.objects.get(id=id)
              
    return render(request, 'viewproject.html',{'locations':locations})


def search_location(request):
    if 'location' in request.GET and request.GET['location']:
        location = request.GET.get("location")
        results = Location.search_location(location)
        message = f'location'
        return render(request, 'search.html', {'locations': results, 'message': message})
    else:
        message = "You haven't searched for any location,try again"
    return render(request, 'search.html', {'message': message})


def signup(request):
    print('here')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('full_name')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})
