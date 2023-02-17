from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages


#? Class Based imports
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)


#! -------------------------
#! Function Based View
#! -------------------------

#* todo'ları listelemek/görüntülemek için,
def todo_list(request):
    #? bütün todo'ları görüntüleyebilmek için
    #? Todo modeldeki bütün objeleri alıp değişkene atadık,
    todos = Todo.objects.all()
    #? gelen data bir queryset'tir.
    
    #? bu student değişkeni context içinde value olacak şekilde yeniden tanımladık,
    context = {
        "todos" : todos
    }
    
    #? ve context içindeki herşeyi kullanabilmek için list.html içine aktardık.
    return render(request, "list.html", context)

#* yeni bir todo oluşturmak/create etmek için; (SİNAN HOCANIN YAPTIĞI)
#? burada serializer görevine yapacak form yapısını kullanıyoruz,
#? app içinde forms.py isimli bir dosya oluşturuyoruz.
def todo_add1(request):
    #? formu alıp içine istek yapılan datayı koyuyoruz,
    #? None yazmazsak html sayfasında 'this field required vs.' gibi uyarı çıkıyor.
    form=TodoForm(request.POST or None)
    
    #? eğer gelen data valid ise kayıt et
    if form.is_valid():
        form.save()
        
        #? başarılı bir kayıt yapılmış ise mesaj dönsün,
        messages.success(request,'New Todo Successfully ADD')
        
    #? sonra işlem bitince list sayfasına yönlendir.
        return redirect('todo_listfb')

    #? context yapısı kurmadan direk içine key/value olarak yazabiliriz.
    return render(request,'add.html',{'form':form})


#* yeni bir todo oluşturmak/create etmek için; (HENRY HOCANIN YAPTIĞI, student örneğinden)
def todo_add2(request):
    # 1-context içine form'dan gelen data'yı koymak için onu bir değişkene atıyoruz,
    form = TodoForm()
    
    if request.method == 'POST':
        
        #? request.POST ile forma girilen dataları yakalayabiliyoruz,
        print("POST :", request.POST)
        # POST : <QueryDict: {'csrfmiddlewaretoken': ['18KNgiCUQVmlx5YUXCMdWXy4eRRO5F8KKCwHaDdZmcXaBqs1PNC20rxspQqlTE3o'], 'title':['henry'], 'description': ['context'], 'priority': ['2'], 'status': ['p']}>
        
        # 2-data boş gitmemesi için içine, yukarıda örnek çıktıları verilen dataları ekliyoruz.
        form = TodoForm(request.POST)
        
        # eğer gelen datalar uygunsa kayıt et.
        if form.is_valid():
            form.save()
            
            #? artık form sayfasında kalmasın, save olduktan sonra başka yere yönlendirilsin;
            #? redirect için url tarafında belittiğimiz ismi yazmak daha kullanışlı redirect("name")
            #? urls.py içinde name ile ilgili açıklama notu var.
            return redirect("todo_listfb") # name ile yazılması
            # return redirect("/list") # path ile yazılması
    
    
    # 3-değişkene atanan TodoForm()'u kullanabilmek için context içine value olarak atıyoruz,
    context = {
        "form" : form
    }
    
    return render(request, "add.html", context) 
    # return render(request, "add.html", {"form" : form})


#* bir todo bilgilerine bakmak için;
#? tek bir todoya bakmak için id kullanmak gerekli,
def todo_detail(request, pk):
    #? sadece id'si benim yazdığım id olan todo gelsin
    todo = Todo.objects.get(id=pk)

    return render(request,'detail.html',{"todo":todo})

#* var olan bir todo güncellemek/update etmek için;
#? tek bir todo update edileceği için id/pk kullanmak gerekli,
# yukarıdaki add1 ile çok benzer, sadece instance=student eklemek gerekiyor.
def todo_update(request, pk):
    #? sadece id'si benim yazdığım id olan todo gelsin
    todo = Todo.objects.get(id=pk)
    
    #? form boş olarak gelmesin, yukarıdaki todo bilgileri ile gelsin;
    form=TodoForm(instance=todo)
    if request.method == "POST":
        
        # data boş gitmemesi için içine verileri ekliyoruz,
        # instance=todo bunu eklemezsek yeni bir todo create eder,
        # ekleyince değikliğe göre update ediyor.
        form=TodoForm(request.POST, instance=todo)
        
        # form uygunsa kayıt et ve yönlendir.
        if form.is_valid():
            form.save()
            return redirect('todo_listfb')
    return render(request,'update.html',{'form':form, "todo":todo})

#* var olan bir todo'yu silmek için;
def todo_delete(request, pk):
    #? sadece id'si benim yazdığım id olan todo gelsin ve silsin
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo_listfb')


#! -------------------------
#! Class Based View
#! -------------------------


#? CBV kullanırken verilecek isim hangi viewdan inherit edilecekse onunla aynı olmak zorunda
#? AppnameListView, AppnameCreateView vs..

#? App içindeki templates klasörüne app ile aynı isimde bir klasör daha eklemek gerekli,
#? templates/todo şeklinde, ve artık bütün html dosyaları burada olmak zorunda,

#? FBV kullanırken context ile değişken gibi bütün todo'ları todos ismi ile template aktardık,
#? fakat CBV context yapısı yok, onun yerine "object_list" kullanıyoruz,
#? bu isim sabit bizim bütün todo'lar bunun içinde ve CBV yapısı ile otomatikmen template aktarılıyor,
#? biz ilave birşey yapmadan template tarafında "object_list" ile kullanıyoruz,


#? template için kullanılacak isimlerde mutlaka CBV bizden istediği gibi verilmeli,
#? template_name_suffix = "_list", hangi view hangi suffix belirtmişse öyle yazmak gerekiyor, todo_list.html gibi
#!  Not :: isterseniz class larda  template_name = 'todo/todo_delete.html' ile django nun isteği dışına çıkabilirsiniz



#* listemele için sadece kullanılacak model yazmak yeterli
#* context olmadığından, kullanılacak template içinde "object_list" kullanmak zorunlu
#! template_name_suffix = "_list",
class TodoListView(ListView):
    model=Todo
    #! template_name = 'todo/mytodolist.html' vs yazılarak default _list harici başka isim yazılabilir.



#* yeni bir todo eklemek için hangi model kullanılacak,
#* hangi form kullanılarak todo oluşturulacak,
#* redirect yerine success_url ile yönlendirme yapılacak,
#! template_name_suffix = "_form",

class TodoCreateView(CreateView):
    model=Todo
    form_class=TodoForm
    success_url=reverse_lazy('todo_listcb')
    



#* update için hangi model kullanılacak,
#* hangi form kullanılarak todo update edilecek,
#* redirect yerine success_url ile yönlendirme yapılacak,
#! template_name_suffix = "_form",
    
class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo_listcb')



#* hangi model kullanılacak,
#* silme işleminden sonra redirect yerine success_url ile yönlendirme yapılacak,
#! template_name_suffix = "_confirm_delete"
class TodoDeleteView(DeleteView):
    model=Todo
    success_url = reverse_lazy('todo_listcb')




#* detail için hangi model kullanılacak,
#! template_name_suffix = "_detail",
class TodoDetailView(DetailView):
    model = Todo
        
