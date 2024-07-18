from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='dashboard'),
    path('addrecord/', views.add_records, name='addrecord'),
    path('delete/<int:id>', views.delete_function, name='delete'),
    path('update/<int:id>', views.upd_info, name='update'),
    path('update/uprecord/<int:id>', views.uprecord, name='uprecord')

]