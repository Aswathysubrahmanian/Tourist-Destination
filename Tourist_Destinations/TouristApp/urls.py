from django.urls import path
from . import views
urlpatterns = [
    
    path("create/",views.DestinationListView.as_view(),name='create'),
    path("destination-create/",views.createDestination,name='destination-create'),
    path("",views.Home_page,name='listview'),
    path("details/<int:pk>/",views.DestinationDetailView.as_view(),name='details'),
    path("details-view/<int:dest_id>/",views.Detail_view,name='details-view'),
    path("update/<int:pk>/",views.DestinationUpdateView.as_view(),name='update'),
    path("update-destination/<int:dest_id>/",views.Update_view,name='update-destination'),
    path("delete/<int:pk>/",views.DestinationDeleteView.as_view(),name='delete'),
    path("delete-destination/<int:dest_id>",views.delete_view,name='delete-destination'),


]
