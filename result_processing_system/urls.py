# IMPORT FROM DJANGO
from django.contrib import admin
from django.urls import (
    path,
    include
)

# IMPORT FROM LOCAL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include("results.urls"))
]
