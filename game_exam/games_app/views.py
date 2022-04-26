from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from game_exam.games_app.forms import ProfileForm, GameAddForm, GameEditForm, GameDeleteForm, ProfileEditForm
from game_exam.games_app.models import Profile, Game


def home(request):
    person = Profile.objects.first()
    context = {
        'person': person,
    }
    return render(request, 'home-page.html', context)
    # return HttpResponse('home')


def dashboard(request):
    person = Profile.objects.first()
    games = Game.objects.all().order_by('id')
    context = {
        'person': person,
        'games': games,
    }
    return render(request, 'dashboard.html', context)
    # return HttpResponse('dashboard')


def game_create(request):
    if request.method == 'POST':
        form = GameAddForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(home)
        else:
            context = {
                'form': form,
            }
            return render(request, 'create-game.html', context)
    else:
        form = GameAddForm()
        context = {
            'form': form,
        }
        return render(request, 'create-game.html', context)
    # return HttpResponse('game create')


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
    }
    return render(request, 'details-game.html', context)
    # return HttpResponse('game details')


def game_edit(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            context = {
                'form': form,
            }
            return render(request, 'edit-game.html', context)
    else:
        form = GameEditForm(initial=game.__dict__)
        context = {
            'form': form,
        }
        return render(request, 'edit-game.html', context)
        # return HttpResponse('game edit')


def game_delete(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('dashboard')
    else:
        form = GameDeleteForm(initial=game.__dict__)
        context = {
            'form': form,
        }
        return render(request, 'delete-game.html', context)

    # return HttpResponse('game delete')


def profile_create(request):
    # person = Profile.objects.first()
    # form = ProfileForm(request.POST)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = ProfileForm(request.POST)
        context = {
            'form': form,
        }
        return render(request, 'create-profile.html', context)
    # return HttpResponse('profile create')


def profile_details(request):
    person = Profile.objects.first()
    games = Game.objects.all()
    average_rating = 0
    for game in games:
        average_rating += game.rating
    if person:
        games_count = games.count()
        context = {
            'person': person,
            'games_count': games_count,
            'average_rating': average_rating,
        }
        return render(request, 'details-profile.html', context)


    # return HttpResponse('profile details')


def profile_edit(request):
    person = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
        else:
            context = {
                'form': form,
            }
            return render(request, 'edit-profile.html', context)
    else:
        form = ProfileEditForm(initial=person.__dict__)
        context = {
            'form': form,
        }
        return render(request, 'edit-profile.html', context)
    # return HttpResponse('profile edit')


def profile_delete(request):
    person = Profile.objects.first()
    games = Game.objects.all()
    if request.method == 'POST':
        person.delete()
        if games:
            games.delete()
        return redirect('home')
    else:
        return render(request, 'delete-profile.html')
    # return HttpResponse('profile delete')
