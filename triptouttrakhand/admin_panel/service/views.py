from django.shortcuts import render, get_object_or_404

from .models import Item


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.all().exclude(pk=pk)[0:3]
    related_items_activity = Item.objects.filter(activity=item.activity, is_available=True).exclude(pk=pk)[0:3]

    return render(request, 'service/detail.html', {
        'item': item,
        'related_items': related_items,
        'related_items_activity': related_items_activity
    })
