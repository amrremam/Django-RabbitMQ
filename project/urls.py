from django.contrib import admin
from django.urls import path, include
from task.views import ReviewEmailView
# import task


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', ReviewEmailView.as_view(), name="reviews")
    # path('reviews/', include(task.urls)),
]
