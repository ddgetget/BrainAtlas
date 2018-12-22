from django.contrib import admin

# Register your models here.


# ----------------------------站点信息的维护--------------------------------------------------
# admin.site.site_header = 'Turing的个人主页'
# admin.site.site_title = '陕西汉中在线网'
# admin.site.index_title = '北京欢迎你'
admin.site.site_header = '这个是菜单栏的标题'
admin.site.site_title = '浏览器的标题'
admin.site.index_title = '页面的标题'
# --------------------------------------------------------------------------------------------


# 进行后台的注册
from book.models import BookInfo, HeroInfo


# ----------------------------------------切记:两个类的顺序不能颠倒--------------------------------------------------
# 用与关联的下面面这个累
class HeroInfoSatckInline(admin.StackedInline):
    # 需要编辑的对象
    model = HeroInfo
    # 附加编辑的数量
    extra = 1


# Django提供的Admin站点的展示效果可以通过自定义ModelAdmin类来进行控制
class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 2
    list_display = ['id', 'btitle', 'pub_date']

    # 显示字段
    # fields = ['btitle','bpub_date']
    # 这两个不能同时显示
    fieldsets = (
        ('基本', {'fields': ['btitle', 'bpub_date','image']}),
        ('高级', {
            'fields': ['bread', 'bcomment'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )

    # 把上面这个类关联致辞
    inlines = [HeroInfoSatckInline]



# -------------------------------------------Hero-------------------------------------

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hbook', 'read']
    list_filter = ['hbook', 'hgender']
    search_fields = ['hname']
    pass


# 注册只能在后台页面进行显示,如果或要显示admin管理,需要添加该类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
