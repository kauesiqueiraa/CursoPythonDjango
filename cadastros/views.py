from django.shortcuts import render

from cadastros.models import Cidade


# Create your views here.

def lista_cidades(request):

    pass

    # retornar a lista de cidades cadastradas...
    # DRM do Django
    # preparar um SQL
    # executar essa sql no banco...
    # trazer os resultados
    # processar esses resultados...

# qs = Cidade.objects.all()
# qs.capitais = Cidade.objects.filter(capital=True)

# Cidade.objects.count()

# Cidade.objects.all()
# Cidade.objects.count()
# Cidade.objects.all()
# Cidade.objects.filter(capuital=True).count()
# qs = Cidade.objects.filter(capital=True).count()
# Cidade.objects.filter(capital=True).values()
# qs = Cidade.objects.filter(capital=True).values()
# Cidade.objects.filter(capital=True)
# qs
# Cidade.objects.filter()
# qs = Cidade.objects.filter()
# for cidade in qs:
#     print(cidade.nome)

# Cidade.objects.create(nome='Manaus', capital=True)
# Cidade.objects.delete()
# Cidade.objects.filter()
# lista_cidades = list(Cidade.objects.filter())
# lista_cidades = list(Cidade.objects.filter().values())
# lista_cidades = list(Cidade.objects.filter().values('nome'))
# lista_cidades2 = list(Cidade.objects.filter().values_list('nome'))
# lista_cidades2 = list(Cidade.objects.filter().values_list('nome', flat=True))
