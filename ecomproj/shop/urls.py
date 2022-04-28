from django.urls import path,include

from . import views
app_name='shop'

urlpatterns = [

    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:prod_slug>',views.proDetail,name='prod_cat_details')
]
