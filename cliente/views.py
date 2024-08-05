from django.shortcuts import redirect, render
from django.http import HttpResponse

from cliente.form import ClienteForm
from. models import Cliente ,Servicos



# Create your views here.

def cliente_add(request):
    form = ClienteForm(request.POST or None) 
    
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cliente')
    
    context = {
        
        "form": form
    }
    
    return render(request, 'cliente.html', context)
        #return HttpResponse('teste')
    

def cliente(request):
    if request.method == "GET":
        return render(request,'cliente.html')
    elif request.method == "POST":
        
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        telefone_fixo = request.POST.get('telefone_fixo')
        nomeId = request.POST.get('nomeId')
       
        #para identificar e não deixar os dados repetir.
        
        cliente = Cliente.objects.filter(email=email)
        
        if cliente.exists():
            return render(request, "cliente.html",{'nome': nome,'celular':celular,'telefone_fixo':telefone_fixo})
        
        cliente = Cliente.objects.filter(celular=celular)
        
        if cliente.exists():
            return render(request, "cliente.html", {'nome': nome,'email':email,'telefone_fixo':telefone_fixo})
        
        cliente = Cliente.objects.filter(telefone_fixo=telefone_fixo)
        
        if cliente.exists():
            return render(request, "cliente.html", {'nome': nome,'celular':celular,'email':email})
        
        cliente = Cliente.objects.filter(nomeId=nomeId)
        
        if cliente.exists():
            return render(request, "cliente.html", {'nome': nome,'celular':celular,'email':email,'telefone_fixo':telefone_fixo})
        
 #para salvar os dados
        
        client = Cliente(
            nome = nome,
            email = email,
            celular = celular,
            telefone_fixo = telefone_fixo,
            nomeId = nomeId,
            
        )
        client.save()#Sem este comando não salva os dados
        
        lista = Cliente.objects.all()
        context = {
            "lista": lista,
        }
      
        return render(request,"cliente.html",context)
    
        
def agendamento(request):
    if request.method == "GET":
        return render(request,'agendamento.html')
    elif request.method == "POST":
        agend = request.POST.get('agedamento') 
        
    print(agend)
    return HttpResponse('estou em agenda')     
        
        

def area(request):
    return render(request,'area.html')


def area_servicos(request):
    lista = Servicos.objects.all()
    
    context = {
       
        "lista": lista,
    }
    return render(request,'area_servicos.html',context)



def area_clientes(request):
    
    lista = Cliente.objects.all()
    
    context = {
       
        "lista": lista,
    }
    return render(request,'area_clientes.html',context)

 
  
  
    
def servicos(request):
    if request.method == "GET":
        return render(request,'servicos.html')
    elif request.method == "POST":
       
        servicos = request.POST.get('servicos')
        cliente = request.POST.get('cliente')
        modelo = request.POST.get('modelo')
        nomeID = request.POST.get('nomeID')
        computador = request.POST.get("computador")
        
        servico= Servicos.objects.filter(nomeID=nomeID)
        
        if servico.exists():
            return render(request, "servicos.html",{'servicos':servicos,'cliente':cliente,'modelo':modelo,'computador':computador})
        
        
        serv = Servicos(
            
            servicos = servicos,
            cliente = cliente,
            modelo = modelo,
            nomeID = nomeID,
            computador = computador,
            
        )
        serv.save()
        
        lista = Servicos.objects.all()
        
        context = {
            "lista": lista,
        }
       
       
        return render(request,"servicos.html",context)
