from testCases.Login import login
from PagesObjects.Seeall import seeall


class Test_seeall:

    def test_see_all_links(self, setup):
        login(setup)
        self.driver=seeall(setup)
        statuscodes=self.driver.checllalllinksin_Seeall()
        for i in statuscodes.keys():
            assert statuscodes[i]==200



