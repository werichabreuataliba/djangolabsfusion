from distutils.command.upload import upload
from tabnanny import verbose
import uuid
from django.db import models
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criado = models.DateField(_('Criação'), auto_now_add=True)
    modificado = models.DateField(_('Atualização'), auto_now=True)
    ativo = models.BooleanField(_('Ativo?'), default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-stats-up', _('Gráfico')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    )
    servico = models.CharField(_('Serviço'), max_length=100)
    descricao = models.CharField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')
    
    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField(_('Cargo'), max_length=100)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')
    
    def __str__(self):
        return self.cargo
    
class Funcionario(Base):
    nome = models.CharField(_('Nome'), max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_path, variations= {'thumb': { 'width': 480, 'height': 480 } } )
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')
    
    def __str__(self):
        return self.nome


class Feature(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-stats-up', _('Gráfico')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
        ('lni-laptop-phone', _('Laptop')),
        ('lni-leaf', _('Folha'))
    )
    feature = models.CharField(_('Feature'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=18, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')
    
    def __str__(self):
        return self.feature