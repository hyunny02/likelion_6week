from django.urls import path
from .views import *

app_name = 'bulletin'

urlpatterns = [

    path('', BulletinListView.as_view(), name = 'list'),
    path('add/', BulletinCreateView.as_view(), name = 'add'),
    path('detail/<int:pk>/', BulletinDetailView.as_view(), name = 'detail'),
    path('update/<int:pk>/', BulletinUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', BulletinDeleteView.as_view(), name = 'delete'),
]