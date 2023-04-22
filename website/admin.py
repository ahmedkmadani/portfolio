from django.contrib import admin
from website.models.about import About, Fact, Client, Service, Testimonial
from website.models.resume import Education, Experience, Certificates, SoftSkill, CodingSkill
from website.models.portfolio import Portfolio, Category
from website.models.blog import Blog,CategoryBlog


admin.site.register(Client)
admin.site.register(Fact)
admin.site.register(Service)
admin.site.register(About)
admin.site.register(Testimonial)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certificates)
admin.site.register(SoftSkill)
admin.site.register(CodingSkill)
admin.site.register(Portfolio)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(CategoryBlog)


