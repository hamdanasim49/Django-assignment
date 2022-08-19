from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import item


def todoappView(request):
    latest_item_list = item.objects.all()

    template = loader.get_template("tasks/todoList.html")
    context = {
        "latest_item_list": latest_item_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request):
    return render(request, "tasks/detail.html")


def submit(request):
    obj = item()
    obj.title = request.GET["title"]
    obj.description = request.GET["description"]
    if obj.title == "" or obj.description == "":
        return render(request, "tasks/detail.html")
    else:
        obj.save()
        return redirect("todolist:todoappView")


def change(request, item_id):
    it = get_object_or_404(item, pk=item_id)
    if it.status:
        it.status = False
    else:
        it.status = True
    it.save()
    return HttpResponseRedirect(reverse("todolist:todoappView"))


def delete(request, item_id):
    it = get_object_or_404(item, pk=item_id)
    it.delete()
    return HttpResponseRedirect(reverse("todolist:todoappView"))


def update(request, item_id):
    it = get_object_or_404(item, pk=item_id)
    template = loader.get_template("tasks/update.html")
    context = {
        "item": it,
    }
    return HttpResponse(template.render(context, request))


def edit(request, item_id):
    it = get_object_or_404(item, pk=item_id)
    title = request.GET["title"]
    description = request.GET["description"]
    it.title = title
    it.description = description
    it.save()
    return HttpResponseRedirect(reverse("todolist:todoappView"))
