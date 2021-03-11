import requests
import sys

def getTemplates(baseurl, token):

    url = f"{baseurl}/dna/intent/api/v1/template-programmer/template"
    payload={}
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    return response.text

def getTemplateDetails(baseurl, token, templateId):

    url = f"{baseurl}/dna/intent/api/v1/template-programmer/template/{templateId}"
    payload={}
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': token
    }

    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

    return response.text



if __name__ == '__main__':
    print(getIssues(sys.argv[1],sys.argv[2]))