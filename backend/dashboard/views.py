from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .forms import CategoryForm, FolderForm, LinksForm
from .models import Category, Folders, Links
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

    

    #GET FUNCTION TO GET ALL THE CATEGORY TO DISPLAY FOR SIDEBAR AND MAIN CONTENT
    def get(self, request, id=None):
        folders = Folders.objects.filter(userID=request.user)
        category = Category.objects.filter(userID=request.user)  # Fetch categories based on user

        form = CategoryForm()
        return render(request, self.template_name, {
            'folders': folders,
            'category':  category,
            'form': form,
        })

    # TO CREATE CATEGORY
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
            
            messages.error(request, "Category not found.")
            return redirect('dashboard')

        
        folders = Folders.objects.filter(categoryID=category, userID=request.user)


        return render(request, self.template_name, {'category': category, 'folders' : folders})
    
    def post(self, request,id):
        folder_form = FolderForm(request.POST)
        link_form = LinksForm(request.POST)
        if folder_form.is_valid() and link_form.is_valid():
            folders = folder_form.save(commit=False)
            folders.userID = request.user  
            folders.categoryID_id = id
            folders.save()

            links = link_form.save(commit=False)
            links.folder_id = folders.folderID
            links.user = request.user
            links.save()
            print("added success folder")
            print("Link CategoryID", links.folder_id)
            messages.success(request, "Added Folder Successfully")

            return redirect('dashboard-nest-tab', id=id)
        
        else:
            print("Folder Form Errors:", folder_form.errors)
            print("Link Form Errors:", link_form.errors)
            print('no added')

        
        
        return self.get(request, id)
    

  



   

    



# Upload Image View
class UploadImageView(View):
    def post(self, request):
        img = request.FILES.get('profileimg')
        if img:
            publicurl = upload_local_image(img, 'userprofile')
            request.user.profile_pic = publicurl
            request.user.save()
        return redirect('user_settings')  # Redirect back to user settings or another appropriate page
