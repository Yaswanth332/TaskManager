from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.views.decorators.http import require_http_methods
from .forms import RegistrationForm
# Create your views here.
class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('TaskList')
    
    
class registerPage(FormView):
    template_name='base/register.html'
    form_class=RegistrationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('TaskList')
    
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(registerPage,self).form_valid(form)
    
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('TaskList')
        return super(registerPage,self).get(*args,**kwargs)
   
class Logoutview(LogoutView):
    template_name='base/logout.html'
    def get(self, request, *args, **kwargs):
        """Allow GET requests for logout"""
        return self.post(request, *args, **kwargs)

class Tasklist(LoginRequiredMixin,ListView):
    model = Task
    context_object_name='tasks'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False).count()
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']=context['tasks'].filter(title__startswith=search_input)
        
        context['search_input']=search_input
        return context
        
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task  # This tells Django which model to use
    context_object_name = 'task'  # This makes it accessible in the template
    template_name = "base/task_detail.html"  
# class TaskDetail(DetailView):
#     def get_queryset(self):
#         return Task.objects.filter(user=self.request.user)  # Example: Only user-specific tasks

class TaskCreation(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','complete']#list all th itesm in the model
    success_url=reverse_lazy('TaskList')
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreation,self).form_valid(form)
    
    
class TaskUpdtat(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']##list all th itesm in the model
    success_url=reverse_lazy('TaskList')
    
# class TaskDelete(DeleteView):
#     modele=Task
#     context_object_name='tasks'
#     success_url=reverse_lazy('TaskList')
    
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task  # Fixed typo (was 'modele')
    context_object_name = 'task'
    success_url = reverse_lazy('TaskList')

    def get_queryset(self):
        return Task.objects.all()

class Logoutview(LogoutView):
    template_name='base/logout.html'
    
    def get(self, request, *args, **kwargs):
        """Allow GET requests for logout"""
        return self.post(request, *args, **kwargs)
    