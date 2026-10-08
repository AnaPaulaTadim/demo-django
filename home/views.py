from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Mensagem


def index(request):
    mensagens = Mensagem.objects.all()
    return render(request, "home/index.html", {"mensagens": mensagens})

#Criando a view para a pagina sobre(recebe a requisição e retorna a pagina sobre.html)
def sobre(request):                                   # ← nova view
    return render(request, "home/sobre.html")
