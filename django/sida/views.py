from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response

from .forms import NameForm

#Eitthver þarf að breyta þessum kóða og láta AngularJS virka svo að í staðin að
#það redirectar á texta HttpResponse þá fer hann aftur inn á Profile
#nafnið á að breytast, about og þegar annað hvort Gender þá kemur lítil mynd af
#Karlkyn eða Kvennkyn og segir svo hvor kynið

def get_name(request):
    if request.method == 'GET':
        form = NameForm(request.GET)
        if form.is_valid():
            return HttpResponse("you have changed your profile successfully")
            #return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

############################################################

from .forms import ModelFormWithFileField

def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
