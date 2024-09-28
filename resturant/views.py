from django.shortcuts import render
from django.views import generic, View


class IndexPage(View):
    """
    Customer will be able to view the landing page
    """

    def get(self, request, *args, **kwargs):
        return render(request, '../templates/index.html')
