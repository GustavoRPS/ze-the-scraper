# -*- coding: utf-8 -*-

import six
from scrapy import Field
from scrapy.loader.processors import TakeFirst, MapCompose
from ze.items import CreativeWorkItem
from ze.processors.article import ArticleProcessor
from ze.processors.common import CommonProcessor
from ze.processors.html import CleanHTML

class ArticleItem(CreativeWorkItem):
    
    def __init__(self, *args, **kwargs):
        self._values = {}
        # TODO: Refactor this!
        self.__class__.__name__ = 'article'
        if args or kwargs:  # avoid creating dict for most common case
            for k, v in six.iteritems(dict(*args, **kwargs)):
                self[k] = v

    articleBody = Field(
        input_processor=MapCompose(
            CleanHTML(),
        ),
        output_processor=TakeFirst(),
    )
    articleSection = Field()
    pageEnd = Field()
    pageStart = Field()
    pagination = Field()
    wordCount = Field()


class NewsArticleItem(ArticleItem):

    dateline = Field()
    printColumn = Field()
    printEdition = Field()
    printPage = Field()
    printSection = Field()