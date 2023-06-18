from django.shortcuts import render
from comment.forms import CommentForm
from comment.models import Comment

def flat_list_view(request):
    
    if request.method=="POST": 
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid(): 
            comment =  form.save(commit=False) 
            #comment. = pk 
            comment.save() 
            form = CommentForm() 
    else:
        form = CommentForm()

    context = {'page':'flats', #'comments_list':comments,
               'form':form}
    return render(request, "flats/flats_list.html", context)

def flat_sell_view(request):
    if request.method=="POST": 
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid(): 
            comment =  form.save(commit=False) 
            #comment. = pk 
            comment.save() 
            form = CommentForm() 
    else:
        form = CommentForm()

    context = {'page':'flats','form':form}
    return render(request, 'flats/flats_sell.html', context)

def flats_sale2_view(request):
    if request.method=="POST": 
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid(): 
            comment =  form.save(commit=False) 
            #comment. = pk 
            comment.save() 
            form = CommentForm() 
    else:
        form = CommentForm()
    context = {"page": "flats_sale2", 'form':form}
    return render(request, 'flats/flats_sale2.html', context)

