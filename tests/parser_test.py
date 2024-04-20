import unittest
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path.parent))
import parser_services


class ProductPageTest(unittest.TestCase):

    def assert_html_content(self, input, output_path):
        output = open(output_path, encoding='utf-8').read()
        self.assertEqual(str(input), str(output))

    def setUp(self):
        self.parser = parser_services.ProductPageParser('')

    def test_get_telephone_number(self):
        html = open('rescourses/html/ProductPageParser/get_telephone_number_image/input_1.html',
                    encoding='utf-8').read()
        self.parser.set_html(html)
        self.assert_html_content(self.parser.get_telephone_number_image(),
                         'rescourses/html/ProductPageParser/get_telephone_number_image/output_1.html')

        html = open('rescourses/html/ProductPageParser/get_telephone_number_image/input_2.html',
                    encoding='utf-8').read()
        self.parser.set_html(html)
        self.assert_html_content(self.parser.get_telephone_number_image(),
                         'rescourses/html/ProductPageParser/get_telephone_number_image/output_2.html')

        html = open('rescourses/html/ProductPageParser/get_telephone_number_image/input_3.html',
                    encoding='utf-8').read()
        self.parser.set_html(html)
        self.assert_html_content(self.parser.get_telephone_number_image(),
                         'rescourses/html/ProductPageParser/get_telephone_number_image/output_3.html')
