# from django import forms
#
# class MyForm(forms.Form):

#     def __init__(self):
#           self._user = user
#     email = forms.EmailField(max_length=100)
#
#
#     def clean(self):
#         if is_spam(self.cleaned_data):
#             raise forms.ValidationError("fewfwe", code='spam')
#
#     def save(self):
#         model.save()
#         return model
# class MyForm(forms.ModelForm):
#     model = Post
#     fields = ['tittle', 'content'....]