import multiprocessing
import requests_services
import itertools
import parser_services
import tesseract_services
import json_services


def write_in_json(name, price, phone):
    json_services.print_product_data_from_json(name, price, phone)


def parse(url):
    requests_services.download_phone_image(url)
    parser = parser_services.ProductPageParser(requests_services.get_html(url))
    name = parser.get_name()

    try:
        price = parser.get_price()
    except TypeError:
        price = 'free'

    try:
        phone = tesseract_services.get_phone()
    except FileNotFoundError:
        phone = None

    print(name, price, phone, sep=', ')

    return name, price, phone


def main():
    a = [30 * index for index in range(10)]

    with multiprocessing.Pool(10) as pool:
        jsones = pool.map(requests_services.get_json_with_links, a)

    with multiprocessing.pool.ThreadPool(40) as pool:
        links = pool.map(requests_services.get_links_on_json, jsones)

    links = list(itertools.chain.from_iterable(links))

    for link in links:
        if link is not None:
            data = parse(link)
            write_in_json(*data)


if __name__ == '__main__':
    main()
