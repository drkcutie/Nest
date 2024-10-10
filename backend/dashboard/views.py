from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .forms import CategoryForm
from .models import Category
from common.utils import upload_local_image

# User Settings View
class UserSettingsView(View):
    template_name = 'dashboard/user_settings.html'

    def get(self, request):
        categories = Category.objects.filter(userID=request.user)
        return render(request, self.template_name, {'categories': categories})
    



# Dashboard View
class DashboardView(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request, id=None):
        categories = Category.objects.filter(userID=request.user)
        form = CategoryForm()
        return render(request, self.template_name, {
            'categories': categories,
            'form': form,
        })

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.userID = request.user
            category.save()
            messages.success(request, "Successfully Added New Category")
            return redirect('dashboard')
        else:
            print(form.errors)
            return self.get(request)  # Render the same page with form errors
        


#Dashboard-Nest-Tab
class DashboardNestView(View):
    template_name = 'dashboard/dashboard_nest_tab.html'

    def get(self, request, id):
        # Assuming you're looking for a specific category by id
        category = Category.objects.filter(categoryID=id, userID=request.user).first()
        if category is None:
            # Handle the case where the category doesn't exist
            messages.error(request, "Category not found.")
            return redirect('dashboard')  # Redirect to main dashboard

        return render(request, self.template_name, {'category': category})

   

    



# Upload Image View
class UploadImageView(View):
    def post(self, request):
        img = request.FILES.get('profileimg')
        if img:
            publicurl = upload_local_image(img, 'userprofile')
            request.user.profile_pic = publicurl
            request.user.save()
        return redirect('user_settings')  # Redirect back to user settings or another appropriate page
