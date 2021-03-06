"""payumoje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as coreVievs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', coreVievs.home, name="HomePage" ),
    path('payu-notification', coreVievs.payuNotification, name="payuNotification" ),
    path('add-to-cart', coreVievs.addToCart, name="add-to-cart"),
    path('remove-from-cart', coreVievs.removeFromCart, name="remove-from-cart"),
    path('chceckout', coreVievs.chceckout, name="chceckout"),
    path('chceckout-confirm', coreVievs.chceckoutConfirm, name="chceckout-confirm"),
    path('order/<order_id>',coreVievs.orderStatus),
    path('order-status/<order_id>',coreVievs.orderStatusData)
]
