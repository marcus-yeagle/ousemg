from django.contrib import admin

from .models import Member

class MemberAdmin(admin.ModelAdmin):
	list_display = ('id', 'first_name', 'last_name', 'group_status')
	list_display_links = ['id']
	list_filter = ['group_status']
	search_fields = ['first_name', 'major', 'year', 'last_name']
	class Meta:
		model = Member

admin.site.register(Member, MemberAdmin)