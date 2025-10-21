from django.shortcuts import render

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
