from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("add-exercise", views.add_exercise, name="add-exercise"),
    path('exercise-list/', views.exercise_list, name='exercise-list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", views.index, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
