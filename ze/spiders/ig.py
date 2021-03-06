# -*- coding: utf-8 -*-
from . import ZeSpider


class IGSpider(ZeSpider):

    name = 'ig'
    allowed_domains = ['ig.com.br']
    items_refs = [{
        "spider_name":name,
        "item": "ze.items.creativework.ArticleItem",
        "fields": {
            "name": {
                "selectors": {
                    "css": [
                        "meta[property='og:title']::attr(content)",
                        "meta[name=title]::attr(content)",
                        "[itemprop=name]::text",
                        "#noticia-titulo-h1::text",
                        ".titinterna::text"
                    ]
                }
            },
            "image": {
                "selectors": {
                    "css": [
                        'meta[property="og:image"]::attr(content)',
                        "[itemprop=image]::attr(content)",
                        "[property='og:image']::attr(content)"
                    ]
                }
            },
            "description": {
                "selectors": {
                    "css": [
                        "meta[property='og:description']::attr(content)",
                        "meta[name=description]::attr(content)",
                        "[itemprop=description]::text",
                        "[property=description]::attr(content)",
                        "[property='og:description']::attr(content)",
                        ".subtitinterna::text"
                    ]
                }
            },
            "author": {
                "selectors": {
                    "css": [
                        "[itemprop=author]::text",
                        "[itemprop=creator] [itemprop=name]::text",
                        "#authors-box::text",
                        "#authors-box strong::text",
                        ".info::text"

                    ]
                }
            },
            "datePublished": {
                "selectors": {
                    "css": [
                        "[itemprop=datePublished]::text",
                        "[property='article:published_time']::attr(content)",
                        ".info::text"
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
                        "#noticia",
                        ".texto-noticia"
                    ]
                },
                "contexts": {
                    "improve_html": [
                        "ze.spiders.ig.IGSpider.improve_html"
                    ]
                }
            },
            "keywords": {
                "selectors": {
                    "css": [
                        "[itemprop=keywords]::text",
                        "[name=news_keywords]::attr(content)"
                    ]
                }
            }
        }
    }]

    @staticmethod
    def improve_html(html, spider_name=None):
        exceptions = []; exceptions_append = exceptions.append
        try:
            for el in html.select('a'):
                el.replace_with(el.get_text())
        except Exception as e:
            exceptions_append(e)

        return html, exceptions
