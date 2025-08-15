# Estudando Django

Este repositório tem como objetivo documentar minha jornada de aprendizado com o framework **Django**. Iniciei pelo curso gratuito oferecido pela [W3Schools](https://www.w3schools.com/django/index.php) o qual será **Projeto Piloto** e sevirá de comparação para os demais projetos.

Outros projetos aqui documentados fazem parte do curso **Django Master** oferecido pela [PycodeBr](https://pycodebr.com.br/) e do aprendizado prático baseado na série de lives do [Canal do Youtube da Pycode] (https://www.youtube.com/@pycodebr).

---

## Sobre o Django

Django é um framework web, escrito em **Python**, **gratuito** e **open source**. Ele facilita a criação de sites dinâmicos, robustos e escaláveis com menos código e mais organização.

Django foi desenvolvido em 2003 por uma equipe do jornal **Lawrence Journal-World**, com o objetivo de agilizar a criação de sistemas para atender a prazos apertados. Foi lançado publicamente em **julho de 2005**, e desde então tem sido mantido por uma comunidade ativa.

---

## Como o Django Funciona?

Django segue o padrão de arquitetura **MVT (Model - View - Template)**:

- **Model**: representa os dados da aplicação, normalmente ligados ao banco de dados.
- **View**: é o controlador da lógica — recebe as requisições, processa os dados e retorna as respostas.
- **Template**: é a camada de apresentação — geralmente arquivos HTML com tags do Django para exibir os dados dinamicamente.

Esse fluxo permite organizar e separar bem as responsabilidades dentro de uma aplicação web.

---

## Estrutura deste Repositório

Este repositório conterá:

- ✅ Referência aos projetos desenvolvidos (com links)
- ✅ Tópicos estudados e suas aplicações
- ✅ Anotações e reflexões pessoais durante o aprendizado

## Projetos Criados

| Projeto         | Descrição                                               | Link              |
|-----------------|---------------------------------------------------------|-------------------|
| Projeto Piloto  | Primeiro projeto Django seguindo passo a passo do curso| [W3Schools](./W3Schools/) |
| Projeto Carros | Primeiro projeto do curso Django Master. Sem nenhuma alteração| [Carros](https://github.com/brunocnog/carros/) |
| Parking Service | Sistema e API de Estacionamento com Python e Django| [Parking-Spot](./Parking-Spot/) |

---

## Próximos Passos

À medida que os projetos forem finalizados, novos repositórios serão criados com os exemplos práticos e documentações. Todos estarão linkados aqui, formando um portfólio de projetos Django com evolução gradual.

---

## Comparação entre `views.py` – Projeto Piloto (W3Schools) vs. Projeto **Carros** (Django Master)

Durante os estudos com Django, percebi diferenças significativas na abordagem dos arquivos `views.py` entre o **projeto piloto da W3Schools** e o **primeiro projeto do curso Django Master** (Projeto “Carros”, app `accounts`).

A principal diferença é o **método de retorno da resposta HTTP**:

* **W3Schools**: usa explicitamente `HttpResponse` combinado com `loader.get_template()` para carregar e renderizar templates.
* **Projeto Carros**: utiliza `render()`, que é um *atalho* (helper function) do Django para carregar, renderizar e retornar o template em uma única função.

---

### Código para comparação

#### **`views.py` – Projeto Piloto (W3Schools)**

```python
# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
```

---

#### **`views.py` – Projeto Carros (Django Master – app accounts)**

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('cars_list')
```

---

### Principais diferenças

1. **Forma de renderizar templates**

   * *W3Schools*:

     ```python
     template = loader.get_template('template.html')
     return HttpResponse(template.render(context, request))
     ```

     Aqui, o carregamento e a renderização são feitos manualmente, retornando explicitamente um objeto `HttpResponse`.
     Essa abordagem é mais “verbosa”, mas deixa claro cada passo do processo.

   * *Projeto Carros*:

     ```python
     return render(request, 'template.html', context)
     ```

     O `render()` faz internamente:

     * Carregar o template
     * Renderizar com o contexto
     * Retornar `HttpResponse`
       É mais simples, mais comum em projetos reais e reduz código repetitivo.

2. **Contexto e Objetos**

   * No projeto da W3Schools, o contexto é geralmente passado como um **dicionário simples** obtido via consultas ORM (ex.: `.values()` ou `.get()`).
   * No projeto Carros, o contexto geralmente vem de **forms Django** (`UserCreationForm`, `AuthenticationForm`), passando dados já estruturados para o template.

3. **Foco e propósito**

   * O projeto W3Schools tem **ênfase didática** na manipulação de templates e dados simples do banco.
   * O projeto Carros já trabalha com **autenticação, permissões e redirecionamentos**, explorando recursos do `django.contrib.auth`.

4. **Fluxo de requisição/resposta**

   * No W3Schools: foco em **listar e detalhar dados** (`members`, `details`), tudo retornado diretamente ao usuário.
   * No Carros: foco em **processamento de formulários e controle de sessão**, usando `redirect()` para mudar a rota após ações de login, registro ou logout.

---

**Conclusão:**
Ambos os métodos (`HttpResponse` + `loader.get_template()` e `render()`) funcionam perfeitamente no Django.

* A abordagem da W3Schools é mais **manual** e ótima para aprender como o Django processa requisições e templates “por baixo dos panos”.
* A abordagem do Projeto Carros é mais **prática e idiomática**, refletindo como a maioria dos projetos Django são escritos no mundo real.

