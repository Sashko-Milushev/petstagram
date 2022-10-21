from django import forms

from petstagram.pets.models import Pet


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'personal_photo')
        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Link to Image',
        }
        widgets = {
            'name': forms.TextInput(
                attrs= {
                    'placeholder': 'Pet name'
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs= {
                    'type': 'date',
                    'placeholder': 'mm/dd/yyyy'
                }
            ),
            'personal_photo': forms.TextInput(
                attrs= {
                    'placeholder': 'Link to image'
                }
            ),
        }


class PetEditForm:
    pass


class PetDeleteForm:
    pass