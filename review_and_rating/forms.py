from django import forms

class ReviewForm(forms.Form):
    rating = forms.IntegerField(label='Rating', min_value=1, max_value=5)
    feedback = forms.CharField(label='Feedback', widget=forms.Textarea)
