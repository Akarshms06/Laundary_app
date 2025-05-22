from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .models import Order  # ✅ Import your Order model


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('place_order')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')


@login_required
def place_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        men_count = int(request.POST.get('men_count', 0))
        women_count = int(request.POST.get('women_count', 0))
        pickup_date = request.POST.get('pickup_date')
        contact = request.POST.get('contact')
        address = request.POST.get('address')

        # Calculate total and delivery date
        total_amount = (men_count * 50) + (women_count * 70)
        pickup_dt = datetime.strptime(pickup_date, "%Y-%m-%dT%H:%M")
        delivery_date = pickup_dt + timedelta(days=3)

        # ✅ Save order to database
        Order.objects.create(
            user=request.user,
            name=name,
            men_count=men_count,
            women_count=women_count,
            pickup_date=pickup_dt,
            delivery_date=delivery_date,
            contact=contact,
            address=address,
            total_amount=total_amount
        )

        # Show confirmation
        return render(request, 'delivery.html', {
            'name': name,
            'total_amount': total_amount,
            'delivery_date': delivery_date.strftime("%Y-%m-%d %H:%M")
        })

    return render(request, 'place_order.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def delivery(request):
    if request.method == 'POST':
        messages.success(request, 'Delivery scheduled successfully!')
        return redirect('place_order')
    return render(request, 'delivery.html')

def app_details(request):
    return render(request, 'app_details.html')

from .models import Order
from django.contrib.auth.decorators import login_required


