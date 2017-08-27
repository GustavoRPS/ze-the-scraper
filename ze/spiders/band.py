# -*- coding: utf-8 -*-
from . import ZeSpider


class BandSpider(ZeSpider):

    name = 'band'
    allowed_domains = ['band.uol.com.br']
    items_refs = [{
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
                        # "[itemprop=author]::text", 
                        "[itemprop=creator]::text",
                        "#mat_autor_nome::text"
                    ]
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
                        "#materia_interna"
                    ]
                }
            },
            "keywords": {
                "selectors": {
                    "css": [ 
                        "meta[name=keywords]::attr(content)",
                        "[itemprop=keywords]::text",
                        "[itemprop=keywords]::attr(content)"
                    ]
                }
            }
        }
    }]
