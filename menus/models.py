from django.db import models
from django.core.urlresolvers import reverse
from django.core.urlresolvers import NoReverseMatch
from django.http import Http404


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    explicit_url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    named_url = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if self.named_url:
            named_url_parts = self.named_url.split()
            url_name = named_url_parts[0]
            params = named_url_parts[1:len(named_url_parts)]
            reversed_named_url = reverse(url_name, args=params)
            if self.explicit_url:
                if self.explicit_url != reversed_named_url:
                    raise Http404('explicit_url does not match named_url')
            else:
                self.explicit_url = reversed_named_url
        super(MenuItem, self).save(*args, **kwargs)

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
