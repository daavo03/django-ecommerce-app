# Mapping the view function to URL pattern

from django.urls import path
from django.urls.conf import include
# We also have another router DefaultRouter
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views




# Creating router object
# If we use DeafultRouter we get 2 additional features. 1) basic root view in localhost/store, 2) getting data in json adding .json of route
#router = SimpleRouter()
router = DefaultRouter()
# Register our viewsets with this router object. We'll be saying that the products endpoint should be manage by the ProductViewSet 
#Passing 2 arguments: 1. Prefix value we're using as the name of our endpoint "products", 2. Our viewset
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

"""
# URLConf
urlpatterns = [
    # In order to use view class need to use as_view() method which will convert the class to a regular function based view
    path('products/', views.ProductList.as_view()),
    # Adding a parameter
    #Applying a converter to this parameter
    # Our generic view expects the parameter ID to be called PK, so we change it
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('collections/', views.CollectionList.as_view()),
    # We can give this mapping a name which is used in the serializer argument "view_name"
    # also changing the parameter to pk
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail')
]
"""

# URLConf
# If we don't have explicit patterns
urlpatterns = router.urls
""" 
# If we have some specific patterns in the array
urlpatterns = [
    # For route it's an empty string, and we're gonna include() and with it we can import routes from somewhere else
    path('', include(router.urls))
] 
"""