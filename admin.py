from django.contrib import admin
from .models import *
# Register your models here.




class ProjectAttachmentInline(admin.TabularInline):
	model = ProjectAttachment
	extra = 1

	# def has_change_permission(self, request, obj=None):
	# 	return False
	#
	# def has_add_permission(self, request, obj=None):
	# 	return False
	#
	# def has_delete_permission(self, request, obj=None):
	# 	return False

class ProjectMemberInline(admin.TabularInline):
	model = ProjectMember
	extra = 1

	def has_change_permission(self, request, obj=None):
		return False

	def has_add_permission(self, request, obj=None):
		return False

	def has_delete_permission(self, request, obj=None):
		return False


class ProjectDetailsAdmin(admin.ModelAdmin):
    inlines = [ProjectAttachmentInline,ProjectMemberInline]
    list_display = ["user","name","start_date","due_date","request_type","description","loom_links","no_of_pages","created"]
    search_field = ['user__email','request_type']
admin.site.register(ProjectDetails,ProjectDetailsAdmin)


#admin  viedoproject code start




class ViedoProjectAdmin(admin.ModelAdmin):

	list_display = ["project_title", "type_request", "project_description", "Loom_linkAdd", "Attachment_viedoAdd", ]
	search_field = ['project_title', 'type_request']

admin.site.register(ViedoProject, ViedoProjectAdmin)
# loom list
class Loom_linkAddAdmin(admin.ModelAdmin):
	list_display = ["Loom_videolink" ]
admin.site.register(Loom_linkAdd, Loom_linkAddAdmin)


#Attachment_viedoAdd
class Attachment_viedoAddAdmin(admin.ModelAdmin):
	list_display = ["Attachment_viedo" ]

admin.site.register(Attachment_viedoAdd, Attachment_viedoAddAdmin)
#




