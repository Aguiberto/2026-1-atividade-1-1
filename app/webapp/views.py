from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Professor! Sou seu aluno Aguiberto Cândido em SO!")