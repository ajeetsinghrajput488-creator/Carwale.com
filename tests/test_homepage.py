from pages.home_page import HomePage

def test_home_page (page):

    page.goto("https://www.carwale.com/")

    home_page = HomePage(page)

    home_page.hover_new_cars()
    home_page.click_find_new_cars()
    home_page.move_mouse_outside()
    home_page.click_maruti_suzuki()


