from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Group, Profile, Match, Comment, Unmatch
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('logout/')

    matches = Match.objects.filter(users=request.user.id)
    for match in matches:
        for user in match.users.all():
            if user.id != request.user.id:
                match.friend_name = user.name
                break
    context = {
        'matches': matches,
        'users': Profile.objects.exclude(id=request.user.id)
    }

    return render(request, 'meet/index.html', context)


@csrf_protect
def edit_profile(request):
    if request.POST:  # update existing profile
        request.user.name = request.POST['name']
        request.user.gender = request.POST['gender']
        request.user.city = request.POST['city']
        request.user.country = request.POST['country']
        request.user.language = request.POST['language']
        request.user.save()
        return HttpResponseRedirect(reverse('meet:edit_profile'))
    else:
        context = dict((key, str(getattr(request.user, key))) for key in ['name', 'gender', 'city', 'country', 'language'])
        print(context)
        return render(request, 'meet/profile.html', context)


@csrf_protect
def create_user(request):
    if request.method == 'POST':
        try:
            Profile.objects.create_user(username=request.POST['username'], password=request.POST['password'],
                                               email=request.POST['email'])
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return HttpResponseRedirect(reverse('meet:edit_profile'))
        except Exception, e:
            print(str(e))
            return HttpResponse(status=201)
    elif request.method == 'GET':
        return render(request, 'meet/signup.html')


def logout_view(request):
    if request.user.is_authenticated():
        logout(request)

    return render(request, 'meet/logout.html')


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('meet:index'))
    else:
        return HttpResponse('login attempt failed')


def user_detail(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    existing_match = Match.objects.filter(users=user.id).filter(users=request.user.id)

    return render(request, 'meet/user.html', {'user': user, 'match_id': existing_match[0].id if existing_match else None})


def upvote_user(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    user.stars += 1
    user.save()
    return HttpResponseRedirect(reverse('meet:user_detail', args=(user_id,)))


def group_detail(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(request, 'meet/group.html', {'group': group})


def match_detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    title = 'match with ' + ',v'.join([user.name for user in match.users.all() if user != request.user])
    return render(request, 'meet/match.html', {'match': match, 'title': title})


def match(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    match = Match(date=timezone.now())
    match.save()
    match.users.add(user, request.user)
    match.save()

    return HttpResponseRedirect(reverse('meet:match_detail', args=(match.id,)))


def unmatch(request, user_id):
    user = get_object_or_404(Profile, pk=user_id)
    match = Unmatch(date=timezone.now())
    match.save()
    match.users.add(user, request.user)
    match.save()

    return HttpResponseRedirect(reverse('meet:index'))


@csrf_protect
def new_comment(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    comment = Comment(match=match, author=request.user, date=timezone.now(), text=request.POST['comment'])
    comment.save()
    return HttpResponseRedirect(reverse('meet:match_detail', args=(match.id,)))

