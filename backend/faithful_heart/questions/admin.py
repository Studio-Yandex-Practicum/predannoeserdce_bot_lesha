from django.contrib import admin

from questions.models import FrequentlyAskedQuestion, UniqueQuestion, Category


class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'answer',
        'category',
        'is_relevant'
    )
    list_display_links = ('text', 'answer')
    search_fields = ('text', 'answer')
    list_editable = ('category', 'is_relevant')


class UniqueQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'owner',
        'answer'
    )
    list_display_links = ('text', 'owner', 'answer')
    search_fields = ('text', 'answer')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'value',
        'is_relevant'
    )
    list_editable = ('is_relevant',)


admin.site.register(FrequentlyAskedQuestion, FrequentlyAskedQuestionAdmin)
admin.site.register(UniqueQuestion, UniqueQuestionAdmin)
admin.site.register(Category, CategoryAdmin)
