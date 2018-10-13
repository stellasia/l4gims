from django.views.generic import TemplateView

class CurrentStatusView(TemplateView):
    template_name = "current_status.html"


class ForecastStatusView(TemplateView):
    template_name = "forecast.html"
