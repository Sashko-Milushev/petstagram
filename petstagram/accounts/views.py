from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import UserCreateForm

UserModel = get_user_model()


# def login_user(request):
#     return render(request, 'accounts/login-page.html')

class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


# def register_user(request):
#     return render(request, 'accounts/register-page.html')

class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        login(request, self.object)

        return response


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


# def details_user(request, pk):
#     return render(request, 'accounts/profile-details-page.html')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set.prefetch_related('photolike_set')

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        return context


# def edit_user(request, pk):
#     return render(request, 'accounts/profile-edit-page.html')
#

class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'gender')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


# def delete_user(request, pk):
#     return render(request, 'accounts/profile-delete-page.html')


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
