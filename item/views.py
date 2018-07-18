from django.shortcuts import render, redirect, get_list_or_404
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, ListView, DetailView, FormView
from item.models import Item
from item.forms import SampleForm, InputForm, InputForm2, InputForm3, ItemForm

def welcome(request):
    return HttpResponse('welcome')

def doget_execute(request, param1):
    return HttpResponse(param1)

def showtemp1(request):
    c = {
         'key1' : 'hello everyone',
    }
    return render(request, 'template1.html', c)

def showtemp1sc(request):
    return render(request, 'template1.html', {'key1': 'hello everyone'})

def showredirect(request):
    return redirect('/show')

def showredirect2(request):
    return redirect('wel')

def showredirect3(request):
    return render(request, 'templateform.html')

def showchild(request):
    return render(request, 'child.html')

@csrf_protect
def dopost_execute(request):
    param = request.POST['message']
    return render(request, 'result.html', {'message': param})

def show_input(request):
    return render(request, 'input.html')

def show_inputerr(request):
    return render(request, 'input_tokenerror.html')

def csrf_failure(request, reason=''):
    c = {'message': 'トークンエラー'}
    return render(request, '403_csrf.html', c)

# TemplateView
class SampleTemplateView(TemplateView):
    template_name = 'html/index.html'

# ListView_1
class ItemModelListView(ListView):
    template_name = 'item_list.html'
    model = Item
    context_object_name = 'items'

# ListView_2
class ItemQueryListView(ListView):
    template_name = 'item_list.html'
    queryset = Item.objects.all().order_by('id')
    context_object_name = 'items'

class ItemNameListView(ListView):
    template_name = 'item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return get_list_or_404(Item, name=self.args[0])

# DetailView
class ItemDetailView(DetailView):
    template_name = 'item_detail.html'
    model = Item
    context_object_name = 'item'

def dopost_view(request):
    form = SampleForm()
    return render(request, 'template.html', {'form': form})

def confirm(request):
#     form = InputForm(request.POST)
#     form = InputForm2(request.POST)
    form = InputForm3(request.POST)
#     form = InputFormValid(request.POST)
    if not form.is_valid():
        return render(request, 'form_param.html', {'form': form})
    msg = form.cleaned_data['param1']
    return render(request, 'form_param.html', {'form': form, 'message': msg})

class InputFormView(FormView):
    form_class = InputForm
    template_name = 'input_form_v.html'
    success_url = '/item/thanks'

class ItemFormView(FormView):
    form_class = ItemForm
    template_name = 'item_form.html'

    def form_valid(self, form):
        form.save()
        return redirect('item:thanks')