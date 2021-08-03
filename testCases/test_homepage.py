from testCases.Login import login
from PagesObjects.Homepage import Homepage

class Test_home:

    def test_gethomelink(self, setup):
        login(setup)
        self.driver=Homepage(setup)
        self.driver.CheckHomepage_links()

