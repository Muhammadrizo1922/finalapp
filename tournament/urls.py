from django.urls import path
from .views import index,tourdetail,myapply,search, playerinfo


urlpatterns = [
    path('', index, name='index'),
    path('<uuid:tour_id>/detail', tourdetail,name='tourdetail'),
    path('apply', myapply, name='myapply'),
    path('search', search, name='search'),
    path('<uuid:plr_id>/info', playerinfo,name='player'),
]
