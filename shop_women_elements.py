

class ShopWomem:

    def __init__(self, page):
        self.celebrating_beauty_header = page.locator("text=Celebrating Beauty and Style")
        self.celebrating_beauty_body = page.locator("text=playwright-practice was founded by a group of like-minded fashion devotees")
        self.celebrating_beauty_hdr = page.locator("text=Celebrating Beauty and Stype")
        self.profile_arrow = page.locator('._1hHt1')
        self.profile_icon = page.locator('bQgup')
        self.my_orders = page.locator('text=My Orders')
        self.my_orders_profile_box = page.locator('#SOSP_CONTAINER_CUSTOM_ID >> :nth-match(div, 4)')
