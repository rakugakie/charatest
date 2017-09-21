from django.shortcuts import render
from charatest_project.users.models import User
from charamain.models import Kyaracter, UserProfile, UserRelationship, ChatGroup, MessageText
from django.http import HttpResponse, HttpResponseRedirect
from charamain.forms import AddKyara, addFriend, editUserProfile, SendMessage

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
        context_dict['profileowner'] = owner
        try:
            userprofile = UserProfile.objects.get(user=owner)
            context_dict['profileDescription'] = userprofile.profileDescription
            context_dict['picture'] = userprofile.picture
        except UserProfile.DoesNotExist:
            pass

        try:
            kyaralist = Kyaracter.objects.kyaralist(owner.id)
            context_dict['kyaralist'] = kyaralist
        except Kyaracter.DoesNotExist:
            pass

        try:
            friendslist = UserRelationship.objects.friendslist(owner.id)
            context_dict['friendslist'] = friendslist
        except UserRelationship.DoesNotExist:
            pass
        except:
            raise Exception("Unknown Error Occured at friendslist")

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
            newfriend = UserRelationship(creator=request.user, friend=friend)
            newfriend.save()
            return render(request, 'genericresponse.html', {'genericcontent': "Friend Added!"})
    else:
        form = addFriend()

    return render(request, 'addfriend.html', {'form':form})



def displayProfileForm(request):
    user = request.user
    edituserform, userprofile = UserProfile.objects.get_or_create(user=user)
    if request.method == "POST":
        form = editUserProfile(request.POST, request.FILES, instance=edituserform)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect("/")
            except UserProfile.DoesNotExist:
                print("beepboop")
                pass
    else:
        form = editUserProfile(instance=edituserform)

    return render(request, 'editprofile.html', {'form': form})


def displaychat(request, groupID):
    context_dict = {}
    form = SendMessage
    context_dict['form'] = form
    if groupID:
        context_dict['groupID'] = groupID

        try:
            chatgroup = ChatGroup.objects.get(groupID=groupID)
            context_dict['chatgroup'] = chatgroup

            participants = chatgroup.participantUserID.all()
            context_dict['participants'] = participants

            if request.user not in participants:
                return render(request, 'genericresponse.html',
                              {'genericcontent': "You are not part of this group!"})

            messages = chatgroup.messagetext_set.all().order_by('created')
            context_dict['messages'] = messages

            # try:
            #     messages = ChatGroup.objects.getmessages(chatgroup)
            #     context_dict['messages'] = messages
            # except ChatGroup.DoesNotExist or MessageText.objects.DoesNotExist:
            #     pass
            # except:
            #     raise Exception("Unknown Error Occurred")

            if request.method == "POST":
                form = SendMessage(request.POST)
                if form.is_valid():
                    newmessage = form.save(commit=False)
                    newmessage.messageGroup = chatgroup
                    newmessage.messageSender = request.user
                    newmessage.save()

        except ChatGroup.DoesNotExist:
            pass
        except:
            raise Exception("Unknown Error Occurred")
    else:
        pass
    return render(request,'displaychat.html', context_dict)






