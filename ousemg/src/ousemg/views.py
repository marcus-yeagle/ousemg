from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class AboutView(TemplateView):
    template_name = "about.html"


class HowView(TemplateView):
    template_name = "how.html"


class NoSchoolView(TemplateView):
    template_name = "noschool.html"


class faqView(TemplateView):
	template_name = "faq.html"