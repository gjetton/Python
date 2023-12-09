# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemForm
from .models import Item  # Correct the import statement

def item_list(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'inventory/item_list.html', context)
    search_query = request.GET.get('search', '')

    # Filter items based on the search query
    items = Item.objects.filter(name__icontains=search_query)

    return render(request, 'inventory/item_list.html', {'items': items, 'search_query': search_query})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # Save the form with the current user
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()

    return render(request, 'inventory/add_item.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to your item list URL
    else:
        form = ItemForm(instance=item)

    return render(request, 'edit_item.html', {'form': form, 'item': item})
