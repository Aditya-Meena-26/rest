from django.shortcuts import render, get_object_or_404,redirect
from .models import Review
from .forms import ReviewForm
from product.models import Product

def submit_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            feedback = form.cleaned_data['feedback']
            Review.objects.create(product=product, buyer=request.user, rating=rating, feedback=feedback)
            return redirect('product_detail', pk=product_id)
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})
