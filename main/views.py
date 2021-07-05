from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import TemplateView, DetailView, UpdateView

from main.forms import UserModelForm
from main.models import UserModel


def index(request):
    data = UserModel.objects.all()

    context = {
        'data': data

    }
    return render(request, 'index.html', context)


# class UserTemplateView(TemplateView):
#     template_name = 'index.html'
#     model = UserModel

def detail(request, pk):
    data = get_object_or_404(UserModel, id=pk)

    context = {
        'data': data
    }

    return render(request, 'detail.html', context)


# class UserDetailView(DetailView):
#     template_name = 'detail.html'
#     model = UserModel


def create(request):
    if request.method == 'POST':
        form = UserModelForm(request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

        return redirect('/')
    else:

        form = UserModelForm()

        context = {
            'form': form
        }

        return render(request, 'form.html', context)


# class BookUpdateView(UpdateView):
#     template_name = 'form.html'
#     form_class = UserModelForm
#     success_url = ''
#     model = UserModel

def edit(request, pk):
    user = get_object_or_404(UserModel, pk=pk)

    if request.method == 'POST':
        form = UserModelForm(request.POST, files=request.FILES, instance=user)

        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = UserModelForm(instance=user)

        context = {
            'form': form
        }

        return render(request, 'form.html', context)


def delete(request, pk):
    user = get_object_or_404(UserModel, pk=pk)
    user.delete()
    return redirect('/')
