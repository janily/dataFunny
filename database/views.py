from django.shortcuts import render,render_to_response
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from database.models import *

# Create your views here.

# def save(request):
#     if request.method == "POST":
#         form = ArtistForm(request.POST);
#         form.save();
#         return HttpResponseRedirect('/artists');
#
# def create(request):
#     if request.method == "GET":
#         form = ArtistForm();
#         return render(request,'create.html',{'form':form});

def create(request):
    if request.method == "GET":
        form = ArtistForm();
        return render(request ,'create.html',{'form':form});
    elif request.method == "POST":
        form = ArtistForm(request.POST);
        form.save();
        return HttpResponseRedirect('/artists');

def update(request, id=''):
    form = ArtistForm(request.POST)

    if form.is_valid():
        artist = Artist.objects.get(id = id)
        form = ArtistForm(request.POST,instance= artist)
        form.save()
        return HttpResponseRedirect('/artists')
    else:
        artist = Artist.objects.get(id = id)
        form = ArtistForm(instance=artist)
        return render_to_response('update.html',{ 'form':form }, context_instance=RequestContext(request))



def delete(request, id=''):
    try:
        artist = Artist.objects.get(id=id)
    except Exception:
        raise Http404
    if artist:
        artist.delete()
        return HttpResponseRedirect('/artists')


def artists(request):
    artists = Artist.objects.all();
    return render_to_response('artist.html', {'artists': artists})

def detail(request, id=''):
    try:
        print "XXXX"
        artist = Artist.objects.get(id = id)
    except Artist.DoesNotExist:
        raise Http404
    return render_to_response('details.html', {'artist': artist})