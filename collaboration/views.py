from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from collaboration.models import Resource


def add_resource(request):
    if request.method == "POST":
        model_name = request.POST.get('model')
        object_id = request.POST.get('object_id')

        name = request.POST.get('name')
        description = request.POST.get('description')
        type_ = request.POST.get('type')
        amount = request.POST.get('amount')
        university = request.POST.get('university')
        department = request.POST.get('department')
        image = request.FILES.get('image')

        content_type = ContentType.objects.get(model=model_name)

        Resource.objects.create(
            name=name,
            description=description,
            type=type_,
            amount=amount,
            university=university,
            department=department,
            image=image,
            content_type=content_type,
            object_id=object_id
        )

        if model_name == "thesis":
            return redirect('post:view_thesis', pk=object_id)
        elif model_name == "event":
            return redirect('post:view_event', pk=object_id)
        elif model_name == "project":
            return redirect('post:view_project', pk=object_id)

    return render(request, "add_resource.html")

def edit_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    if request.method == 'POST':
        resource.name = request.POST.get('name')
        resource.description = request.POST.get('description')
        resource.type = request.POST.get('type')
        resource.amount = request.POST.get('amount')
        resource.university = request.POST.get('university')
        resource.department = request.POST.get('department')

        if request.FILES.get('image'):
            resource.image = request.FILES['image']

        resource.save()

        model = request.POST.get('model')
        object_id = request.POST.get('object_id')

        if model == "project":
            return redirect('post:view_project', pk=object_id)
        elif model == "event":
            return redirect('post:view_event', pk=object_id)
        elif model == "thesis":
            return redirect('post:view_thesis', pk=object_id)
        else:
            return redirect('collaboration:view_resource', pk=resource.id)

    model = request.GET.get('model')
    object_id = request.GET.get('object_id')
    return render(request, 'collaboration/edit_resource.html', {
        'resource': resource,
        'type': model,
        'obj': {'id': object_id}
    })


def view_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'collaboration/view_resource.html', {'resource': resource})

def delete_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'collaboration/confirm_delete_resource.html', {'resource': resource})

def confirm_delete(request, pk):

    if request.method == 'POST':
        model_name = request.POST.get('model')
        object_id = request.POST.get('object_id')
        resource = get_object_or_404(Resource, pk=pk)
        resource.delete()
        if model_name == "thesis":
            return redirect('post:view_thesis', pk=object_id)
        elif model_name == "event":
            return redirect('post:view_event', pk=object_id)
        elif model_name == "project":
            return redirect('post:view_project', pk=object_id)
        return redirect('home')

    return render(request, 'collaboration/confirm_delete_resource.html')
