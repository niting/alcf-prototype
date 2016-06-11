from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail_embed_videos.edit_handlers import EmbedVideoChooserPanel

""" Blocks defining the elements on the pages """
class CarouselBlock(blocks.StructBlock):
    """ Single Carousel slide"""
    image = ImageChooserBlock() 
    caption = blocks.CharBlock()
    text = blocks.RichTextBlock()
    link = blocks.PageChooserBlock()

    class Meta:
        template = 'home/carousel_block.html'

class Carousel(blocks.ListBlock): 
    """ Multiple Carousel blocks """
    carousel_block = CarouselBlock()

class PageCardBlock(blocks.StructBlock):
    """ Represents the card for a page. Has a link, text and some """
    """ image. """
    image = ImageChooserBlock()
    link = blocks.PageChooserBlock()
    caption = blocks.CharBlock()
    text = blocks.RichTextBlock()

""" Different types of pages """
class MainPage(Page):
    """ Main pages that branch out from the HomePage """
    """ Care, Connect, Events, Give, Learn, Visit, Volunteer """
    subpage_types = ['InfoPage']

class InfoPage(Page): 
    """ These are pages that branch out from the MainPage """
    """ These are leaf pages and should not branch out further """
    subpage_types = []

class HomePage(Page):
    """ Landing page for all users """
    subpage_types = ['MainPage']
    showcase_video = models.ForeignKey(
            'wagtail_embed_videos.EmbedVideo',
            verbose_name="Video",
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
    )
    showcase_box = RichTextField(null=True, blank=True) 

    overlay_text = models.CharField(max_length = 250)
    image_carousel = StreamField([('carousel', CarouselBlock())])
    page_card_carousel = StreamField([('page_card_carousel',
        blocks.ListBlock(PageCardBlock()))], null=True)
    content_panels = Page.content_panels + [
            EmbedVideoChooserPanel('showcase_video'),
            FieldPanel('showcase_box'),
            FieldPanel('overlay_text'),
            StreamFieldPanel('image_carousel'),
            StreamFieldPanel('page_card_carousel'),
    ]

