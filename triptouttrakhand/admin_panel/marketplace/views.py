from django.shortcuts import render

from service.models import Item, Activity, Place


def index(request):
    items = Item.objects.filter(is_available=True)[0:6]
    activities = Activity.objects.all
    places = Place.objects.all
    return render(request, 'marketplace/index.html', {
        'items': items,
        'activities': activities,
        'places': places
    })


def contact(request):
    return render(request, 'marketplace/contact.html')
