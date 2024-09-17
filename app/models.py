import uuid
from itertools import chain

from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class BaseManager(models.Manager):
    pass


class BaseModel(models.Model):
    """Parent model for all models in the project."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BaseManager()

    class Meta:
        abstract = True
        ordering = [
            "-updated_at",
        ]

    def to_dict(self, exclude=None, include=None):
        """Custom implementation of Django's model_to_dict()."""

        opts = self._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            if exclude and f.name in exclude:
                continue
            data[f.name] = f.value_from_object(self)
        for f in opts.many_to_many:
            if exclude and f.name in exclude:
                continue
            data[f.name] = [i.to_dict() for i in f.value_from_object(self)]
        if include:
            for f in include:
                data[f] = getattr(self, f)
        return data


class Client(TenantMixin, BaseModel):
    name = models.CharField(max_length=250)


class Domain(DomainMixin, BaseModel):
    pass


class Institution(BaseModel):
    name = models.CharField(max_length=250, unique=True)
    domain = models.OneToOneField(
        Domain, on_delete=models.CASCADE, null=True, blank=True
    )
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    county = models.ForeignKey(
        "County",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="county_institutions",
    )
    sub_county = models.ForeignKey(
        "SubCounty",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sub_county_institutions",
    )
    ward = models.ForeignKey(
        "Ward",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="ward_institutions",
    )

    def __str__(self) -> str:
        return f"{self.name}"


class County(BaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Counties"


class SubCounty(BaseModel):
    county = models.ForeignKey(
        County,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subcounties",
    )
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = "Sub Counties"
        unique_together = (("county", "name"),)


class Ward(BaseModel):
    sub_county = models.ForeignKey(
        SubCounty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wards",
    )
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        unique_together = (("sub_county", "name"),)
