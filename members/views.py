from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Member
from .forms import MemberForm

def members_create(request):
	form = MemberForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Sucessfully Created!")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Error, not created.")

	if request.method == "POST":
		print(request.POST.get("first_name"))
		print(request.POST.get("last_name"))
	
	context = {
		"form":form,
	}
	return( render(request, "member_form.html", context) )



def members_detail(request, id):
	instance = get_object_or_404(Member, id=id)
	context = {
		"title":"detail",
		"instance":instance,
	}
	return render(request, "member_detail.html", context)



def members_update(request, id=None):
	instance = get_object_or_404(Member, id=id)
	form = MemberForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Updated Successfully")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title":"detail",
		"instance":instance,
		"form":form,
	}
	
	return render(request, "member_form.html", context)



def members_delete(request, id=None):
	instance = get_object_or_404(Member, id=id)
	instance.delete()
	messages.success(request, "Deleted Successfully")
	
	return redirect("members:list")



def members_list(request):
	board_mems = Member.objects.filter(group_status='Board')
	head_mems = Member.objects.filter(group_status='Head')
	anal_mems = Member.objects.filter(group_status='Analyst')

	context = {
		"board_members":board_mems,
		"head_analyst":head_mems,
		"analyst":anal_mems,
		"title":"list",
	}

	return render(request, "members_list.html", context)