from behave import *


def addition(a, b):
    return a + b


@given(u'I have entered into the calculator')
def step_impl(context):
    context.a = context.text

@given(u'I entered a 2nd variable into the calculator')
def step_impl(context):
    context.b = context.text
@when(u'I press add')
def step_impl(context):
    context.results = addition(context.a, context.b)

@then(u'the results should be 150 on the screen')
def step_impl(context):
    assert context.results, 150

@given(u'the results above')
def step_impl(context):
    context.execute_steps(u"""
    given I have entered into the calculator
    given I entered a 2nd variable into the calculator
    when I press add
    then the results should be 150 on the screen
    """)



    assert False

@given(u'I entered another variable into the calculator')
def step_impl(context):
    assert False

@when(u'I press add this time wround')
def step_impl(context):
    assert False

@then(u'the results hould be 250')
def step_impl(context):
    assert False
