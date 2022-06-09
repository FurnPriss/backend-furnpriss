from django.urls import path
from dummy_opennotes import views

urlpatterns = [
    path('dummy-opennotes/', views.DummyOpenNotesList.as_view(), name='dummy-opennotes-list'),
    path('dummy-opennotes/<int:pk>', views.DummyOpenNotesDetail.as_view()),
]
