from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import UserProfile


def profile(request, profile_slug):
	if profile_slug is None:
		userprofile = get_object_or_404(UserProfile,slug=profile_slug)
	else:
		userprofile = get_object_or_404(UserProfile, slug=profile_slug)
		user_restaurant = userprofile.restaurant.all()
		user_order = userprofile.order_history.all()
		total_purchase = userprofile.total_purchase
	return render(request, 'userprofiles/profile.html', {'userprofile':userprofile, 
														'user_restaurant':user_restaurant,
														'user_order':user_order,
														'total_purchase':total_purchase
														})



# class UserProfileDetailView(DetailView):
# 	model = UserProfile
# 	slug_url_kwarg = 'profile_slug'
# 	template_name = 'userprofiles/profile.html'

# 	# def get_object(self, queryset=None):
# 	# 	user = super(UserProfileDetailView, self).get_object(queryset)
# 	# 	UserProfile.objects.get_or_create(user=user)
# 	# 	return user 

# 	def get_context_data(self, **kwargs):
# 		context = super(UserProfileDetailView, self).get_context_data(**kwargs)
# 		context['userprofile'] = get_object_or_404(UserProfile, slug=self.kwargs['slug'])
# 		# context['user_restaurant'] = userprofile.restaurant.all()
# 		context['user_order'] = userprofile.order_history.all()
# 		return context




