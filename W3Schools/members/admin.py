from django.contrib import admin
from .models import Member

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", 'email', 'gender', "created_at", 'updated_at')
  search_fields = ('firstname',)
  list_filter = ('is_active',)
  prepopulated_fields = {"slug": ("firstname", "lastname")}

# admin.site.register(Member, MemberAdmin)
