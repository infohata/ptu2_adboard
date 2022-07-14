from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(_("name"), max_length=63, db_index=True)
    priority = models.IntegerField(_("priority"), default=0, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ('-priority', 'name', )


ADPOST_STATUS = Choices(
    (0, 'new', _('new')),
    (10, 'active', _('active')),
    (20, 'reserved', _('reserved')),
    (30, 'sold', _('sold')),
    (90, 'canceled', _('canceled')),
    (99, 'removed', _('removed')),
)


class AdPost(models.Model):
    title = models.CharField(_("title"), max_length=127, db_index=True)
    description = HTMLField(_("description"), max_length=8190)
    category = models.ManyToManyField(
        Category, 
        verbose_name=_("categories"), 
        related_name="ad_posts",
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True)
    owner = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("owner"), 
        on_delete=models.CASCADE,
        related_name="ad_posts",
    )
    buyer = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("buyer"), 
        on_delete=models.CASCADE,
        related_name="purchases",
        blank=True, null=True,
    )
    status = models.PositiveSmallIntegerField(
        _("status"),
        choices=ADPOST_STATUS,
        default=ADPOST_STATUS.new,
        db_index=True,
    )
    promoted = models.BooleanField(_("promoted"), default=False)

    def __str__(self):
        return _('{} by {} from {}').format(self.title, str(self.owner), str(self.created_at))
    
    class Meta:
        verbose_name = 'advertisement post'
        verbose_name_plural = 'advertisement posts'
        ordering = ('-promoted', '-created_at', )

