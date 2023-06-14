from django.shortcuts import render, get_object_or_404
from flats_sale.models import Flat, Category, Object
from django.views.generic import ListView
from flats_sale.forms import FlatSearchForm
from comment.forms import CommentForm
from comment.models import Comment

class SaleListView(ListView):
    model = Flat
    context_object_name = 'flats_sale'
    template_name = 'flats_sale/flats_sale.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = FlatSearchForm()         
        return context                          

    def get(self, request, *args, **kwargs):
        
        form = FlatSearchForm(self.request.GET)
        if form.is_valid():
           cd = form.cleaned_data  
           flats = self.model.objects.filter(name__icontains=cd['search'])
        else:    
            flats = self.model.objects.all()
        return render(request, self.template_name, self.get_context_data(object_list=flats))

def sale_id_view(request, pk):
    object_list = Object.objects.filter(pk=pk)
    category_list = Category.objects.filter(object_name=pk)
    pk = get_object_or_404(Flat, pk=pk)
    #comments = pk.comments.all()
    if request.method=="POST": 
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid(): 
            comment =  form.save(commit=False) 
            #comment. = pk 
            comment.save() 
            form = CommentForm() 
    else:
        form = CommentForm()

    context = {"pk": pk,'page':'flats', #'comments_list':comments,
               'form':form,'category_list': category_list,
               'object_list':object_list}
    return render(request, "flats_sale/flats_detail.html", context)