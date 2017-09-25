from django.shortcuts import render
from kyara.forms import AddKyara


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
