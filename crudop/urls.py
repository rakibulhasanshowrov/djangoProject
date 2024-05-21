from django.urls import path

# Your URL patterns

from . import views

urlpatterns=[
    path('',views.crudop,name='crudop'),
    path('album_list/<int:artist_id>',views.album_list,name="album_list"),
    path('add_musician/',views.add_musician,name="add_musician"),
    path('add_album/',views.add_album,name="add_album"),
    path('musician_list/',views.musician_list,name="musician_list"),
    path('edit_artist_info/<int:artist_id>',views.edit_artist_info,name="edit_artist_info"),
    path('edit_album/<int:album_id>',views.edit_album,name="edit_album"),
    path('delete_album/<int:album_id>',views.delete_album,name='delete_album'),
    ]