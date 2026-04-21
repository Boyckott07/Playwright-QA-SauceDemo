from behave import given, when, then
from features.pages.login_page import LoginPage

@given('I navigate to "{url}"')
def step_impl(context, url):
    # Creamos la instancia del POM
    context.login_page = LoginPage(context.page)
    context.login_page.navigate(url)

@when('I enter "{userito}" as username')
def step_impl(context, userito):
    # Usamos el atributo del objeto
    context.page.fill(context.login_page.username_input, userito)

@when('I enter "{password}" as password')
def step_impl(context, password):
    context.page.fill(context.login_page.password_input, password)

@when('I click the login button')
def step_impl(context):
    # Usamos el método de Playwright directamente sobre el selector del POM
    context.page.click(context.login_page.login_button)

@then('I should see the products page title "{expected_title}"')
def step_impl(context, expected_title):
    # Usamos el método que creamos en el POM para obtener el texto
    assert context.login_page.get_title_text() == expected_title

@then('I should see an error message containing "{expected_error}"')
def step_impl(context, expected_error):
    error_text = context.login_page.get_error_text()
    assert expected_error in error_text