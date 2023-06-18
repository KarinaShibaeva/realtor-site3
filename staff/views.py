from django.shortcuts import render
from comment.forms import CommentForm
from comment.models import Comment
from staff.models import Staff

def staff_view(request):
    staff_list = Staff.objects.all()
    if request.method=="POST": 
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid(): 
            comment =  form.save(commit=False) 
            #comment. = pk 
            comment.save() 
            form = CommentForm() 
    else:
        form = CommentForm()

    context = {"page": "staff", 'form':form, "staff_list":staff_list}
    return render(request, 'staff/contacts.html', context)
