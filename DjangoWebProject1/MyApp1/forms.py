
from django import forms
from .models import teacher
from .models import *
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
class OutlineForm(forms.ModelForm):
    class Meta:
        model = courseForm
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = courseData.objects.none()

        if 'courseArea' in self.data:
            try:
                courseAreaID = int(self.data.get('courseArea'))
                self.fields['course'].queryset = courseData.objects.filter().order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

