import catalog.models

from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin


admin.site.register(catalog.models.Tag)
admin.site.register(catalog.models.Category)


class AlbumImageAdmin(admin.StackedInline):
    model = catalog.models.PhotoForGallery
    extra = 2


class ImageAdmin(admin.TabularInline):
    model = catalog.models.ImageModel
    max_num = 1


@admin.register(catalog.models.Item)
class ItemAdmin(SummernoteModelAdmin):
    list_display = (
        catalog.models.Item.id.field.name,
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
        catalog.models.ImageModel.image_tmb,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)
    inlines = [AlbumImageAdmin, ImageAdmin]
    summernote_fields = (catalog.models.Item.text.field.name,)
