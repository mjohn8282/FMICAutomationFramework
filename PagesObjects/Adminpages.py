import  requests
from Utilities.CustomLogger import logs

class Adminpages:

    Adminpages_xpath="//div[@id='divHomeMenu']/div[4]/ul/li[4]"

    def __init__(self,driver):
        self.driver=driver

    def test_checklinks_adminpages(self):
        self.driver.find_element_by_xpath(Adminpages.Adminpages_xpath).click()
        links = self.driver.find_elements_by_xpath(".//a")
        for i in links:
            href = str(i.get_attribute('href'))
            if href.__contains__('Logoff.aspx') or href.__contains__(str(None)):
                continue
            else:
                status = requests.get(href).status_code
                logs.loggen().info(href + " Status code " + str(status))

