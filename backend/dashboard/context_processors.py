from .models import Category


def context(request):
   
    categories = Category.objects.filter(userID=request.user)
    
    return {"categories": categories}