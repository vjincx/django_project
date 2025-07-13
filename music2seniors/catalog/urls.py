

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('performers/', views.performerListView.as_view(), name ='performers'),
    path('senior_homes/', views.serniorhomeListView.as_view(), name ='senior_homes'),

]

urlpatterns += [
    path('performer/<int:pk>', views.PerformerDetailView.as_view(), name = 'performer-detail'),
    path('senior_home/<int:pk>', views.SeniorhomeDetailView.as_view(), name = 'senior_home-detail'),
    path('enquiry/<int:pk>', views.EnquiryDetailView.as_view(), name = 'enquiry-detail'),
]

urlpatterns += [
    path('enquiry/create/', views.EnquiryCreate.as_view(), name='enquiry-create'),

]

