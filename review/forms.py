from django import forms 

from .models import Review 

class ReviewForm(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	# parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
	review = forms.CharField(widget=forms.Textarea)
