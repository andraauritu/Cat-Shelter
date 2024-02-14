from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Cat, Adoption
from .forms import ScheduleVisitForm


# Create your views here.
class IndexView(ListView):
    model = Cat
    template_name = 'catalog/cat_list.html'
    context_object_name = 'cat_list'

class DetailView(LoginRequiredMixin, DetailView):
    model = Cat
    template_name = 'catalog/cat_detail.html'
    context_object_name = 'cat'
    login_url = '/catalog/login/'  # Redirect to login page if not authenticated
    redirect_field_name = 'redirect_to'
   

class ConfirmationView(TemplateView):
    template_name = 'catalog/confirmation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_id = self.kwargs['pk']
        context['cat'] = get_object_or_404(Cat, pk=cat_id)
        return context
def schedulevisit(request, cat_id):
    cat = get_object_or_404(Cat, pk=cat_id)
    if request.method == 'POST':
        form = ScheduleVisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.cat = cat
            visit.visitor = request.user
            #visit.full_name = request.user.get_full_name()
            visit.save()
            cat.adoption_status = 'pending'  # Update the cat's adoption status to 'pending'
            cat.save()
            return render(request, 'catalog/confirmation.html', {'cat': cat, 'visit': visit})
    else:
        form = ScheduleVisitForm()

    return render(request, 'catalog/schedule_visit.html', {'form': form, 'cat': cat})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Redirect to a success page.
            return redirect('catalog:index')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
