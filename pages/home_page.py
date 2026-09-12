from playwright.sync_api import Page, expect

class HomePage:

    def __init__(self, page:Page):
        self.page =  page
        self.new_cars = page.locator('//div[@class="o-os o-js o-jy o-kF o-mo o-ef o-bS o-co o-mJ dvEJRN"]').nth(0)
        self.find_new_cars = page.locator("//div[contains(text(),'Find New Cars')]")
        self.maruti_suzuki = page.locator('//img[@title="Maruti Suzuki Cars"]')
        # self.dashboard_link = page.locator('//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]').nth(7)


    def hover_new_cars(self):
        self.new_cars.hover()

    def click_find_new_cars(self):
        self.find_new_cars.click()

    def move_mouse_outside(self):
        self.page.mouse.move(0 , 0)

    def click_maruti_suzuki(self):
        self.maruti_suzuki.click()