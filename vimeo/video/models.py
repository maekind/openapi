
from django.db import models
from django.utils.translation import gettext_lazy as _


class Video(models.Model):
    """ Class to handle basic video information """
    id = models.BigIntegerField(primary_key=True, blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    duration = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    fps = models.IntegerField(default=0)


class Thumb(models.Model):
    """ This class handles video thumbs. One video could have many thumbs. """
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    height = models.CharField(max_length=10, blank=True, null=True)
    url = models.URLField(max_length=256, blank=True, null=True)


class Owner(models.Model):
    """ This class handles video owner information """

    class Accounts(models.TextChoices):
        """ This class implements the accounts type field """
        BASIC = 'basic', _('Basic')
        BUSINESS = 'business', _('Business')
        LIVE_BUSINESS = 'live business', _('Live business')
        LIVE_PREMIUM = 'live premium', _('Live premium')
        LIVE_PRO = 'live pro', _('Live pro')
        PLUS = 'plus', _('Plus')
        PRO = 'pro', _('Pro')
        PRO_UNLIMITED = 'pro unlimited', _('Pro unlimited')
        PRODUCER = 'producer', _('Producer')

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    id = models.BigIntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.URLField(max_length=1024, blank=True, null=True)
    image_max = models.URLField(max_length=1024, blank=True, null=True)
    url = models.URLField(max_length=256, blank=True, null=True)
    account_type = models.CharField(max_length=100, choices=Accounts.choices,
                                    default=Accounts.BASIC)


class Seo(models.Model):
    """ This class handles SEO information about the video """
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(blank=True, null=True)
    embeded_url = models.URLField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, default='')
    thumbnail = models.URLField(max_length=1024, blank=True, null=True)


class Quality(models.Model):
    """ This class handles video quality fields. One video could have several many qualities. """
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    quality = models.CharField(max_length=10, blank=False, null=False)
    fps = models.IntegerField(default=0)
    url = models.URLField(max_length=256, blank=True, null=True)
    mime_type = models.CharField(max_length=20, blank=False, null=False)
