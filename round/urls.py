from django.urls import path
from .views import roundmatches


urlpatterns = [
    path('<uuid:rnd_id>/matches',roundmatches,name='roundmatches')

]
