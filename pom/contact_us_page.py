class ContactUsPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self, name, address, email, phone_num, subject, message):
        self.page.locator("[placeholder='Enter your name']").fill(name)
        self.page.locator("[placeholder='Enter your address']").fill(address)
        self.page.locator("[placeholder='Enter your email']").fill(email)
        self.page.locator("[placeholder='Enter your phone number']").fill(phone_num)
        self.page.locator("[placeholder='Type the subject']").fill(subject)
        self.page.locator("textarea").fill(message)

        #self.page.press("[aria-label='Enter your search term']","Enter")
