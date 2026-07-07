from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipie

# Create your views here.
@login_required(login_url='login')
def recipie(request):
    print(request.user.username)
    if request.method == "POST":

        name = request.POST.get('name')
        description = request.POST.get('recipe_description')
        image = request.FILES.get('recipe_image')
        print(name)
        print(description)
        Recipie.objects.create(
            user=request.user,
            name=name,
            description=description,
            image=image
        )
        
        return redirect('/recipie/')
    queryset = Recipie.objects.filter(user=request.user)
    print(queryset)
    context = {'recipes': queryset}
    return render(request, 'recipie.html',context)

#function for delete
@login_required(login_url='login')
def delete_recipie(request, id):
    querryset = get_object_or_404(
    Recipie,
    id=id,
    user=request.user
   )
    querryset.delete()
    return redirect('recipie')

# function for update
@login_required(login_url='login')
def update_recipie(request,id):
    query_set = get_object_or_404(
    Recipie,
    id=id,
    user=request.user
    )
    if request.method == 'POST' :
        query_set.name = request.POST.get('name')
        query_set.description = request.POST.get('recipe_description')
        image = request.FILES.get('recipe_image')

        if image:
            query_set.image = image
        query_set.save()
        return redirect('recipie')
    context = {'recipe': query_set}
    return render(request,'update_recipie.html',context)
