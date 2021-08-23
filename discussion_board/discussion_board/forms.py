from django import forms
from django.core.exceptions import ValidationError


class CreatePostForm(forms.Form):
    title = forms.CharField(label='Post Title',
                            max_length=128,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    details = forms.CharField(label='Details',
                            max_length=8192,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    anonymous = forms.BooleanField(label='Anonymous',
                            widget=forms.CheckboxInput(),
                            required=False)
    # Not needed because django has built-in validation already
    '''
    def check_title_details(self):
        title = self.cleaned_data['title']
        details = self.cleaned_data['details']
        return title, details
    '''
class CreateReplyForm(forms.Form):
    details = forms.CharField(label='Details',
                            max_length=1024,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    anonymous = forms.BooleanField(label='Anonymous',
                            widget=forms.CheckboxInput(),
                            required=False)
    # Not needed because django has built-in validation already
    '''
    def check_details(self):
        details = self.cleaned_data['details']
        return details
    '''

