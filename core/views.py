from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import MenuItem, Reservation

def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'index.html', {'menu_items': menu_items})


def reserve_table(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')

        Reservation.objects.create(
            name=name,
            phone=phone,
            date=date,
            time=time,
            guests=guests
        )
        return redirect('home')