from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
#from .forms import ProjectForm, PortfolioForm
from django.contrib import messages
from .forms import ProjectForm, PortfolioForm
from django.shortcuts import get_object_or_404


# Student Views
class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

#Portfolio Views
class PortfolioListView(generic.ListView):
    model = Portfolio

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio_id = self.object.id # Adds the current portfolio id to new variable
        context['projects'] = Project.objects.filter(portfolio_id=portfolio_id) # Sorts through all projects and sends only those associated with current portfolio
        return context

#Portfolio Functions
def updatePortfolio(request, pk):
  # Adds portfolio record/object into new variable
  portfolio = get_object_or_404(Portfolio, pk=pk) 
  
  if request.method == 'POST':
    portfolio_data = request.post.copy() # Copies the changes from POST reuest made by client 
    form = PortfolioForm(portfolio_data, instance = portfolio) # Saves changes to form 
    if form.is_valid():
      form.save()
      return redirect('portfolio-detail', pk=pk) # Redirects user back to portfolio-detail after request has been completed
  else:
    form = PortfolioForm(instance=portfolio)
    
  context={'form': form,'portfolio': portfolio, }
  return render(request, 'portfolio_app/portfolio_update.html', context)

#Project Views
class ProjectListView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project

# Project Functions 
def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        
        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)

#Project Functions 
def deleteProject(request, pk):
    # Add project record/object into new variable
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete() # Delete project
        return redirect('portfolio-detail', pk=project.portfolio.id) # Redirect user back to portfolio-detail page
    
    context = {'project': project}
    return render(request, 'portfolio_app/project_delete.html', context)

def updateProject(request, pk):
  project = get_object_or_404(Project, pk=pk)
  if request.method == 'POST':
    project_data = request.POST.copy() # Requests copy of changes from POST reuqest made by client 
    form = ProjectForm(project_data, instance = project) # Saves changes to form 
    if form.is_valid():
      form.save() # saves updated form 
      return redirect('project-detail', pk=pk) # Returns to project-detail page if changes were successfull 
  else:
    form = ProjectForm(instance=project) # reverts project back to inital state 
   
    context={'form': form, 'project': project,}
    return render(request, 'portfolio_app/project_update.html', context)
  
#Index Fucntion
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})
