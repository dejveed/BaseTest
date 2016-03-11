import basecrm
import json
from commonMethods import datePrinter, loadJsonData

class leadsServices:
    def __init__(self, authToken):
        self.client = basecrm.Client(access_token=authToken, timeout=60)
        self.allowedParams = ['address', 'custom_fields', 'description', 'email', 'facebook', 'fax', 'first_name',
                              'industry', 'last_name', 'linkedin', 'mobile', 'organization_name', 'owner_id', 'phone',
                              'skype', 'status', 'tags', 'title', 'twitter', 'website']
        self.allowedStatus = ['New', 'Working', 'Unqualified']

    def createLead(self, fileData, deleteFlag=False, verbose=False):
        """
        :param bool deleteFlag: (optional) Remove users with the same first name, second name and company name Default: False.
        :param bool verbose: (optional) Verbose/debug mode. Default: False.
        """
        try:
            leadData = loadJsonData(fileData)
            leadList = self.client.leads.list()
        except ValueError as e:
            print "[ERROR] " + datePrinter() + " " + str(e) + ". Check data file!"
        if deleteFlag == True:
            for lead in leadList:
                try:
                    if leadData["first_name"] == lead["first_name"] and leadData["last_name"] == \
                            lead["last_name"] and leadData["organization_name"] == lead["organization_name"]:
                        self.client.leads.destroy(lead["id"])
                        if verbose==True:
                            print "[DEBUG] " + datePrinter() + " Lead removed properly. Deleted lead data: " + json.dumps(lead, indent=4)
                        else:
                            print "[DEBUG] " + datePrinter() + " Name: " + str(lead["first_name"]) + " " + \
                                  str(lead["last_name"]) + ", Company: " + str(lead["organization_name"]) + ", Succesfully removed!"
                except:
                    pass
        try:
            client = self.client.leads.create(leadData)
            if verbose == True:
                print "[DEBUG] " + datePrinter() + " Lead added properly. New lead data: " + json.dumps(leadData, indent=4)
            else:
                print "[DEBUG] " + datePrinter() + " Lead added properly. ID number: " + str(client["id"])
            return client["id"]
        except AssertionError as e:
            print e

    #if neccessary -> easy refactor code to read multiple values - dictionaries
    def readUserParameter(self, userID, parameterName, toCompare = None):
        """
        :param str toCompare: (optional) Compare with read value. Default: None.
        """
        try:
            parameterValue = self.client.leads.retrieve(userID)[parameterName]
        except NameError as e:
            print e
        if toCompare!= None:
            assert parameterValue == toCompare, "[ERROR] " + datePrinter() + " Parameter: " + parameterName + \
                                                ", is already set as: " + parameterValue + ", while should be: " + toCompare
        print "[DEBUG] " + datePrinter() + " Parameter: " + parameterName + ", is set as: " + parameterValue

    #if neccessary -> easy refactor code to set multiple values - dictionaries
    def setParameter(self, userID, parameterName, parameterValue):
        assert parameterName in self.allowedParams, "[ERROR] " + datePrinter() + " Chosen parameter incorrect: " + parameterName
        if parameterName == "status" and parameterValue not in self.allowedStatus:
            print "[WARNING] " + datePrinter() + " Not recognized status:  " + parameterValue
        try:
            self.client.leads.update(userID,{parameterName: parameterValue})
            print "[DEBUG] " + datePrinter() + " Parameter: " + parameterName + ", is settnig as: " + parameterValue
        except ValueError as e:
            print e

    def removeAllLeads(self, verbose=False):
        leadList = self.client.leads.list()
        for lead in leadList:
            self.client.leads.destroy(lead["id"])
            if verbose==True:
                print "[DEBUG] " + datePrinter() + " Lead removed properly. Deleted lead data: " + json.dumps(lead, indent=4)
            else:
                print "[DEBUG] " + datePrinter() + " Name: " + str(lead["first_name"]) + " " + str(lead["last_name"]) + \
                  ", Company: " + str(lead["organization_name"]) + ". Succesfully removed!"
