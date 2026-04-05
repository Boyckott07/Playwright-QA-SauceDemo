class LoginPage:
    def __init__(self, page):
        self.page = page
        # Selectores centralizados
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "h3[data-test='error']"
        self.header_title = ".title"

    def navigate(self, url):
        self.page.goto(url)

    def login(self, user, pwd):
        self.page.fill(self.username_input, user)
        self.page.fill(self.password_input, pwd)
        self.page.click(self.login_button)

    def get_error_text(self):
        return self.page.inner_text(self.error_message)

    def get_title_text(self):
        self.page.wait_for_selector(self.header_title, timeout=10000)
        return self.page.inner_text(self.header_title)