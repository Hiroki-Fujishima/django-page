import django
from django.shortcuts import render
form django.views import View

class SampleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app_folder/top_page.html')
top_page = SampleView.as_view()
