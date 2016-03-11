'''
Checking simple Lead service flow using Base API Client
    0. Gather Auth. token, proper lead data and so on
    1. Build a client
    2. Create a new lead
    3. Check if status is set as "new"
    4. Change status value
    5. Valide if status has been changed correctly
'''

__author__ = 'Dawid Pacia'

import time
import unittest

from common import leadsServiceLib


class testLeadService(unittest.TestCase):

    def setUp(self):
        self.authToken = 'c732e3bc1548357f75337c121d9e60965ff6b3511572d7e716878c59611a8875'
        self.newStatus = 'Working'
        self.firstLeadData = 'leadData.json'

    def testSingleLeadFlow(self):
        client = leadsServiceLib.leadsServices(authToken=self.authToken)
        clientID = client.createLead(self.firstLeadData, verbose=False, deleteFlag=True)
        client.readUserParameter(clientID, "status", toCompare="New")
        client.setParameter(clientID, "status", self.newStatus)
        client.readUserParameter(clientID, "status", toCompare=self.newStatus)
        #client.removeAllLeads()
        time.sleep(1) #just to aviod logs mixing

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
