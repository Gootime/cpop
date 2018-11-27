from django.contrib import admin
from .models import Article,Category,Commentaire

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','date','slug')
    list_filter = ('author','category')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('title','content')
    prepopulated_fields ={'slug':('title',),}
    fieldsets = (
        ('Général',{
            'classes': ['collapse',],
            'fields': ('title','slug','category','thumbnail','adress')
        }),
        ('Contenu de l\'article',{
            'description': 'le formulaire accepte les balise HTML, utilisez-les à bon escient !',
            'fields': ('content',),

        })
    )

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('pseudo','email','contenu','article_id')
    list_filter = ('pseudo','article_id')

admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Commentaire,CommentaireAdmin)
