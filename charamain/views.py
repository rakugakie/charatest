from django.shortcuts import render
from charatest_project.users.models import User
from charamain.models import Kyaracter, UserProfile, userRelationship
from django.http import HttpResponse, HttpResponseRedirect
from charamain.forms import AddKyara, addFriend, editUserProfile

# Create your views here.


def index(request):

    context_dict = {}

    try:
        userlist = User.objects.order_by('username')

        context_dict['userlist'] = userlist

    except User.DoesNotExist:
        context_dict = {}

    return render(request, 'index.html', context_dict)


def displayprofile(request, owner):
    context_dict = {}
    try:
        owner = User.objects.get(username__iexact=owner)

        try:
            kyaralist = Kyaracter.objects.filter(kyaraowner=owner.id)
            context_dict['kyaralist'] = kyaralist
        except Kyaracter.DoesNotExist:
            pass

        try:
            friendslist = userRelationship.objects.filter(creator=owner.id)
            context_dict['friendslist'] = friendslist
        except userRelationship.DoesNotExist:
            pass

        return render(request, 'displayprofile.html', context_dict)
    except User.DoesNotExist:
        print("The user does not exist")

    return render(request, 'genericresponse.html', {'genericcontent':"The user does not exist"})


def addkyara(request):
    if request.method == "POST":
        form = AddKyara(request.POST, request.FILES)
        if form.is_valid():
            try:
                kyara = form.save()
                kyara.kyaraowner.add(request.user)
                kyara.save()
                return render(request, 'genericresponse.html', {'genericcontent': "Character made successfully!"})
            except:
                return render(request, 'genericresponse.html',
                              {'genericcontent': "Character creation failed! Try again or let us know"})
    else:
        form = AddKyara()

    return render(request,'addkyara.html', {'form': form})

def addfriend(request):
    if request.method == "POST":
        form = addFriend(request.POST)
        if form.is_valid():
            try:
                friend = User.objects.get(username__iexact=form.cleaned_data['friend'])
            except User.DoesNotExist:
                return render(request, 'addfriend.html', {'form': form})
            newfriend = userRelationship(creator=request.user, friend=friend)
            newfriend.save()
            return render(request, 'genericresponse.html', {'genericcontent': "Friend Added!"})
    else:
        form = addFriend()

    return render(request, 'addfriend.html', {'form':form})


def displayProfileForm(request):
    user = request.user
    userprofile = UserProfile.objects.get_or_create(user=user)
    alreadyuser = UserProfile.objects.get(user = user)

    form = editUserProfile(instance=alreadyuser)

    return render(request, 'editprofile.html', {'form': form})


