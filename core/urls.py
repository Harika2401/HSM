from django.urls import path
from core import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
app_name= "core"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.reg,name='reg') ,
    path("store/",views.store) ,
    path("store2/",views.store2) ,
    path("store3/",views.store3,name='store3') ,
    path("store4/",views.store4,name='store4') ,
    path("store5/",views.store5,name='store5') ,
    path("store6/",views.store6,name='store6') ,
    path("store7/",views.store7,name='store7') ,
    path("perfumes/",views.perfumes,name='perfumes') ,
    path("bathandbody/",views.bathandbody,name='bathandbody') ,
    path("blog/",views.blog,name='blog') ,
    path("userlog/", views.loginpage,name='userlog'),
    path("unknownskin/", views.unknownskin,name='unknownskin'),
    path("knownhair/", views.knownhair,name='knownhair'),
    path('index/', views.index, name='index'),
    path('image/', views.image, name='image'),
    path('skincare/', views.skincare, name='skincare'),
    path('knownskin/', views.knownskin, name='knownskin'),
    path('darkspot/', views.darkspot, name='darkspot'),
    path('acne/', views.acne, name='acne'),
    path('tan/', views.tan, name='tan'),
    path('aging/', views.aging, name='aging'),
    path("skintype/",views.skintype,name='skintype'),
    path("prodesc6/",views.prodesc6,name='prodesc') ,
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)