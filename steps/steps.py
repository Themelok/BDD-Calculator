from behave import *
import random

@given('two positive numbers')
def step_impl(context):
    context.first_int = random.randint(1,100)
    context.second_int = random.randint(1,100)
    assert isinstance(context.first_int, int)
    assert isinstance(context.second_int, int)

@given('two negative numbers')
def step_impl(context):
    context.first_int = random.randint(-100,0)
    context.second_int = random.randint(-100,0)
    assert isinstance(context.first_int, int)
    assert isinstance(context.second_int, int)

@given('one positive number and one negative number.')
def step_impl(context):
    context.first_int = random.randint(1,100)
    context.second_int = random.randint(-100,0)
    assert isinstance(context.first_int, int)
    assert isinstance(context.second_int, int)

# -- Scenario: Addition

@when('we add first numbers to second')
def step_impl(context):
    context.calc = context.open_proc()
    msg = '{}+{}'.format(context.first_int, context.second_int)
    context.out, context.err = context.calc.communicate(msg.encode('utf-8'))
    context.draft = str(context.first_int+context.second_int)
    context.out = context.handle_response(context.out)

@then('the result should be equal to summ')
def ster_impl(context):
    assert context.out == context.draft, '{} != {}'.format(context.out, context.draft)

# -- Scenario: Subtraction

@when('we subtract second number from first number')
def step_impl(context):
    context.calc = context.open_proc()
    msg = '{}-{}'.format(context.first_int, context.second_int)
    context.out, context.err = context.calc.communicate(msg.encode('utf-8'))
    context.draft = str(context.first_int-context.second_int)
    context.out = context.handle_response(context.out)

@then('the result should be equal to difference')
def ster_impl(context):
    assert context.out == context.draft, '{} != {}'.format(context.out, context.draft)

# -- Scenario: Multiplication

@when('we multiply first number by the second')
def step_impl(context):
    context.calc = context.open_proc()
    msg = '{}*{}'.format(context.first_int, context.second_int)
    context.out, context.err = context.calc.communicate(msg.encode('utf-8'))
    context.draft = str(context.first_int*context.second_int)
    context.out = context.handle_response(context.out)

@then('the result should be equal to product')
def ster_impl(context):
    assert context.out == context.draft, '{} != {}'.format(context.out, context.draft)

# -- Scenario: Division

@given('zero as the first and one any number as the second')
def step_impl(context):
    context.first_int = 0
    context.second_int = random.randint(-100,100)
    assert context.first_int == 0
    assert isinstance(context.second_int, int)

@given('any number as the first and  zero as the second')
def step_impl(context):
    context.first_int = random.randint(-100,100)
    context.second_int = 0
    assert context.second_int == 0
    assert isinstance(context.first_int, int)

@when('we divide first numbers by the second')
def step_impl(context):
    # import pdb; pdb.set_trace()
    context.calc = context.open_proc()
    msg = '{}/{}'.format(context.first_int, context.second_int)
    context.out, context.err = context.calc.communicate(msg.encode('utf-8'))
    context.draft = str(round(context.first_int/context.second_int,1))
    context.out = context.handle_response(context.out)
    a=1+1
    b=1+1

@when('we divide first numbers by zero')
def step_impl(context):
    # import pdb; pdb.set_trace()
    context.calc = context.open_proc()
    msg = '{}/{}'.format(context.first_int, context.second_int)
    context.out, context.err = context.calc.communicate(msg.encode('utf-8'))
    context.err = context.handle_response(context.err)
    a=1+1
    b=1+1

@then('the result should be equal to quotient')
def ster_impl(context):
    assert context.out == context.draft, '{} != {}'.format(context.out, context.draft)


@then('the result should be equal to zero')
def ster_impl(context):
    assert context.out == '0', '{} not 0'.format(context.out)

@then('the result should be Error')
def ster_impl(context):
    assert 'Error' in context.err, '{} not 0'.format(context.out)

