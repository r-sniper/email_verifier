from django.conf.urls import url

from my import views

app_name = "exam"
urlpatterns = [
    # /verify_email/add
    url(r'^verify_email/$', views.verify_email, name='verify_email'),


]
