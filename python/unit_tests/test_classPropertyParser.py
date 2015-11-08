from unittest import TestCase
from cssparser import ClassPropertyParser


class TestClassPropertyParser(TestCase):
    def test_class_set_to_lowercase(self):
        original_class_set = {'ThE', 'the', 'THE', 't2HE'}
        expected_class_set = {'the', 'the', 'the', 't2he'}
        class_parser = ClassPropertyParser(class_set=original_class_set)
        class_parser.class_set_to_lowercase()
        self.assertEquals(class_parser.class_set, expected_class_set)

    def test_underscores_valid_is_true(self):
        valid_classes = {'6_3', 'padding-5_2rem', 'height-24_48p'}
        class_parser = ClassPropertyParser(class_set=valid_classes)
        for css_class in class_parser.class_set:
            self.assertTrue(class_parser.underscores_valid(css_class=css_class), msg=css_class)

    def test_underscores_valid_is_false(self):
        # Invalid: '-_2", '2_rem', 'm_px', and '__'
        invalid_classes = {'_bold', 'lighter-1_', 'width-_2', 'margin-2_rem', 'height-m_px', 'bg-color__blue'}
        class_parser = ClassPropertyParser(class_set=invalid_classes)
        for css_class in class_parser.class_set:
            self.assertFalse(class_parser.underscores_valid(css_class=css_class), msg=css_class)

    def test_clean_class_set(self):
        valid_classes = {'width-6_3', 'padding-5_2rem', 'height-24_48p', 'padding-7_3-8_5-9_7-10_2'}
        invalid_classes = {'_b', 'lighter-1_', 'width-_2', 'margin-2_rem', 'height-m_px', 'bg-color__blue'}
        class_parser = ClassPropertyParser(class_set=valid_classes.union(invalid_classes))
        class_parser.clean_class_set()                              # Called explicitly even though called by init().
        self.assertEquals(class_parser.class_set, valid_classes)    # Only valid classes should remain.
        self.assertEquals(class_parser.removed_class_set, invalid_classes)

    def test_get_property_name_by_identical_name_valid(self):
        valid_identical_set = {'font-weight-bold', 'font-weight-700'}
        expected_property_name = 'font-weight'
        class_parser = ClassPropertyParser(class_set=valid_identical_set)

        class_list = list(class_parser.class_set)
        for i, css_class in enumerate(class_list):
            property_name = class_parser.get_property_name(css_class=css_class)
            self.assertEquals(property_name, expected_property_name)

    def test_get_property_name_by_identical_name_invalid(self):
        invalid_identical_set = {'font-weight', 'font-weight-', '-font-weight'}
        expected_property_name = ''
        expected_empty_set = set()
        class_parser = ClassPropertyParser(class_set=invalid_identical_set)

        class_list = list(class_parser.class_set)
        for i, css_class in enumerate(class_list):
            property_name = class_parser.get_property_name(css_class=css_class)
            self.assertEquals(property_name, expected_property_name)
        self.assertEquals(class_parser.class_set, expected_empty_set)

    def test_get_property_name_alias(self):
        identical_set = {'normal', 'b', 'bold', 'bolder', 'lighter', 'initial', 'inherit', 'fw'}
        expected_property_name = 'font-weight'
        class_parser = ClassPropertyParser(class_set=identical_set)

        class_list = list(class_parser.class_set)
        for i, css_class in enumerate(class_list):
            property_name = class_parser.get_property_name(css_class=css_class)
            self.assertEquals(property_name, expected_property_name)

    def test_get_property_name_non_matching(self):
        non_matching = {'font-weight', 'font-weight-', '-font-weight'}
        expected_property_name = ''
        expected_empty_set = set()
        class_parser = ClassPropertyParser(class_set=non_matching)

        class_list = list(class_parser.class_set)
        for i, css_class in enumerate(class_list):
            property_name = class_parser.get_property_name(css_class=css_class)
            self.assertEquals(property_name, expected_property_name)
        self.assertEquals(class_parser.class_set, expected_empty_set)

    #def test_get_encoded_property_value(self):


    # def test_get_property_value(self):
    #     self.fail()
    #
    # def test_get_property_priority(self):
    #     self.fail()