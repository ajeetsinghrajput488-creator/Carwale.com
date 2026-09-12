from pages.maruti_cars_page import MarutiCarsPage

def test_maruti_cars (page):

    page.goto("https://www.carwale.com/")

    maruti_cars_page = MarutiCarsPage(page)

    maruti_cars_page.hover_new_cars()
    maruti_cars_page.click_find_new_cars()
    maruti_cars_page.move_mouse_outside()
    maruti_cars_page.click_maruti_suzuki()

    maruti_cars_page.verify_maruti_car_models_heading()

    maruti_cars_page.click_maruti_baleno()
    maruti_cars_page.click_view_images_breakup()
    maruti_cars_page.click_images_tab()
