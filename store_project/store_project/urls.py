from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated:
        if request.user.profile.role == 'seller':
            return redirect('seller_dashboard')
        else:
            return redirect('customer_dashboard')
    return redirect('login')

urlpatterns = [
    path('', home),  
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('inventory/', include('inventory.urls')),
    path('sales/', include('sales.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )