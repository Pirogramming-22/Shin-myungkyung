from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from apps.idea.models import Idea
from apps.idea.forms import Ideaform
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json

def toggle_like(request, idea_id):
    if request.method == 'POST':
        try:
            idea = Idea.objects.get(id=idea_id)
            idea.is_liked = not idea.is_liked
            idea.save()
            return JsonResponse({'is_liked': idea.is_liked})
        except Idea.DoesNotExist:
            return JsonResponse({'error': 'Idea not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def update_interest(request):
    if request.method == "POST":
        data = json.loads(request.body)
        idea_id = data.get("id")
        action = data.get("action")
        try:
            idea = Idea.objects.get(id=idea_id)
            if action == "increase":
                idea.interest += 1
            elif action == "decrease" and idea.interest > 0:
                idea.interest -= 1
            idea.save()

            return JsonResponse({
                "success": True,
                "new_interest": idea.interest
            })
        except Idea.DoesNotExist:
            return JsonResponse({
                "success": False,
                "error": "Idea not found."
            })
    return JsonResponse({"success": False, "error": "Invalid request."})


def list(request):
    sort_by = request.GET.get('sort_by', 'created_at')

    if sort_by == 'interest':
        ideas = Idea.objects.all().order_by('-interest')  # 관심도순
    elif sort_by == 'is_liked':  # 'is_liked'로 변경
        ideas = Idea.objects.all().order_by('-is_liked', '-created_at')  # 찜한순
    elif sort_by == 'title':
        ideas = Idea.objects.all().order_by('title')  # 이름순
    elif sort_by == 'latest':
        ideas = Idea.objects.all().order_by('-created_at')  # 최신순
    else:
        ideas = Idea.objects.all().order_by('created_at')  # 등록순

    paginator = Paginator(ideas, 4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sort_by': sort_by,
    }
    return render(request, 'idea/list.html', context)


def detail(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {
        'idea': idea,
    }
    return render(request, 'idea/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = Ideaform(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect(f'detail/{idea.pk}', idea.pk)
        else:
            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'idea/create.html', context)
    else:
        form = Ideaform()
        context = {
            'form': form,
        }
        return render(request, 'idea/create.html', context)


def update(request, pk):
    idea = Idea.objects.get(id=pk)
    if request.method == 'POST':
        form = Ideaform(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea:detail', pk=pk)
        else:
            context = {
                'idea': idea,
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'idea/update.html', context)
    else:
        form = Ideaform(instance=idea)
        context = {
            'form': form,
        }
        return render(request, 'idea/update.html', context)


def delete(request, pk):
    Idea.objects.get(id=pk).delete()
    return redirect('idea:list')