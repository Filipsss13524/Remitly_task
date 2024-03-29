import unittest
import main
import pytest

#date.json - "*" in Resource
#date_v1.json - "text" in Resource
#date_v2.json - Error in name PolicyDocument
#date_v3.json - ["*"] in Resource - one element with []
#date_v4.json - ["*","text"] in Resource - two element with []


class MyTestCase(unittest.TestCase):
    def test_resource_checker_pandas(self):
        # "*" in Resource
        self.assertEqual(main.resource_checker_pandas('date.json'), False)
        # Errors in path name
        self.assertEqual(main.resource_checker_pandas('date.jso'), True)
        self.assertEqual(main.resource_checker_pandas('dat.json'), True)
        # "text" in Resource
        self.assertEqual(main.resource_checker_pandas('date_v1.json'), True)
        # Error in name PolicyDocument
        self.assertEqual(main.resource_checker_pandas('date_v2.json'), True)
        # ["*"] in Resource - one element with []
        self.assertEqual(main.resource_checker_pandas('date_v3.json'), False)
        # ["*","text"] in Resource - two element with []
        self.assertEqual(main.resource_checker_pandas('date_v4.json'), True)

    def test_resource_checker_function(self):
        # "*" in Resource
        self.assertEqual(main.resource_checker_function('date.json'), False)
        # Errors in path name
        self.assertEqual(main.resource_checker_function('date.jso'), True)
        self.assertEqual(main.resource_checker_function('dat.json'), True)
        # "text" in Resource
        self.assertEqual(main.resource_checker_function('date_v1.json'), True)
        # Error in name PolicyDocument
        self.assertEqual(main.resource_checker_function('date_v2.json'), True)
        # ["*"] in Resource - one element with []
        self.assertEqual(main.resource_checker_function('date_v3.json'), False)
        # ["*","text"] in Resource - two element with []
        self.assertEqual(main.resource_checker_function('date_v4.json'), True)


if __name__ == '__main__':
    unittest.main()
