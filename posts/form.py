from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-[#7695EC] focus:border-[#7695EC] block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#7695EC] dark:focus:border-[#7695EC]',
            'placeholder': 'Hello World',
            'id': 'title',
            'required': 'required'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-[#7695EC] focus:border-[#7695EC] block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-[#7695EC] dark:focus:border-[#7695EC]',
            'placeholder': 'Content here',
            'cols': '30',
            'rows': '5',
            'id': 'description',
            'required': 'required'
        })