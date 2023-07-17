"""
test_public_function.py

This file contains the tests for the two required functions that students have to write,
`record_shipment` and `record_sale`.

The biggest difference with function tests vs main tests is that runner is different.
"""

from gradescope_utils.autograder_utils.decorators import weight, number
from StudentSubmission import StudentSubmissionExecutor
# We use the function runner rather than main runner
# Internally this runner runs the entire student submission then uses reflection to
#  call the student's function.
from StudentSubmission.Runners import FunctionRunner
from TestingFramework import BaseTest
from StudentSubmission.common import PossibleResults
class TestPublicFunction(BaseTest):
    pass