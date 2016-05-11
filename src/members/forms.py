from django import forms

from .models import Member

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = [
			"first_name",
			"last_name",
			"year",
			"major",
			"group_status",
		]