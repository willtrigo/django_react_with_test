"""View frontend."""
from django.shortcuts import render


def index(request):
    """Render index."""
    return render(request, 'frontend/index.html')
