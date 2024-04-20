from bs4 import BeautifulSoup


class ProductPageParser(BeautifulSoup):

    def __init__(self, html, type='lxml'):
        super().__init__(html, type)

    def set_html(self, html, type='lxml'):
        super().__init__(html, type)

    def get_price(self):
        price_block = self.find('span', attrs={'itemprop': 'price'})
        return price_block['content']

    def get_name(self):
        name_block = self.find('span', 'title-info-title-text')
        return name_block.string

    def get_telephone_number_image(self):
        try:
            telephone_image = self.find('div', 'contacts-root-1q_8O').img
        except AttributeError:
            telephone_image = self.find('div', {'data-marker': 'phone-popup'}).img
        return telephone_image
