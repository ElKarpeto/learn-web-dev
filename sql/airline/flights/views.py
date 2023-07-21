from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights" : Flight.objects.all()
    })

def flight(request, flight_id) :
    flight = Flight.objects.get(pk=flight_id)
    # pk itu primary key
    return render(request, "flights/flight.html", {
        "flight" : flight,
        "passengers" : flight.passengers.all(),
        "non_passengers" : Passenger.objects.exclude(flights=flight).all()
        # non_passenger menyimpan data Passenger yang tidak terdata pada variable flight pada func ini
    })

def book(request, flight_id) :
    if request.method == "POST" :
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # passenger mengambil data Passenger dari pk yang kita POST pada HTML
        passenger.flights.add(flight)
        # bagian ini untuk menambahkan flight ke dalam passenger pada func ini
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
        # setelah semua tereksekusi, maka kita akan kembali ke halaman "flight" dengan args flight_id

