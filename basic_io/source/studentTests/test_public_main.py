"""
test_public_main.py

This file contains the tests for when the entire program is run.
This only accounts for stdio.

Don't add test cases for sake of adding test cases. Think about
how each test case should showcase something different in the
student's submission.

This test file is public and is worth 3 points

1 point for sample tests
- The tests that are in the write-up
2 points for non-sample tests
- These tests check error handling, we will expand more on them in the private tests
"""

# Weight is used to set the number of points that the test is worth on gradescope
# Number is used to order the test on gradescope as the order that tests are run in is random
from gradescope_utils.autograder_utils.decorators import weight, number
# The student submission executor controls the execution of the submission
#  It creates the sandbox and links the submission to the runner to be executed
from StudentSubmission import StudentSubmissionExecutor
# One of the predefined runners that is used to execute the main module in a submission
#  A runner is basically a thin wrapper around the actual that the student submitted code
#  that exposes an interface to the RunnableSubmission that facilitates the actual execution
#  of the code
from StudentSubmission.Runners import MainModuleRunner

# BaseTest contains all the common code that is needed for a TestClass to run correctly.
#  It also contains useful assertions
from TestingFramework import BaseTest

# Possible results is an enum for all the possible things that the autograder is able to observe.
from StudentSubmission.common import PossibleResults


# All test classes must inherit from BaseTest to be able to access the student submission object
class TestPublicMain(BaseTest):

    @classmethod
    def setUpClass(cls):
        # If the setup class method is overriden, the first call should be to the super setUpClass
        #  method as it does a lot of setup.
        # In general, there isn't usually much of a reason to override this method
        # The setUpClass method get called once per class
        super().setUpClass()

    def setUp(self):
        # The setup method gets called before each test runs
        # This is where all common setup code should be written (ie, setting up the environment)

        # Creates a new environment with the students submission
        self.environment = StudentSubmissionExecutor.generateNewExecutionEnvironment(self.studentSubmission)
        # How long we should wait for the student's execution to wait
        self.environment.timeout = 1

        # The runner object should be reconstructed before every test
        self.runner = MainModuleRunner()

    def tearDown(self):
        # Need to clean up after the run to ensure that everything gets reset.
        StudentSubmissionExecutor.cleanup(self.environment)

    # Functions like this help keep us from repeating code.
    # I highly recommend writing functions like this as much as possible
    def assertStdIo(self, stdin: list[str], expectedOutput: list[str]):
        # You set all the inputs in the environment and get the outputs from the environment
        self.environment.stdin = stdin

        # Setup environment for executing and pass control to the RunnableStudentSubmission
        #  to spawn the student's submission
        # This method will raise assertion errors if anything happens during execution
        StudentSubmissionExecutor.execute(self.environment, self.runner)

        # Attempt to get stdout from the student's execution.
        #  If stdout doesn't exist, then an assertion error will be raised
        actualOutput = StudentSubmissionExecutor.getOrAssert(PossibleResults.STDOUT)

        # The assertion here will be shown to the student, so they know where they went wrong
        self.assertEqual(expectedOutput, actualOutput)

    # Generally, we want all the sample test cases to add up to one point total
    @weight(.5)
    @number(1.1)
    def test_sample_1(self):
        """Sample Execution 1"""
        # The comment under the test name is the name of the test that gets displayed

        # Can define the stdin as either a string or a list
        stdin = [
            "shipment:apples:150",
            "sale:apples:10",
            "EOD"
        ]

        expectedOutput = [
            "Received shipment of 150 apples",
            "Sold 50 apples",
            "apples: 100"
        ]

        self.assertStdIo(stdin, expectedOutput)

    @weight(.5)
    @number(1.2)
    def test_sample_2(self):
        """Sample Execution 2"""

        stdin = [
            "shipment:bananas:150",
            "shipment:apples:100",
            "EOD"
        ]

        expectedOutput = [
            "Received shipment of 150 bananas",
            "Received shipment of 100 apples",
            "bananas: 150",
            "apples: 100"
        ]

        self.assertStdIo(stdin, expectedOutput)

    @weight(1)
    @number(2.1)
    def test_negative_sale(self):
        """Sale with not enough inventory of item"""
        stdin = [
            "shipment:bananas:50",
            "sale:bananas:75",
            "EOD"
        ]

        expectedOutput = [
            "Received shipment of 50 bananas",
            "Sold 50 bananas",
            "bananas: 0"
        ]

        self.assertStdIo(stdin, expectedOutput)

    @weight(1)
    @number(2.2)
    def test_non_existent_inventory(self):
        """Sale of items not in inventory"""
        stdin = [
            "sale:apples:50",
            "EOD"
        ]

        expectedOutput = [
            "ERROR: apples not found in inventory"
            "No items in inventory"
        ]

        self.assertStdIo(stdin, expectedOutput)
