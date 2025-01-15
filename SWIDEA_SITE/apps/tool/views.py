from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from apps.tool.models import Tool
from apps.tool.forms import Toolform

def list(request):
    tools = Tool.objects.all()
    paginator = Paginator(tools, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'tool/list.html', context)


def detail(request, pk):
    tool = Tool.objects.get(id=pk)
    ideas = tool.ideas.all()
    context = {
        'tool': tool,
        'ideas': ideas
    }
    return render(request, 'tool/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = Toolform(request.POST, request.FILES)
        if form.is_valid():
            tool = form.save()
            return redirect(f'detail/{tool.pk}', tool.pk)
        else:
            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'tool/create.html', context)
    else:
        form = Toolform()
        context = {
            'form': form,
        }
        return render(request, 'tool/create.html', context)


def update(request, pk):
    tool = Tool.objects.get(id=pk)
    if request.method == 'POST':
        form = Toolform(request.POST, request.FILES, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('tool:detail', pk=pk)
        else:
            context = {
                'tool': tool,
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'tool/update.html', context)
    else:
        form = Toolform(instance=tool)
        context = {
            'form': form,
        }
        return render(request, 'tool/update.html', context)


def delete(request, pk):
    Tool.objects.get(id=pk).delete()
    return redirect('tool:list')