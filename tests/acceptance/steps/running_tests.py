from behave import given, when, then

from tests.test_app.tests import MyCustomTestCase, MyCustomTestRunner


@given(u'this step exists')
def step_exists(context):
    pass


@when(u'I run "python manage.py behave"')
def run_command(context):
    pass


@then(u'I should see the behave tests run')
def is_running(context):
    pass


@then(u'the test_runner should be MyCustomTestRunner')
def get_runner_dynamically(context):

    assert context.test_runner.is_custom


@then(u'before_django_ready should be called')
def before_django_context(context):
    assert context.before_django, "custom hook should be called"
    assert context.test_runner.before_django, "runner should have custom hook flag"
    assert MyCustomTestCase in context.test_runner.testcase_class.mro(), "test case sould be created from MyCustomTestCase"
    assert context.test_runner.testcase_class.is_custom, "test case should be the custom one"


@then(u'django_ready should be called')
def django_context(context):
    assert context.django
