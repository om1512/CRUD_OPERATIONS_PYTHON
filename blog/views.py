from django.shortcuts import render
from django.shortcuts import (get_object_or_404,
                              render, 
                              HttpResponseRedirect)

# relative import of forms
from .models import BlogModel
from .forms import BlogForms

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    form = BlogForms(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "Create_view.html",context)

def list_view(request):
# dictionary for initial data with
# field names as keys
    context ={}
# add the dictionary during initialization
    context["dataset"] = BlogModel.objects.all()
    return render(request, "List_view.html", context)
# pass id attribute from urls
def detail_view(request, id):
# dictionary for initial data with
# field names as keys
    context ={}
# add the dictionary during initialization
    context["data"] = BlogModel.objects.get(id = id)
    return render(request, "Detail_view.html", context)

# update view for details
def update_view(request, id):
# dictionary for initial data with
# field names as keys
    context ={}
# fetch the object related to passed id
    obj = get_object_or_404(BlogModel, id = id)
# pass the object as instance in form
    form = BlogForms(request.POST or None, instance = obj)
# save the data from the form and
# redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/blog/"+id)
# add form dictionary to context
    context["form"] = form
    return render(request, "Update_view.html", context)

def delete_view(request, id):
# dictionary for initial data with

# field names as keys
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(BlogModel, id = id)

    if request.method =="POST":
    # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/blog/list")
    return render(request, "Delete_view.html", context)
