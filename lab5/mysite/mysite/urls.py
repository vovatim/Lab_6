from bk.views import index, ExampleView, OrdersView, OrderView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', index),
    url(r'^example$', ExampleView.as_view()),
    url(r'^order$', OrdersView.as_view(), name='orders_url'),
    url(r'^order/(?P<id>\d+)$', OrderView.as_view(), name ='order_url'),
]
