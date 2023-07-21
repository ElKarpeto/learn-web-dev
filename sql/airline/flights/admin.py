from django.contrib import admin
from .models import Flight, Airport, Passenger

# ini untuk section admin, jadi hanya admin yang bisa mengakses section ini nanti

class FlightAdmin(admin.ModelAdmin) :
    list_display = ("id", "origin", "destination", "duration")
    # nama variable sangat diperhatikan, harus "list_display"
    # class ini digunakan untuk menampilkan tabel halaman admin

class Passengeradmin(admin.ModelAdmin) :
    filter_horizontal = ("flights",)
    # filter_horizontal harus berisi tuple, dengan "," di akhirnya

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, Passengeradmin)
