#!python3

from DNACsystem import getToken
from DNACintent import getTemplates, getTemplateDetails
import json
from includes import baseurl, dnac_user, dnac_password

if __name__ == '__main__':
    #
    # Log into DNAC and pull a list of templates
    #
    token = json.loads(getToken(baseurl, dnac_user, dnac_password))['Token']
    jtemplates = json.loads(getTemplates(baseurl, token))

    # print(json.dumps(jtemplates, indent=2))
    tempnum = 0
    for template in jtemplates:
        print(f"{tempnum} - {template['name']}:  {template['templateId']}")
        tempnum += 1

    #
    # prompt user to choose a template and print the text content of the template
    #

    choice = 0
    while choice != 100:
        choice = int(input('Which template? '))
        if choice == 100:
            exit()
        templateDetail = json.loads(getTemplateDetails(baseurl, token, jtemplates[choice]['templateId']))
        #print(json.dumps(templateDetail, indent=2))
        print(templateDetail['templateContent'])
