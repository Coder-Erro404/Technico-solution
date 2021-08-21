from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.index, name='resume'),
    path('index', views.index, name='index'),
    path('project', views.projects, name='project'),
    path('blogs', views.blogs , name='blogs'),
    path('documents', views.documents , name='documents'),
    path('Notes', views.Notes , name='Notes'),
    path('impotantImage', views.impotantImages , name='impotantImage'),
    # path('addblog', views.addblogs),
    path('contact', views.contact, name='contact'),
    path('hardware', views.hardware, name='hardware'),
    path('laptop', views.laptop, name='laptop'),
    path('computer', views.computer, name='computer'),
    path('webdesign', views.webdesign, name='webdesign'),
    path('accessories', views.accessories, name='accessories'),
    path('refurbished', views.refurbished, name='refurbished'),
    path('cctv', views.cctv, name='cctv'),
    path('repairing', views.repairing, name='repairing'),
    path('newtechnology', views.newtechnology, name='newtechnology'),
    path('productinfo', views.productinfo, name='productinfo'),
   ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

