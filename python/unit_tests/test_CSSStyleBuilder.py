from unittest import TestCase
# Custom
from classpropertyparser import ClassPropertyParser
from cssstylebuilder import CSSStyleBuilder
__author__ = 'chad nelson'
__project__ = 'blow dry css'


class TestCSSStyleBuilder(TestCase):
    def test_get_css_text_sets(self):
        class_set = {
            'margin-top-10', 'bgc-h000', 'hide', 'margin-20', 'padding-top-10', 'height-200', 'padding-10',
            'valign-middle', 'b', 'width-150', 'width-50', 'font-size-48', 'c-blue', 'margin-top-50px',
            'text-align-center', 'height-50px', 'height-150px', 'bold', 'color-hfff'
        }
        expected_clean_set = {
            'c-blue', 'height-150px', 'bgc-h000', 'bold', 'color-hfff', 'height-50px', 'text-align-center',
            'margin-top-50px', 'valign-middle'
        }
        expected_removed_set = {'b (property_name not found in self.property_dict.)', 'margin-20 (cssutils invalid property value: 20)', 'padding-10 (cssutils invalid property value: 10)', 'margin-top-10 (cssutils invalid property value: 10)', 'font-size-48 (cssutils invalid property value: 48)', 'width-150 (cssutils invalid property value: 150)', 'padding-top-10 (cssutils invalid property value: 10)', 'hide (property_name not found in self.property_dict.)', 'height-200 (cssutils invalid property value: 200)', 'width-50 (cssutils invalid property value: 50)'}
        property_parser = ClassPropertyParser(class_set=class_set)
        style_builder = CSSStyleBuilder(property_parser=property_parser)
        self.assertTrue(style_builder.property_parser.class_set == expected_clean_set, msg=style_builder.property_parser.class_set)
        self.assertTrue(style_builder.property_parser.removed_class_set == expected_removed_set, msg=style_builder.property_parser.removed_class_set)

    def test_get_css_text_output(self):
        class_set = {
            'margin-top-10', 'bgc-h000', 'hide', 'margin-20', 'padding-top-10', 'height-200', 'padding-10',
            'valign-middle', 'b', 'width-150', 'width-50', 'font-size-48', 'c-blue', 'margin-top-50px',
            'text-align-center', 'height-50px', 'height-150px', 'bold', 'color-hfff'
        }
        expected_properties = [
            'background-color: #000;', 'vertical-align: middle;', 'color: blue;', 'margin-top: 50px;',
            'text-align: center;', 'height: 50px;', 'height: 150px;', 'font-weight: bold;', 'color: #fff;'
        ]
        property_parser = ClassPropertyParser(class_set=class_set)
        style_builder = CSSStyleBuilder(property_parser=property_parser)
        css_text = style_builder.get_css_text()

        for expected in expected_properties:
            self.assertTrue(expected in css_text)
            if expected in css_text:
                css_text = css_text.replace(expected, '')

        self.assertTrue(css_text.strip() == '', msg=css_text)   # remove whitespace
