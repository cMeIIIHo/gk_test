from django.db import models
from django.core.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def children(self):
        return self.menuitem_set.all()

    # # todo: sure?
    # def get_absolute_url(self):
    #     try:
    #         named_url_parts = self.url.split()
    #         url_name = named_url_parts[0]
    #         args = named_url_parts[1:len(named_url_parts)]
    #         return reverse(url_name, args=args)
    #     except NoReverseMatch:
    #         return self.url

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []
