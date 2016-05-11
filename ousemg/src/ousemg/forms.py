from members.models import Intern
from django import forms


class InternForm(forms.ModelForm):
	class Meta:
		model = Intern
		fields = [
			"email",
		]