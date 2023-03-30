from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Language, SkillSet

# class UserProfileForm(forms.ModelForm):
#     #language = ModelMultipleChoiceField(queryset=Language.objects.all())
#     #skills = ModelMultipleChoiceField(queryset=SkillSet.objects.all())
#     class Meta:
#         model = UserProfile
#         fields = ('full_name', 'profile_picture','money_per_hour','language','skills')
        
#     language = forms.ModelMultipleChoiceField(
#     queryset=Language.objects.all(),
#     widget=forms.CheckboxSelectMultiple
#     )
#     skills = forms.ModelMultipleChoiceField(
#     queryset=SkillSet.objects.all(),
#     widget=forms.CheckboxSelectMultiple
#     )
        
#     def form_valid(self, form):
#         form.instance.username = self.request.user.username
#         return super().form_valid(form)



class MyModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ 'full_name', 'profile_picture','money_per_hour']
        # widgets = {
        #     'language': forms.CheckboxSelectMultiple(),
        # }