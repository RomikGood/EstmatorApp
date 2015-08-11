from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from est_client.models import Client


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return 'Category: {}'.format(self.name)


@python_2_unicode_compatible
class Product(models.Model):
    # Inputs
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=256)

    # Piece Multipliers
    mins_piece = models.IntegerField()
    mult_dollies = models.IntegerField()
    m_cart = models.IntegerField()
    l_cart = models.IntegerField()
    p_cart = models.IntegerField()
    s_pack = models.IntegerField()

    def __str__(self):
        return 'Product: {}'.format(self.name)


@python_2_unicode_compatible
class Quote(models.Model):
    user = models.ForeignKey(User, related_name='user')
    client = models.ForeignKey(Client, related_name='client')
    name = models.CharField(max_length=256)
    date = models.DateField(auto_now_add=True)
    sub_total = models.IntegerField(blank=True, null=True)
    products = models.ManyToManyField(
        Product,
        related_name='products',
        through='ProductInQuote',
        blank=True
    )
    loc_vars = models.ManyToManyField(
        Product,
        related_name='loc_vars',
        through='LocVars',
        blank=True
    )
    global_mods = models.ManyToManyField(
        'GlobalVars',
        related_name='globals',
        through='GlobalMods',
        blank=True
    )

    def __str__(self):
        return 'Quote: {}'.format(self.name)


class GlobalVars(models.Model):
    # Location multipliers
    street_load = models.FloatField()
    midrise_elev_std = models.FloatField()
    midrise_elv_frt = models.FloatField()
    highrise = models.FloatField()
    stairs = models.FloatField()
    lng_psh = models.FloatField()


class ProductInQuote(models.Model):
    quote = models.ForeignKey('Quote', null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    counts = models.IntegerField(blank=True, null=True)

    # Outputs
    @property
    def total_mins(self):
        return self.counts * self.mins_piece

    @property
    def dollies(self):
        return self.counts * self.mult_dollies

    @property
    def machine_carts(self):
        return self.counts * self.m_cart

    @property
    def library_carts(self):
        return self.counts * self.l_cart

    @property
    def panel_carts(self):
        return self.counts * self.p_cart

    @property
    def speed_packs(self):
        return self.counts * self.s_pack


class LocVars(models.Model):
    quote = models.ForeignKey(Quote, null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True)
    # Origin variables
    org_street_load = models.BooleanField()
    org_midrise_elev_std = models.BooleanField()
    org_midrise_elv_frt = models.BooleanField()
    org_highrise = models.BooleanField()
    org_stairs = models.BooleanField()
    org_lng_psh = models.BooleanField()
    # Destination variables
    dest_street_load = models.BooleanField()
    dest_midrise_elev_std = models.BooleanField()
    dest_midrise_elv_frt = models.BooleanField()
    dest_highrise = models.BooleanField()
    dest_stairs = models.BooleanField()
    dest_lng_psh = models.BooleanField()


class GlobalMods(models.Model):
    quote = models.ForeignKey(Quote, null=True, blank=True)
    glob_vars = models.ForeignKey(GlobalVars, null=True, blank=True)

    @property
    def get_street_load(self):
        return self.quote.sub_total * self.glob_vars.street_load

    @property
    def get_midrise_elev_std(self):
        return self.quote.sub_total * self.glob_vars.midrise_elev_std

    @property
    def get_midrist_elev_frt(self):
        return self.quote.sub_total * self.glob_vars.midrist_elev_frt

    @property
    def get_highrise(self):
        return self.quote.sub_total * self.glob_vars.highrise

    @property
    def get_stairs(self):
        return self.quote.sub_total * self.glob_vars.stairs

    @property
    def get_long_push(self):
        return self.quote.sub_total * self.glob_vars.long_push
