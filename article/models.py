from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


def categories():
    CATEGORIES = (
        ('1', 'Temel Elektronik'),
        ('2', 'Elektronik Tasarım'),
        ('3', 'Endüstriyel Otomasyon'),
        ('4', 'C Programlama'),
        ('5', 'FPGA-VHDL'),
        ('6', 'PIC'),
        ('0', 'Diğer'),
    )

    return CATEGORIES


class Article(models.Model):
    CATEGORIES = categories()

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=100, verbose_name="Başlık")
    content = RichTextUploadingField(verbose_name="İçerik",
                                     external_plugin_resources=[(
                                         'youtube',
                                         '/static/ckeditor/ckeditor/plugins/youtube/youtube/',
                                         'plugin.js',
                                     )],
                                     )
    preview = models.CharField(blank=True, null=True, max_length=300, verbose_name="Önizleme(Anasayfada Gözükecek Kısım)")
    createdDate = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    mainImage = models.ImageField(blank=True, null=True, verbose_name="Ana Fotoğraf")
    isConfirmed = models.BooleanField(default=False)
    category = models.CharField(max_length=60, default="0", choices=CATEGORIES, verbose_name="Kategori")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createdDate']
