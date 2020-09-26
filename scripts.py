from requests_html import HTMLSession

from lxml import html
import pandas as pd
import datetime
import arrow
import json, re, os

def main():
    new_product_urls = parse_xml(fetch_map('https://knifekits.com/vcom/smproducts.xml'))

def fetch_map(url):
    '''Fetch sitemap and return parsed txt'''
    response=session.get(url)
    return response

def parse_xml(response):
    '''Parse response and return new URLS to crawl.
        Returns list of urls added in the last 7 days
    '''
    urls = response.html.xpath('//loc/text()')
    dates = [arrow.get(date) for date in response.html.xpath('//lastmod/text()')]
    urls_to_crawl=[]
    for x in enumerate(dates):
        if x[1].date() - datetime.timedelta(days=-7) > datetime.date.today():
            urls_to_crawl.append(urls[x[0]])
    return urls_to_crawl

def parse_url(url):
    '''Parse url for product data
        Return dict(data)
    '''
    page = session.get(url)
    description=page.html.xpath('//div[@itemprop="description"]')[0]
    desc_text = description.text
    price=page.html.xpath('//*[@itemprop="price"]/@content')[0]
    sku=page.html.xpath(".//*[@itemprop='model']/text()")[0]
    keywords = page.html.xpath(".//meta[@name='keywords']/@content")
    breadcrumbs = page.html.xpath('//*[@class="breadcrumb"]/descendant::text()')[2::2]
    image = page.html.xpath('.//div[@class="piGalMain"]/img/@src')[0]
    all_images = page.html.xpath('//img/@src')
    images = [img for img in all_images if "600" in img or "800" or "550" in img and ".jpg" in img]
    cat = breadcrumbs[1]
    subcat=breadcrumbs[2]
    Data = {"description":description,
            "desc_text": desc_text,
            "price":price,
            "sku":sku,
            "keywords":keywords,
            "breadcrumbs":breadcrumbs,
            "image":image,
            "images":images,
            "link":url,
            "category":cat,
            "subcategory":subcat
            }
    return Data

def crawl_drive(start,fileType="*.mp3"):
    '''crawls filesystem from start and returns a list of mp3files'''
    music=[]
    for folderName, subfolders, filenames in os.walk(start):
        for subfolder in subfolders:
            for filename in filenames:
                if fileType in filename:

                    music.append(filename)
    return music
