from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    new_list=List.objects.create()
    item = Item(text=request.POST['item_text'], list=new_list)
    try:
        item.full_clean()
        # only save the item if the item is not empty
        item.save()
    except ValidationError:
        new_list.delete()
        error = "You can't have an empty item"
        return render(request, 'home.html', {"error": error})
    return redirect('/lists/%d/' % (new_list.id,))

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    # 'items' is a key.
    return render(request, 'list.html', { 'list': list_,})

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text = request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))

def delete_item(request, item_id):
    item_ = Item.objects.get(id=item_id)
    list_ = item.list
    # delete the item
    return redirect('/lists/%d/' % (list_.id))
