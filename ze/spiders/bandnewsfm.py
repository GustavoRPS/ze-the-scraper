# -*- coding: utf-8 -*-
from . import ZeSpider


class BandNewsFMSpider(ZeSpider):

    name = 'bandnewsfm'
    allowed_domains = ['cbn.globoradio.globo.com']
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
                        "#materia_interna h1::text"
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
            "description":  {
                "selectors": {
                    "css": [
                        "meta[property='og:description']::attr(content)",
                        "meta[name=description]::attr(content)",
                        "[itemprop=description]::text",
                        "[itemprop=alternativeHeadline]::text",
                        "#materia_interna h2::text"
                    ]
                }
            },
            "author": {
                "selectors": {
                    "css": [
                        "[itemprop=author]::text",
                        "[itemprop=creator]::text",
                        ".td-post-author-name a::text"
                    ]
                }
            },
            "audio": {
                "item": "ze.items.creativework.AudioObjectItem",
                "fields": {
                    "url": {
                        "selectors": {
                            "css": [
                                ".td-post-content iframe::attr(src)"
                            ]
                        },
                        "contexts": {
                            "format": "http://video12.mais.uol.com.br/{}.mp3"
                        }
                    }
                }
            },
            "datePublished": {
                "selectors": {
                    "css": [
                        "[itemprop=datePublished]::attr(datetime)",
                        "[itemprop=datePublished]::text",
                        "time[datetime]::text",
                        "time::attr(datetime)",
                        ".datahora::text"
                    ]
                }
            },
            "dateModified": {
                "selectors": {
                    "css": [
                        "[itemprop=dateModified]::attr(datetime)" ,
                        "[itemprop=dateModified]::text",
                        ".updated"
                    ]
                }
            },
            "articleBody": {
                "selectors": {
                    "css": [
                       "[itemprop=articleBody]",
                        "#materia_interna",
                        '.td-post-content'
                    ]
                },
                "contexts": {
                    "improve_html": [
                        "ze.spiders.bandnewsfm.BandNewsFMSpider.improve_html"
                    ]
                }
            },
            "keywords": {
                "default": ["rádio"],
                "selectors": {
                    "css": [
                        "meta[name=keywords]::attr(content)",
                        "[itemprop=keywords]::text"
                    ]
                }
            }
        }
    }]
    # def harvest_metadata(self, resp: Response, item, **kargs):
    #     # TODO: Move to DownloadMiddleware
    #     item['meta']['jsonLDSchemas'] = self.jsonLDSchemas(reponse)
    #     item['meta']['otherLinks'] = self.jsonLD

    @staticmethod
    def improve_html(html, spider_name=None):
        exceptions = []; exceptions_append = exceptions.append

        to_decompose=[]

        try:
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


