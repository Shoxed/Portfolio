from django.forms import ModelForm
from .models import Project, Portfolio


#Form for Project Model 
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =('title', 'description')

#Form for Portfolio Model
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields =('title', 'contact_email', 'is_active', 'about')   