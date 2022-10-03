from django.contrib import admin

# Register your models here.
from movie.models import Movie, Show, Promotion
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'alias', 'movie_code', 'expire_date', 'poster_image')
    list_display=['title', 'alias', 'movie_code', 'expire_date', 'poster_image']

admin.site.register(Movie, MovieAdmin)


class ShowAdmin(admin.ModelAdmin):
    fields = ('movie', 'start_time', 'end_time', 'seat_row', 'amount')
    list_display=['movie', 'start_time', 'end_time', 'seat_row', 'amount']

admin.site.register(Show, ShowAdmin)


class PromotionAdmin(admin.ModelAdmin):
    fields = ('movie', 'promo_code', 'off_amount', 'off_percent', 'promo_type', 'min_amount')
    list_display=['movie', 'promo_code', 'off_amount', 'off_percent', 'promo_type', 'min_amount']

admin.site.register(Promotion, PromotionAdmin)