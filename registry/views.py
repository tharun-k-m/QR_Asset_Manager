from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
import base64
from django.core.files.base import ContentFile

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'registry/home.html')

@login_required
def dashboard(request):
    items = Item.objects.filter(owner=request.user)
    return render(request, 'registry/dashboard.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'registry/detail.html', {'item': item})


@login_required
def create_item(request):
    if request.method == "POST":
        # Capture the new fields
        item = Item(
            owner=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            serial_number=request.POST.get('serial_number'),
            purchase_price=request.POST.get('purchase_price') or None,
            purchase_date=request.POST.get('purchase_date') or None,
            warranty_expiry=request.POST.get('warranty_expiry') or None,
            location=request.POST.get('location'),
            is_public=request.POST.get('is_public') == 'on'
        )

        # Handle image (Webcam or File)
        webcam_image = request.POST.get('webcam_image')
        if webcam_image:
            format, imgstr = webcam_image.split(';base64,')
            item.image.save(f"cam_{item.name}.png", ContentFile(base64.b64decode(imgstr)), save=False)
        else:
            item.image = request.FILES.get('image')

        item.save()
        return redirect('dashboard')

    return render(request, 'registry/create_item.html', {'categories': Item.CATEGORY_CHOICES})
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)  # Strict ownership check
    if request.method == "POST":
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.is_public = request.POST.get('is_public') == 'on'

        # Only update image if a new one is uploaded
        if request.FILES.get('image'):
            item.image = request.FILES.get('image')

        item.save()
        return redirect('item_detail', pk=item.id)

    return render(request, 'registry/edit_item.html', {'item': item})


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)  # Strict ownership check
    if request.method == "POST":
        item.delete()
        return redirect('dashboard')
    return redirect('item_detail', pk=pk)