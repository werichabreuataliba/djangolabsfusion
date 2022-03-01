from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Funcionario, Servico, Feature
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        
        size = Feature.objects.all().order_by('?').count()
        half = int(size / 2)

        posts = list(Feature.objects.all().order_by('?')[:size])
        first_group_feature = posts[:half]
        second_group__feature = posts[half:]
        
        context['primeiro_grp_recurso'] = first_group_feature
        context['segundo_grp_recurso'] = second_group__feature

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)