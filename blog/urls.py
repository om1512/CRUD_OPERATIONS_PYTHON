from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_view, name='Create_view'),
    path('list', views.list_view, name='List_view'),
    path('<id>',views.detail_view, name='Detail_view'),
    path('<id>/update',views.update_view, name='Update_view'),
    path('<id>/delete',views.delete_view, name='Delete_view'),
]