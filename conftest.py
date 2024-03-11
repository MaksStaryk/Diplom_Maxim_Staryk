

@pytest.fixture(autouse=False)
def driver_chrome():
    print('Start driver GoogleChrome\n')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()

    print('Finish')