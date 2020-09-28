from requests_html import HTMLSession
from lxml import html
import datetime
import arrow
import json, re, os
import pandas as pd


def fetch_map(url):
    '''Fetch sitemap and return parsed txt'''
    response=session.get(url)
    return response

def parse_xml(response):
    '''
    Reads the fetched sitemap and checks for new Products
    Returns list of urls added in the last 7 days.
    '''
    urls = response.html.xpath('//loc/text()')
    dates = [arrow.get(date) for date in response.html.xpath('//lastmod/text()')]
    urls_to_crawl=[]
    for x in enumerate(dates):
        if x[1].date() - datetime.timedelta(days=-7) > datetime.date.today():
            urls_to_crawl.append(urls[x[0]])
    return urls_to_crawl
 
def get_urls_to_crawl():
    '''
    Fetch sitemaps and determine what urls to crawl.
    Return a dict of product urls per shop / sitemap
    '''
    kk_sitemap = 'https://knifekits.com/vcom/smproducts.xml'
    hs_sitemap = 'https://holstersmith.com/vcom/smproducts.xml'

    # parse_xml defaults to the last 7 days.
    # This can be adjusted (days=-7), Negative values are in the past!
    kk_urls =  parse_xml(fetch_map(kk_sitemap))
    hs_urls =  parse_xml(fetch_map(hs_sitemap))
    
    both = [kk_urls, hs_urls]
    return {"kk":kk_urls,"hs":hs_urls,"both":both}

def parse_url(url):
    '''
    Parse url for product data
    Return dict(data)
    '''
    page = session.get(url)

    description=page.html.xpath('//div[@itemprop="description"]',first=True)
    desc_text = description.text
    price=page.html.xpath('//*[@itemprop="price"]/@content',first=True)
    sku=page.html.xpath(".//*[@itemprop='model']/text()",first=True)
    metaKeywords = page.html.xpath(".//meta[@name='keywords']/@content")
    breadcrumbs = page.html.xpath('//*[@class="breadcrumb"]/descendant::text()')[2::2]
    image = page.html.xpath('.//div[@class="piGalMain"]/img/@src',first=True)
    images = [img.attrs['data-image'] for img in page.html.xpath('//*[@data-target="#image-gallery"]')]
    category = breadcrumbs[1]
    subcategory=breadcrumbs[2]
    name = page.html.xpath('//h1/descendant::span[@itemprop="name"]/text()', first=True)
    
    Data = {"description":description,
            "desc_text": desc_text,
            "price":price,
            "sku":sku,
            "metaKeywords":metaKeywords,
            "breadcrumbs":breadcrumbs,
            "image":image,
            "images":images,
            "link":url,
            "category":category,
            "subcategory":subcategory,
            "name": name
            "shop": Shop.objects.get(name="Knifekits")
            }
    return Data




# Get new urls every N days (7)
def main():
    session = HTMLSession()
    urls = get_urls_to_crawl()  
    
    
    for url in urls['kk']:
        item = parse_url(url)
        try:
            Product.objects.get_or_create(**item)
            print("Success! ", item)
        except:
            print("Failed to import Product: ",url)
            
                
if __name__ == "__main__":
    main()