from django.urls import path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('rules/', views.rules_page, name='rules_page'),

    path('profile/', views.UserProfileView.as_view(), name='user_profile'),

    path('shop/', views.ProductListView.as_view(), name='product_page'),
    path('shop/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('shop/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('shop/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('shop/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('purchase/', views.PurchaseListView.as_view(), name='purchase_page'),
    path('purchase/create/', views.PurchaseCreateView.as_view(), name='purchase_create'),

    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/create/', views.NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),
    # Другие пути URL
]

