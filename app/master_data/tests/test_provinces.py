from django.test import TestCase

class ProvincesTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("ProvincesTestClass: Start testing...")
        pass

    def setUp(self):
        print("Setup testing")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
