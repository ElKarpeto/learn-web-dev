from django.contrib import admin
from .models import Flight, Airport, Passenger

# ini untuk section admin, jadi hanya admin yang bisa mengakses section ini nanti

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
