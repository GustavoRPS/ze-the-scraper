# -*- coding: utf-8 -*-
from . import ZeSpider
__all__ = ['ElPaisBrasilSpider']

class ElPaisBrasilSpider(ZeSpider):

    name = 'elpais'
    allowed_domains = ['brasil.elpais.com']
    items_refs = [{
        "spider_name":name,
        "item": "ze.items.creativework.ArticleItem",
        "fields": {
            "name": {
                "selectors": {
                    "css": [
                        "meta[property='og:title']::attr(content)",
                        "meta[property='twitter:title']::attr(content)",
                        "meta[name=title]::attr(content)",
                        "[itemprop=name]::text",
                        ".title::text"
                    ]
                }
            },
            "image": {
                "selectors": {
                    "css": [
                        'meta[property="og:image"]::attr(content)',
                        'meta[property="twitter:image"]::attr(content)',
                        "[itemprop=image]::attr(content)"
                    ]
                }
            },
            "description": {
                "selectors": {
                    "css": [
                        "meta[name='description']::attr(content)",
                        "meta[property='twitter:description']::attr(content)",
                        "meta[property='og:description']::attr(content)",
                        "meta[name=description]::attr(content)",
                        "[property=description]::attr(content)",
                        "[property='og:description']::attr(content)"
                    ]
                }
            },
            "author": {
                "selectors": {
                    "css": [
                        ".authorName::text",
                        "[name=author]::attr(content)",
                        # "[itemprop=creator] [itemprop=name]::text",
                    ]
                }
            },
            "datePublished": {
                "selectors": {
                    "css": [
                        "[itemprop=datePublished]::attr(content)",
                        "[property='article:published_time']::attr(content)"
                    ]
                }
            },
            "dateModified": {
                "selectors": {
                    "css": [
                        "[itemprop=dateModified]::text",
                        "[itemprop=dateModified]::attr(datetime)"
                    ]
                }
            },
            "articleBody": {
                "selectors": {
                    "css": [
                        "[itemprop=articleBody]",
                        ".content",
                        "#article_content"
                    ]
                },
                "contexts": {
                    "improve_html": [
                        "ze.spiders.elpais.ElPaisBrasilSpider.improve_html"
                    ]
                }
            },
            "keywords": {
                "selectors": {
                    "css": [
                        "meta[property='keywords']::attr(content)",
                        "[itemprop=keywords]::text",
                        "[name=news_keywords]::attr(content)"
                    ]
                }
            },
        }
    }]
    @staticmethod
    def improve_html(html, spider_name=None):
        exceptions = []; exceptions_append = exceptions.append

        to_decompose=['#elpais_gpt-INTEXT',]

        try:
            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA--------------------AAAAAAAAAAAAAAAA')
            for el in html.select('a'):
                el.replace_with(el.get_text())
        except Exception as e:
            exceptions_append(e)
        try:
            for item in to_decompose:
                for el in html.select(item):
                    el.decompose()
        except Exception as e:
            exceptions_append(e)

        return html, exceptions

