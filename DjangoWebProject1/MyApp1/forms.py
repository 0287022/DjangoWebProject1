
from django import forms
from .models import teacher
from .models import courseArea
areas = []
for d in list(courseArea.objects.all().values("courseArea")): areas.append(d["courseArea"])
courses = []
for d in list(courseArea.objects.all().values("course")): courses.append(d['course'])
combination = []
values = []
for i in range(len(areas)):
    values.append(i+1)
    combination.append(areas[i] + " - " + courses[i])
class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']
class GenerateForm(forms.Form):
    options = zip(values, combination)
    dropdown = forms.ChoiceField(choices=options, widget=forms.Select, label="Select Course:")
class OutlineForm(forms.Form):
    assessmentYear = forms.IntegerField(min_value=2000, max_value=2050, initial=2000)
    assessmentSemester = forms.IntegerField(min_value = 1, max_value = 2)

