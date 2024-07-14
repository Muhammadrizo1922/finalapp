from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tournament.urls')),
    path('round/', include('round.urls')),
]