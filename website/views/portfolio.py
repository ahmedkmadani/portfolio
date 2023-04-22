from django.shortcuts import render
from website.models.portfolio import Portfolio, Category


def portfolio(request):
    portfolios = Portfolio.objects.all()
    ccategory = Category.objects.all()
    return render(request, 'portfolio.html', {'portfolios': portfolios, 'category': ccategory})
