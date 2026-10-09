from django.db import models

class SiteConfiguration(models.Model):
    name = models.CharField(max_length=100, default="Olive Cafe")
    logo = models.ImageField(upload_to='site_config/', blank=True, null=True, help_text="Upload a logo to replace the text in the top navigation")

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Enforce singleton
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class InstagramPost(models.Model):
    url = models.URLField(max_length=500, help_text="Paste the full Instagram post link here (e.g. https://www.instagram.com/p/C_abc123/)", unique=True)
    is_active = models.BooleanField(default=True, help_text="Check to show this post on the homepage")
    order = models.IntegerField(default=0, help_text="Used to order the posts on the homepage (lower number comes first)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Instagram Post"
        verbose_name_plural = "Instagram Posts"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.url

