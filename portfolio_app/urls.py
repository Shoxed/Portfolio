from django.urls import path
from . import views

urlpatterns = [
    #Student Paths 
    path('', views.index, name = 'index'),
    path('students/', views.StudentListView.as_view(), name= 'students'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    #Portfolio Paths
    path('portfolios/', views.PortfolioListView.as_view(), name= 'portfolios'),
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('portfolio/<int:pk>/update_portfolio/', views.updatePortfolio, name='update-portfolio'),
    #Project Paths 
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
<<<<<<< HEAD
    path('portfolio/<int:portfolio_id>/delete_project/<int:project_id>', views.deleteProject, name='delete-project'),
    path('portfolio/<int:portfolio_id>/update_project/<int:project_id>', views.updateProject, name='update-project'),
    path('portfolio/update_portfolio/<int:portfolio_id>', views.updatePortfolio, name='update-portfolio'),
=======
    path('project/<int:pk>/delete_project/', views.deleteProject, name='delete-project'),
    path('project/<int:pk>/update_project/', views.updateProject, name='update-project'),
>>>>>>> 42acc90a9d7422a333aed5643c528296530b57dc
]
