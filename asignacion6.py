# Ejercicio 1 
def promedio(*arguments):
    ## complete el código en el siguiente espacio ##
    total=0
    for number in arguments:
        total+=number
    prom = total/len(arguments)


    ################################################
    return prom

# Ejercicio 2 
def charCount(string1):
    chardict = {}
    ## complete el código en el siguiente espacio ##
    arg = string1.lower()
    for letra in arg:
        if letra in chardict:
            chardict.update({letra:chardict[letra]+1})
        else:
            chardict.update({letra:1})
    ################################################
    return chardict

# Ejercicio 3 
import requests
def getMerakiOrganizations():
    ## complete el código en el siguiente espacio ##
    response = requests.get(
    'https://api.meraki.com/api/v0/organizations',
    headers={'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'},
    )
    ################################################
    return response.text.encode('utf8')

# Ejercicio 4 
import json
def jsonExtractMerakiOrgName(jsontext):
    nameList = []
    ## complete el código en el siguiente espacio ##
    response_JSON = json.loads(jsontext)
    for organization in response_JSON:
        nameList.append(organization['name'])
    ################################################
    return nameList

# Ejecute el programa en una consola, usando el comando "python3 asignacion6.py"
# descomente los comandos "print" para probar sus funciones.
if __name__ == '__main__':
    # Prueba ejercicio 1 #########
    #print(promedio(1,2,3))

    # Prueba ejercicio 2 #########
    #print(charCount("-Aa-Bb-Cc-"))

    # Prueba ejercicio 3 #########
    #print(getMerakiOrganizations())

    # Prueba ejercicio 4 #########
    print(jsonExtractMerakiOrgName(getMerakiOrganizations()))
    #Para que se vea mejor, voy a colocar un for

    for organization in jsonExtractMerakiOrgName(getMerakiOrganizations()):
        print(organization)




