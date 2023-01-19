from django.contrib import admin
from .models import Product, Review
from django.utils import timezone

#? product'ların review'larını altında görmek için;
#? TabularInline'dan inherit ederek custom bir Review model yazıyoruz
# class ReviewInline(admin.StackedInline): #StackedInline farklı bir görünüm aynı iş
class ReviewInline(admin.TabularInline):
    model = Review
    
    #? mesela 3 yorum var, extra 1 tane boş gelsin yorum yazabilmek için,
    extra = 1
    
    #? kapalı gelsin, SHOW ile açılsın,
    classes = ('collapse',)
    
    #? min 3 tane, max 20 tane göster
    # min_num = 3
    # max_num = 20


#? admin panelde customize için ModelAdmin inherit edilmeli
class ProductAdmin(admin.ModelAdmin):
    #? hangi field'lar görünsün
    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews")
    
    #? edit edilmesini istediklerimiz (true/false gibi)
    list_editable = ( "is_in_stock", )
    
    #? link olsun, üzerine basınca objeye gitsin, default name
    #? link olan editable olmaz, birden fazla link olabilir.
    # list_display_links = ("create_date", )
    
    #? filitreleme için
    list_filter = ("is_in_stock", "create_date")
    
    #? sıralama (ilk açılış için) ("-name",) eksi de olabilir,
    ordering = ("-update_date",)
    
    #? search box açılıyor,
    search_fields = ("name",)
    
    #? bir field'ı başka bir field'tan üretme
    #? bu örnekte slug'ı name'den üretiyor.
    prepopulated_fields = {'slug' : ('name',)}   # when adding product in admin site
    
    #? pagination, default 100
    list_per_page = 25
    
    #? yıl / ay / tarih ayrı ayrı seçilebiliyor.
    date_hierarchy = "update_date"
    
    #? objenin içine gelince hangi fieldlar görünsün
    # fields = (('name', 'slug'), 'description', "is_in_stock") #fieldset kullandığımız zaman bunu kullanamayız
    
    #todo, bunu sonradan ekledik, çalışması için bu classın üstüne yazdık.
    #todo, artık her ürünün altındaki yorumları görebilir, silebilir, yeni ekleyebiliriz.
    inlines = (ReviewInline,)
    
    #? her obje, yani her product nasıl görünsün,
    #? burada ikiye ayırmış, birinci bölüme isim vermemiş None, ikinciye Optionals Settings yazmış
    #? classes, collapse-kapalı gelir, SHOW yapılır, wide-açık gelir
    #? description, açıklma yazılır.
    fieldsets = (
    (None, {
        "fields": (
            ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
        ),
        # 'classes': ('wide', 'extrapretty'), wide or collapse
    }),
    ('Optionals Settings', {
        "classes" : ("collapse", ),
        "fields" : ("description",),
        'description' : "You can use this section for optionals settings"
    })
    )
    
    #? default sadece delete action vardı, yeni yazdık ve actions içine ekledik.
    actions = ("is_in_stock", )
    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
    #? işlem sonunda nasıl bir uyarı/mesaj yazsın
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
    #? action kutusunda ismi nasıl görünsün, bunu yazmazsak fonksiyon ismi görünür, is_in_stock olarak.
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'


    #? actions kullanmadan custum metod yazabilirim
    #? şimdiki zamandan, eklendiği zamanı çıkarıp kaç gün önce eklendiğini bulabilirim
    #? bunu görmek için fields içine eklemek gerekli.
    #? bunun aynısını model.py içinde de yapabiliriz.
    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days
    #? ismini değiştirmek istersek;
    added_days_ago.short_description = 'kaç gün önce eklendi'
    
    #! obj veya product aynı şey ikiside yazılabilir,
    
    # bunu modelde yazdık onun için yorumda, burada da yazılabilirdi,
    # def how_many_reviews(self, obj):
    #     count = obj.reviews.count()
    #     return count


class ReviewAdmin(admin.ModelAdmin):
    #? list_display içine metod'da yazabiliriz, __str__ veya kendi yazdığımız metodlar,
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    
    #?id'ye göre seçim yaptırıyor,
    raw_id_fields = ('product',)

# yeni oluşturulan customAdmin registere eklenir,
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)

# tab/sekmedeki isim 
admin.site.site_title = "Clarusway Title"

# başlıktaki isim
admin.site.site_header = "Clarusway Admin Portal"  

# Home'daki isim
admin.site.index_title = "Welcome to Clarusway Admin Portal"