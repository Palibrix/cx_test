from django.urls import path

from orders import views

urlpatterns = [
    path('customer/', views.create_customer, name='create_customer'),
    path('order/', views.create_order, name='create_order'),
    path('user/<int:pk>', views.OrderAPIViewSet.as_view(), name='user_data')
]
