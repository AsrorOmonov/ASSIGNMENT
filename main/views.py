from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView

from main.forms import UserModelForm
from main.models import UserModel


class UserListView(LoginRequiredMixin, ListView):
    """ data variable is object_list """
    template_name = 'index.html'

    # model = UserModel
    # queryset = UserModel.objects.all()
    def get_queryset(self):
        users = UserModel.objects.all().order_by('-pk')
        # q = self.request.GET.get('q')  # for search
        #
        # if q:
        #     users = users.filter(Q(name__icontains=q))

        return users


# def index(request):
#     data = UserModel.objects.all()
#
#     context = {
#         'data': data
#
#     }
#     return render(request, 'index.html', context)


class UserDetailView(LoginRequiredMixin, DetailView):
    """ name of user object is : object """
    template_name = 'detail.html'
    model = UserModel


# def detail(request, pk):
#     data = get_object_or_404(UserModel, id=pk)
#
#     context = {
#         'data': data
#     }
#
#     return render(request, 'detail.html', context)


class UserCreateView(LoginRequiredMixin, CreateView):
    """ name of object is "form" """
    template_name = 'form.html'
    form_class = UserModelForm
    success_url = '/'

    # def form_valid(self, form):
    #     body = f'{form.instance.name} is added to database'
    #
    #     send_mail(
    #         'User is created',  # topic
    #         body,  # text within the body var
    #         'User Admin System',  # from whom
    #         recipient_list=['mr.omonov_asror@mail.ru']
    #     )

    # return super().form_valid(form)

    # def form_invalid(self, form):
    #     return super().form_invalid(form)

    # 998990108666 Ruhsora

    # Just grant 998998205800


# def create(request):
#     if request.method == 'POST':
#         form = UserModelForm(request.POST, files=request.FILES)
#
#         if form.is_valid():
#             form.save()
#
#         return redirect('/')
#     else:
#
#         form = UserModelForm()
#
#         context = {
#             'form': form
#         }
#
#         return render(request, 'form.html', context)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """ name of object is "form" """
    template_name = 'form.html'
    form_class = UserModelForm
    success_url = '/'
    model = UserModel


# def edit(request, pk):
#     user = get_object_or_404(UserModel, pk=pk)
#
#     if request.method == 'POST':
#         form = UserModelForm(request.POST, files=request.FILES, instance=user)
#
#         if form.is_valid():
#             form.save()
#
#         return redirect('/')
#     else:
#         form = UserModelForm(instance=user)
#
#         context = {
#             'form': form
#         }
#
#         return render(request, 'form.html', context)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    success_url = '/'
