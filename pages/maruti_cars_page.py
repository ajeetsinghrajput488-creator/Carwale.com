from playwright.sync_api import Page, expect

class MarutiCarsPage:

    def __init__(self, page:Page):
        self.page =  page
        self.new_cars = page.locator('//div[@class="o-os o-js o-jy o-kF o-mo o-ef o-bS o-co o-mJ dvEJRN"]').nth(0)
        self.find_new_cars = page.locator("//div[contains(text(),'Find New Cars')]")
        self.maruti_suzuki = page.locator('//img[@title="Maruti Suzuki Cars"]')
        self.maruti_car_models_heading = page.get_by_role("heading", name="Maruti Car Models", exact=True)
        self.maruti_baleno_tab = page.locator('//img[@alt="Maruti Suzuki Baleno"]')
        # self.view_price_breakup = page.locator ('//button[@title="Maruti Suzuki Baleno Price in Delhi"]')
        self.view_images_breakup = page.locator ('//span[@class="o-jK o-j1" and @fs="12"]').nth(1)
        self.view_seats_tab = page.locator ('//span[@title="Seats"]').nth(0)

    def hover_new_cars(self):
        self.new_cars.hover()

    def click_find_new_cars(self):
        self.find_new_cars.click()

    def move_mouse_outside(self):
        self.page.mouse.move(0 , 0)

    def click_maruti_suzuki(self):
        self.maruti_suzuki.click()

    def verify_maruti_car_models_heading(self):
        expect(
            self.maruti_car_models_heading).to_be_visible()

    def click_maruti_baleno(self):
        self.maruti_baleno_tab.click()

    def click_view_images_breakup(self):
        self.view_images_breakup.click()

    def click_images_tab(self):
        self.view_seats_tab.click()



