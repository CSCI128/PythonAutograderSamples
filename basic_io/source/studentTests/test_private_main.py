"""
test_private_main.py

This file contains the tests for when the entire program is run.
This only accounts for stdio.

Private tests should not be doing anything fundamentally new to the students submission, rather it should be expanding
on what has already been tested

This test file is private
"""

from gradescope_utils.autograder_utils.decorators import weight, number
from StudentSubmission import StudentSubmissionExecutor
from StudentSubmission.Runners import MainModuleRunner
from TestingFramework import BaseTest
from StudentSubmission.common import PossibleResults


class TestPrivateMain(BaseTest):
    def setUp(self):
        self.environment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        self.environment.timeout = 1

        self.runner = MainModuleRunner()

    def tearDown(self):
        StudentSubmissionExecutor.cleanup(self.environment)

    # This function is very similar to the one found in the public test file, except that
    #  the actual assertion on the student's output is hidden - but they will still receive
    #  error messages with their submission
    def assertStdIo(self, stdin: list[str], expectedOutput: list[str]):
        self.environment.stdin = stdin

        StudentSubmissionExecutor.execute(self.environment, self.runner)

        actualOutput = StudentSubmissionExecutor.getOrAssert(PossibleResults.STDOUT)

        try:
            self.assertEqual(expectedOutput, actualOutput)
            # we catch the assertion error so that the student doesn't see where their
            #  output was wrong
        except AssertionError:
            # then so the test actually fails, we re-raise the assertion error
            raise AssertionError("Incorrect Output")

    # for the actual tests, we want to expand on what was tested in the public tests
    #  we don't want to do anything new because that's not really fair to the students

    @weight(1)
    @number(3.1)
    def test_many_items_not_in_inventory(self):
        """Sale of many items not in inventory"""
        # Make sure that the name for the private tests is still helpful,
        #  so the student has an idea of what was tested and what will help.
        #  This also helps TAs in OH when they need to quickly be reminded about
        #  what was tested in this test case.

        stdin = [
            "shipment:apples:50",
            "sale:apples:50",
            "sale:bananas:50",
            "sale:bananas:50",
            "sale:oranges:50",
            "EOD"
        ]

        expectedOutput = [
            "Received shipment of 50 apples",
            "Sold 50 apples",
            "ERROR: bananas not found in inventory",
            "ERROR: bananas not found in inventory",
            "ERROR: oranges not found in inventory",
            "apples: 0"
        ]

        self.assertStdIo(stdin, expectedOutput)

    @weight(1)
    @number(3.2)
    def test_repeated_sale(self):
        """Many sales of the same item"""

        stdin = [
            "shipment:apples:150",
            "sale:apples:50",
            "sale:apples:50",
            "sale:apples:60",
            "EOD"
        ]

        expectedOutput = [
            "Received shipment of 150 apples",
            "Sold 50 apples",
            "Sold 50 apples",
            "Sold 50 apples",
            "apples: 0"
        ]

        self.assertStdIo(stdin, expectedOutput)




