from behave import given, when, then
from calculator import Calculator

@given('I have a calculator')
def step_given_i_have_a_calculator(context):
    context.calculator = Calculator()

@when('I add {a:d} and {b:d}')
def step_when_i_add(context, a, b):
    context.result = context.calculator.add(a, b)

@when('I subtract {a:d} from {b:d}')
def step_when_i_subtract(context, a, b):
    context.result = context.calculator.subtract(b, a)

@when('I multiply {a:d} by {b:d}')
def step_when_i_multiply(context, a, b):
    context.result = context.calculator.multiply(a, b)

@when('I divide {a:d} by {b:d}')
def step_when_i_divide(context, a, b):
    try:
        context.result = context.calculator.divide(a, b)
    except ValueError as e:
        context.error_message = str(e)

@then('the result should be {expected:d}')
def step_then_the_result_should_be(context, expected):
    assert context.result == expected, f"Expected {expected}, but got {context.result}"

@then('I should receive an error saying "{message}"')
def step_then_i_should_receive_an_error(context, message):
    assert context.error_message == message, f"Expected error message '{message}', but got '{context.error_message}'"
