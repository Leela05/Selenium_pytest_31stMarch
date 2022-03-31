from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture
def setUp():
    global driver,movie_name, year, director_name, distributor, producer
    movie_name = input("Enter Name:")
    year = input("Enter year:")
    director_name = input("Enter director name")
    distributor = input("Enter distributor name:")
    producer = input("Enter producer name:")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(2)
    driver.find_element_by_name("mname").send_keys(movie_name)
    time.sleep(2)
    driver.find_element_by_name("myear").send_keys(year)
    time.sleep(2)
    driver.find_element_by_name("mdirector").send_keys(director_name)
    time.sleep(2)
    driver.find_element_by_name("mdist").send_keys(distributor)
    time.sleep(2)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[4]").click()
    time.sleep(2)
    driver.find_element_by_name("subbtn").click()
    time.sleep(2)

