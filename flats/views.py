from django.shortcuts import render

def flat_list_view(request):
    context={"flats_list": "flats"}
    return render(request, "flats/flats_list.html",context)
