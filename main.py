import bs4
import requests
import lxml


class AsaxiyScrapper:
    def __init__(self, *args, **kwargs):
        pass

    def get_products(self, name="iphone"):
        url = f"https://asaxiy.uz/product?key={name}&size=72"

        response = requests.get(url)

        soup = bs4.BeautifulSoup(response.content, 'html.parser')

        # body > main > section > div > div > div.col-lg-9.col-md-12 > div.row.custom-gutter.mb-40

        products = soup.find_all("div", attrs={"class": "col-6 col-xl-3 col-md-4"}, limit=72)

        for product in products:
            # image_link = product.find("div", attrs={"class": "product__item-img"}).find("img")['data-src']
            title = product.find("span", attrs={"class": "product__item__info-title"}).text
            price = product.find("span", attrs={"class": "product__item-price"}).text
            image_link = product.find("img", attrs={"class": "img-fluid"})['data-src']
            is_sale = product.find("span", attrs={"class": "pr_flash pr_discount"})

            if is_sale:
                is_sale = True
            else:
                is_sale = False

            print(f"Title: {title}", f"Price: {price}", f"Image: {image_link}", f"Is Sale: {is_sale}", sep="\n")


scrapper = AsaxiyScrapper()
scrapper.get_products("iphone")
