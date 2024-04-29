from django.contrib import admin
from watchlist_app.models import Movie,Director,MovieActor,Technician 

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(MovieActor)
admin.site.register(Technician)

# Register your models here.
