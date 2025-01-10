from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
#from comment.models import Comment

# Create your views here.

def review_list(request):   #제목, 개봉 년도, 장르, 별점
    reviews = Review.objects.all()   #values('title', 'release_year', 'genre', 'rating')
    context = {'reviews': reviews}
    return render(request, 'review/list.html', context)

def review_create(request):     #제목, 개봉년도, 장르, 별점, 러닝타임, 리뷰, 감독, 배우
    if request.method=='POST':
        review = Review.objects.create(
            title = request.POST['title'],
            release_year = request.POST['release_year'],
            genre = request.POST['genre'],
            rating = request.POST['rating'],
            running_time = request.POST['running_time'],
            review_content = request.POST['review_content'],
            director = request.POST['director'],
            cast = request.POST['cast'],
        )
        return redirect(reverse('review:review_list'))
    return render(request, 'review/create.html')

def review_detail(request, pk):
    reviews = Review.objects.get(id=pk)
    context = {
         'review' : reviews
    }
    return render(request, 'review/detail.html', context) #여기확인

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)  # 안전하게 객체 가져오기
    if request.method=="POST":
        title2 = request.POST.get('title')
        release_year2 = request.POST.get('release_year')
        genre2 = request.POST.get('genre')
        rating2 = request.POST.get('rating')
        running_time2 = request.POST.get('running_time')
        review_content2 = request.POST.get('review_content')
        director2 = request.POST.get('director')
        cast2 = request.POST.get('cast')
        
        review.title = title2
        review.release_year = release_year2
        review.genre = genre2
        review.rating = rating2
        review.running_time = running_time2
        review.review_content = review_content2
        review.director = director2
        review.cast = cast2
        review.save()
        return redirect('review:review_detail', pk=review.pk)

    context = {
        'review':review
    }
    return render(request, 'review/update.html', context)


def review_delete(request, pk):
    if request.method == 'POST':
        review = Review.objects.get(id = pk)
        review.delete()
        return redirect('review:review_list')
    return redirect('review:review_list')