import time

from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Browsers\chromedriver.exe')


def test():
    try:
        driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element_by_class_name('search-keyword').send_keys('ber')
        time.sleep(1)
        add_to_cart_items = driver.find_elements_by_xpath("//*[text()='ADD TO CART']")
        for i in add_to_cart_items:
            i.click()
        driver.find_element_by_class_name('cart-icon').click()
        driver.find_element_by_xpath("//*[text()='PROCEED TO CHECKOUT']").click()
        number_of_products = driver.find_elements_by_class_name('product-name')
        products_names = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
        for i in number_of_products:
            if i.text in products_names:
                print(f'{i.text} is found, marking as ok.')
        print('tada!!! Test successful....')
        amount = driver.find_element_by_class_name('discountAmt').text
        driver.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
        driver.find_element_by_class_name('promoBtn').click()
        time.sleep(8)
        amount_after_applying_discount = driver.find_element_by_class_name('discountAmt').text
        time.sleep(2)
        if float(amount_after_applying_discount) < int(amount):
            print('Closing the test as the discount is successfully applied')
            # This is the code for table xpath viewing
        manual_total_amount = driver.find_elements_by_xpath('//tr/td[5]/p')
        manual_total_amount_in_int = 0
        for i in manual_total_amount:
            manual_total_amount_in_int += float(i.text)
        if manual_total_amount_in_int == int(amount):
            print('Total amount matches')

    except Exception as e:
        print(e)
    finally:
        driver.close()


if __name__ == '__main__':
    test()
