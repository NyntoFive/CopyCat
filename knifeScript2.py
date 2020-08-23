import urllib.parse
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

asess = AsyncHTMLSession()
session = HTMLSession()

def main():
    '''
    Query knifekits,holstersmith,xxxxx for a product SKU.
    If found, scrape URL for product data.
    If not found, write SKU: website to the log

    For each SKU that exists in both (all) sites,
        Download main product images, Compare:
                        naming, description, keywords,
                        Image similarity, ect
    
    Report Findings

    '''
    sites = ['https://knifekits.com/vcom/','https://holstersmith.com/vcom/']
    kk, hs = check_for_sku(sku, sites[0]), check_for_sku(sku, sites[1])
    
    if not kk:
        print("No KK")
    if not hs:
        print("NO HS")
    
QueryData = {
    "Matches": "meta[itemprop='numberOfItems']", # Css
    "Name": xpath('//h2/descendant::span[@itemprop="name"]/text()')
    "Name": xpath('//h2/a[@itemprop="url"]/@href')
    "Description": kk.html.xpath('//*[@itemprop="description"]/text()')[0].strip()
}

def check_for_sku(sku, shop):
    """Search for a product SKU per shop
    :param [sku] A Product SKU: "AV-KYSHE-BTLSHP-06-2448"
    :param [shop]: BaseURL of the website (shop) you want to check: "https://knifekits.com/vcom/"
    
    :return [Returns response object of Match, or False]"""

    url =  "advanced_search_result.php?keywords=" + urllib.parse.quote(sku)
    try:
        search_results = ses.post(shop + url)
        MATCH = search_results.html.find('a[itemprop="url"]', first=True).url
        print("Match Found!", MATCH)
        return ses.get(MATCH)
    except:
        print("No results! \nShop: {}\nSku: {}".format(shop,sku))
        return False


def parse_product_url(page):
    '''
    Parses product page for data
     :page, response object 
    '''###############
    description=page.html.xpath('//div[@itemprop="description"]')[0]
    price=page.html.xpath('//*[@itemprop="price"]/@content')[0]
    sku=page.html.xpath(".//*[@itemprop='model']/text()")[0]
    keywords = page.html.xpath(".//meta[@name='keywords']/@content")
    breadcrumbs = page.html.xpath('//*[@class="breadcrumb"]/descendant::text()')[::2]
    image = page.html.xpath('.//div[@class="piGalMain"]/img/@src')[0]
    all_images = page.html.xpath('//img/@src')
    images = [img for img in all_images if img.startswith("images/") and "600" in img or "800" in img and ".jpg" in img]
    link = page.url
    if "knifekits.com" in link:
        shop=0
    if "holstersmith.com" in link:
        shop=1
    
    Data = {"description":description, 
            "price":price,
            "sku":sku,
            "keywords":keywords,
            "breadcrumbs":breadcrumbs,
            "image":image,
            "all_images":all_images,
            "images":images,
            "link":link,
            "shop": shop
            }
    return Data
    
async def get_knifekits(sku):
    # Test SKU=AV-KYSHE-BTLSHP-06-2448
    url = "https://www.knifekits.com/vcom/kydex-sheet-colors-battleship-gray-c-1071_54_652_805.html"
    kk_r = await asess.get(url)
    
    r.html.find('img[alt="{}"]'.format(sku))
    images = [x.attrs.get('src') for x in imgs]

    return kk_r




async def get_holstersmith(sku):
    # Tes SKU = AV-KYSHE-BTLSHP-06-2448
    url = "https://www.holstersmith.com/vcom/kydex-sheet-battleship-gray-060-2ft-4ft-p-7004.html"
    hs_r = await asess.get(url)

    imgs=r.html.find('img[alt="{}"]'.format(sku))
    images = [x.attrs.get('src') for x in imgs]
    for IMG in images:
        base='https://holstersmith.com/vcom/'
        for I in images:
            HS_img = sess.get(base+I)
    
    match = search_sku(sku)
    # dl_img(images)


def make_thumbs(filename):
    for infile in glob.glob(filename):
        img = Image.open(infile)
        img.thumbnail((128,128), Image.ANTIALIAS)
        if infile[0:2] != "Th_":
            img.save("Th_" + infile.replace('.jpg', '.png'))