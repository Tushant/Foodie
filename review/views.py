import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages

from restaurants.models import Restaurant
from .models import Review 

from .forms import ReviewForm

# def review_list(request):
#     latest_review_list = Review.objects.order_by('-created')[:9]
#     context = {'latest_review_list':latest_review_list}
#     return render(request, 'reviews/review_list.html', context)


# def review_detail(request, review_id):
#     review = get_object_or_404(Review, pk=review_id)
#     return render(request, 'reviews/review_detail.html', {'review': review})

def review_thread(request, review_id):
	review_object = get_object_or_404(Review, id=review_id)
	# content_object = review_object.content_object
	# content_id = review_object.content_object.id
	initial_data = {
		'content_type':review_object.content_type, # no need to give () because its a parenthesis
		'object_id':review_object.object_id
	}
	form = ReviewForm(request.POST or None, initial=initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get('content_type')
		content_type = ContentType.objects.get(model=c_type)
		object_id = form.cleaned_data.get('object_id')
		review = form.cleaned_data.get('review')
		parent_obj = None
		try:
			parent_id = int(request.POST.get('parent_id')) # <input type="hidden" name="parent_id" />
		except:
			parent_id = None
		if parent_id:
			parent_qs = Review.objects.filter(id=parent_id)
			if parent_qs.exists():
				parent_obj = parent_qs.first()
		new_review, created = Review.objects.get_or_create(
								reviewer = request.user,
								content_type = content_type,
								object_id = object_id,
								review = review,
								parent = parent_obj
								)
		return redirect(new_review.content_object.get_absolute_url())
	context = {
		"review":review_object,
		"review_form":form
	}
	return render(request, 'review/review_thread.html', context)


def add_review(request, review_id):
	restaurant = get_object_or_404(Restaurant, pk=review_id)
	print('restaurant from review form',restaurant)
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.cleaned_data['review']
			Review.objects.create(reviewer=request.user,restaurant=restaurant,review=review)
			return redirect('/restaurants/')
	else:
		form = ReviewForm()
	return render(request, 'review/review_form.html', {'form':form})
