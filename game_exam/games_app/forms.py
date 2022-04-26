from django import forms
from django.forms import TextInput

from game_exam.games_app.models import Profile, Game


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }



class GameAddForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'category', 'rating', 'max_level', 'game_image_url', 'summary']


class GameEditForm(GameAddForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameDeleteForm(GameAddForm):
    class Meta:
        model = Game
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'


class ProfileEditForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password', 'first_name', 'last_name', 'profile_picture_url']