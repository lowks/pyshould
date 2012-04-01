from .expectation import *

# Create instances to be used with the overloaded | operator
should = Expectation(deferred=True)
should_not = ExpectationNot(deferred=True)
should_all = ExpectationAll(deferred=True)
should_any = ExpectationAny(deferred=True)
should_none = ExpectationNone(deferred=True)
should_either = Expectation(deferred=True, def_op=OPERATOR_OR)


def it(value):
    """ Wraps a value in a should """
    return Expectation(value)

def any_of(value):
    """ At least of the items in value should match """
    return ExpectationAny(value)

def all_of(value):
    """ All the items in value should match """
    return ExpectationAll(value)

def none_of(value):
    """ None of the items in value should match """
    return ExpectationNone(value)
