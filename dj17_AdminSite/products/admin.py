from django.contrib import admin
from .models import Product, Review, Category
from django.utils import timezone
#? eklenen fotoğraflar, güvenli demek,
from django.utils.safestring import mark_safe
#? filter import
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter
#? date range filter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

#? import-export 
from products.resources import ReviewResource
from import_export.admin import ImportExportModelAdmin

#? product'ların review'larını altında görmek için;
#? TabularInline'dan inherit ederek custom bir Review model yazıyoruz
# class ReviewInline(admin.StackedInline): #* StackedInline farklı bir görünüm aynı iş
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
    # list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews")
    
    #? hangi field'lar görünsün (sonradan image'da eklendi)
    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews", "bring_img_to_list")
    
    #? edit edilmesini istediklerimiz (true/false gibi)
    list_editable = ( "is_in_stock", )
    
    #? link olsun, üzerine basınca objeye gitsin, default name
    #? link olan editable olmaz, birden fazla link olabilir.
    # list_display_links = ("create_date", )
    
    #? filitreleme için (django kendisi)
    # list_filter = ("is_in_stock", "create_date")
    
    #? filitreleme için (rangefilter ile)
    list_filter = ("is_in_stock", ("create_date", DateTimeRangeFilter)) 
    
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
        # "fields" : ("description",),
        #? sonradan eklenen field ilave edildi
        # "fields" : ("description", "categories"),
        #? sonradan eklenen image field ilave edildi
        "fields" : ("description", "categories", "product_img", "bring_image"),
        'description' : "You can use this section for optionals settings"
    })
    )
    
    #? category seçimini daha görsel hale getiriyor, yatay/dikey
    filter_horizontal = ("categories", )
    # filter_vertical = ("categories", )
    
    #? IMAGE için readonly_fields eklemek lazım ;
    readonly_fields = ("bring_image",)
    
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
    
    def bring_image(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=400 height=400></img>")
        return mark_safe(f"<h3>{obj.name} has not image </h3>")
    
    #? listede image gösterme:
    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")

    bring_img_to_list.short_description = "product_image"

#? import-export ekleyince inherit değişiyor
class ReviewAdmin(ImportExportModelAdmin):
# class ReviewAdmin(admin.ModelAdmin):
    #? list_display içine metod'da yazabiliriz, __str__ veya kendi yazdığımız metodlar,
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    
    #?id'ye göre seçim yaptırıyor,
    raw_id_fields = ('product',)
    
    #? djangonun kendi filteri
    # list_filter = ('product',)
    
    #? django_admin_listfilter_dropdown ile;
    list_filter = (
        ('product', RelatedDropdownFilter),
    )
    
    resource_class = ReviewResource

# yeni oluşturulan customAdmin registere eklenir,
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)

#! tab/sekmedeki isim 
admin.site.site_title = "Clarusway Title"

#! başlıktaki isim
admin.site.site_header = "Clarusway Admin Portal"  

#! Home'daki isim
admin.site.index_title = "Welcome to Clarusway Admin Portal"