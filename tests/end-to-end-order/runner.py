import sys
import unittest
import HtmlTestRunner

sys.path.append('../../')
from end_to_end_complete_order import OrderTest

if __name__ == "__main__":

    runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="End_2_End_Order_Report")

    test_classes_to_run = [OrderTest]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    suite = unittest.TestSuite(suites_list)

    results = runner.run(suite)