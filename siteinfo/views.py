from django.shortcuts import render

def main_view(request):
    context = {"page": "main"}
    return render(request, 'siteinfo/main.html', context)

def about_view(request):
    context = {"page": "about"}
    return render(request, 'siteinfo/about.html', context)
