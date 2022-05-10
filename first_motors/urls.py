"""first_motors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core_app.views import home_view, co_details, \
    services, products, mining, contactUS,  \
    productDetails, storyDetail, aboutView, signup, \
    login, activeamail, cart, verifyEmail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('about_company/', co_details, name='company_details'),
    path('services/', services),
    path('products/', products),
    path('mining/', mining),
    path('contactus/', contactUS),
    path('productDetails/', productDetails, name=''),
    path('story-detail/', storyDetail),
    path('about/', aboutView, name='about'),
    path('signup/', signup, name='signup'),
    path('login/', login, name="login"),
    path('active-email/', activeamail),
    path('cart/', cart),
    path('verify-email/', verifyEmail)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
