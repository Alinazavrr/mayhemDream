from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from django.views import View
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewsForm, PurchaseForm
from .models import News, Product, Purchase, UserProfile

# Create your views here.

def home_page(request):
    return render(request, 'main/main.html')

def rules_page(request):
    return render(request, 'main/rules.html')


# UserProfile CRUD

class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'main/user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        # Получаем профиль пользователя, связанный с текущим пользователем
        return get_object_or_404(UserProfile, user=self.request.user)


# Purchase CRUD

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'main/purchases.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        # Получаем только покупки текущего пользователя
        return Purchase.objects.filter(user_profile__user=self.request.user)

class PurchaseCreateView(FormView):
    template_name = 'main/purchase_create.html'
    form_class = PurchaseForm

    def get_form_kwargs(self):
        # Передаем product_id в параметры формы
        kwargs = super().get_form_kwargs()
        kwargs['product_id'] = self.request.GET.get('product_id')
        return kwargs

    def form_valid(self, form):
        product_id = form.cleaned_data['product_id']
        product = Product.objects.get(pk=product_id)

        # Создаем новую покупку
        Purchase.objects.create(
            user_profile=self.request.user.userprofile,
            product=product
        )

        # Здесь можно добавить логику оплаты, если необходимо

        return redirect('purchase_page')  # Замените 'purchases_page' на ваш путь к странице с покупками

# Product CRUD

class ProductListView(ListView):
    model = Product
    template_name = 'main/products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset # Optionally, you can order by a specific field

class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'main/product_create.html'
    fields = ['name', 'price', 'image', 'description', 'type', 'duration']
    success_url = reverse_lazy('product_page')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'main/product_update.html'
    fields = ['name', 'price', 'image', 'description', 'type', 'duration']
    success_url = reverse_lazy('product_page')


class ProductDeleteView(DeleteView):
    model = Product 
    template_name = 'main/product_delete.html'
    success_url = reverse_lazy('product_page')



# News CRUD

# views.py

class NewsCreateView(CreateView):
    model = News
    template_name = 'main/news_create.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('news_list')

class NewsListView(ListView):
    model = News
    template_name = 'main/news.html'
    context_object_name = 'news_list'

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'main/news_delete.html'
    success_url = reverse_lazy('news_list')

class NewsUpdateView(UpdateView):
    model = News
    template_name = 'main/news_update.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('news_list')