
from . import models as md
from django.views.generic import *



class Homedetail(DetailView):
    model = md.Kinolar
    template_name = 'homedetail.html'

class Homedetail(DetailView):
    model = md.Kinolar
    template_name = 'homedetail.html'



class Homeupdate(UpdateView):
    fields = '__all__'
    model = md.Kinolar
    template_name = 'homeupdate.html'
    success_url = '/'



class Homedel(DeleteView):
    model = md.Kinolar
    template_name = 'homedelete.html'
    success_url = '/'


class Homepage(ListView):
    model = md.Kinolar
    template_name = 'index.html'
    paginate_by = 8
