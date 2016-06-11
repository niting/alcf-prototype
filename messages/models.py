from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore import blocks

# App containing the last few sermons in the Church
class MessageBlock(blocks.StructBlock):
    """ Defines a message for the sermons page """
    title = blocks.CharBlock()
    # TODO(niting): Make speaker a foreign key so that 
    # we can check all messages by a speaker.
    date = blocks.DateBlock()
    speaker = blocks.CharBlock()
    mp3_link = blocks.URLBlock()
    video_link = blocks.URLBlock()
    pdf_link = blocks.URLBlock()
    # Image might only be required when show casing.
    image = blocks.ImageChooserBlock(required=False)

