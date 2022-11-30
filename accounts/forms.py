from django import forms

from .models import Contact, Student ,Project
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  

class ContactForm(forms.ModelForm):  
    class Meta:  
        model = Contact
        fields = "__all__" 
    
class ProjectForm(forms.ModelForm):  
    class Meta:  
        model = Project
        fields = "__all__" 