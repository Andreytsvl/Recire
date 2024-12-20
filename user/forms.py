from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from user.models import User


class UserLoginForm(AuthenticationForm):
    """Форма для входа пользователя."""

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        # Добавляем классы для стилизации полей (опционально)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class UserRegistrationForm(UserCreationForm):
    """Форма для регистрации пользователя."""

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'phone_number')

    phone_number = forms.CharField(
        label="Номер телефона",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        # Добавляем классы для стилизации полей (опционально)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class ProfileForm(UserChangeForm):
    """Форма для редактирования профиля пользователя."""

    class Meta:
        model = User
        fields = ('image', 'phone_number')

    image = forms.ImageField(
        label="Аватар",
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )
    phone_number = forms.CharField(
        label="Номер телефона",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Убираем ненужные поля, которые не нужны в профиле
        self.fields.pop('password')  # Убираем поле пароля