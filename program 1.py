import xml.dom.minidom
import datetime
import random

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        return False

doc = xml.dom.minidom.Document()
x = random.randint(0, 99999)
xy = str(x)

print('------ Greenvale Police Department ------\n')
print('------ Create Report ------\n')
crime = doc.createElement('crime')
doc.appendChild(crime)



crime.setAttribute('id', xy)

crimeType = doc.createElement('crimeType')
victim = doc.createElement('victim')
offender = doc.createElement('offender')
witness = doc.createElement('witness')
evidence = doc.createElement('evidence')
location = doc.createElement('location')
date = doc.createElement('date')
comments = doc.createElement('comments')

crime.appendChild(date)
crime.appendChild(crimeType)
crime.appendChild(victim)
crime.appendChild(offender)
crime.appendChild(witness)
crime.appendChild(evidence)
crime.appendChild(location)
crime.appendChild(comments)


print("1. Theft\n2. Violence\n3. Criminal Damage\n4. Drug Offense\n5. Fraud\n6. Other\n")
cType = input("Enter crime type: ")

setCType = doc.createTextNode(cType)
crimeType.appendChild(setCType)

#Checks if date entered is valid
incorrectDate = True
while incorrectDate ==True:
    dateOfOffence = input("Enter the date of the offence. Please use the format DD/MM/YYYY: ")
    
    if validate(dateOfOffence) == True:
        incorrectDate = False

setDateOfOffence = doc.createTextNode(dateOfOffence)
date.appendChild(setDateOfOffence)

if cType in ("f","Fraud", "F","fraud", "Criminal Damage", "criminal damage", "Criminal damage"):

    damage = doc.createElement('damage')    
    damageCost = doc.createElement('damageCost')
    crime.appendChild(damage)
    damage.appendChild(damageCost)

    inputDamageCost = input("Enter the cost of the criminal damage or fraud: (do not include £)")
    setDamageCost = doc.createTextNode(inputDamageCost)
    damageCost.appendChild(setDamageCost)

#Species circumstances for theft
if cType == "Theft" or cType == "theft":

    #Elements specific to theft created
    itemStolen = doc.createElement('itemStolen')
    itemDesc = doc.createElement('itemDesc')
    itemColour = doc.createElement('itemColour')
    itemMake = doc.createElement('itemMake')
                                
    #Elements specific to theft appended
    crime.appendChild(itemStolen)
    itemStolen.appendChild(itemDesc)
    itemStolen.appendChild(itemColour)
    itemStolen.appendChild(itemMake)

    #Text added to nodes
    inputItemDesc = input("Enter stolen item's description.\nEnter 'vehical' to include details specific to vehical theft: ")
    setItemDesc = doc.createTextNode(inputItemDesc)
    itemDesc.appendChild(setItemDesc)

    #Checks if stolen item is a vehical for use in dialog
    isCar = "item"
    if inputItemDesc == "vehical" or inputItemDesc == "Vehical":
        isCar = "vehical"

    inputItemColour = input("Enter colour of stolen " + isCar +": ")
    setItemColour = doc.createTextNode(inputItemColour)
    itemColour.appendChild(setItemColour)
                                 
    inputItemMake = input("Enter the make of the stolen " + isCar +": ")
    setItemMake = doc.createTextNode(inputItemMake)
    itemMake.appendChild(setItemMake)    

    
    #Elements specific to vehical theft
    if inputItemDesc == "vehical" or inputItemDesc == "Vehical":
        itemReg = doc.createElement('itemReg')
        itemModel = doc.createElement('itemModel')

        itemStolen.appendChild(itemReg)
        itemStolen.appendChild(itemModel)
                                  
        inputItemModel = input("Enter the model of the stolen vehical: ")
        setItemModel = doc.createTextNode(inputItemModel)
        itemModel.appendChild(setItemModel)    
        
        inputItemReg = input("Enter the registration of the stolen vehical: ")
        setItemReg = doc.createTextNode(inputItemReg)
        itemReg.appendChild(setItemReg)




cVictim = input("Enter victim(s): ")
setCVictim = doc.createTextNode(cVictim)
victim.appendChild(setCVictim)


offenderName = doc.createElement('offenderName')
offenderDoB = doc.createElement('offenderDoB')
offenderSex = doc.createElement('offenderSex')
offenderAddress = doc.createElement('offenderAddress')

offender.appendChild(offenderName)
offender.appendChild(offenderDoB)
offender.appendChild(offenderSex)
offender.appendChild(offenderAddress)


inputOffenderName = input("Enter the offender's name: ")
setOffenderName = doc.createTextNode(inputOffenderName)
offenderName.appendChild(setOffenderName)

dateCheck = True
while dateCheck == True:
    inputOffenderDoB = input("Enter the offender's date of birth: ")
    if validate(inputOffenderDoB) is True:
        dateCheck = False
setOffenderDoB = doc.createTextNode(inputOffenderDoB)
offenderDoB.appendChild(setOffenderDoB)

#Does not work for some reason
sexCheck = True
while sexCheck == True:
    inputoffenderSex = input("Enter the offender's sex (male/female): ")
    if inputoffenderSex in ("m","f","Male","Female","M","F","male","female"):
        sexCheck = False
setoffenderSex = doc.createTextNode(inputoffenderSex)
offenderSex.appendChild(setoffenderSex)

inputoffenderAddress = input("Enter the offender's address: ")
setoffenderAddress = doc.createTextNode(inputoffenderAddress)
offenderAddress.appendChild(setoffenderAddress)


cWitness = input("Enter witness(es): ")
setCWitness = doc.createTextNode(cWitness)
witness.appendChild(setCWitness)

cEvidence = input("Enter evidence: ")
setCEvidence = doc.createTextNode(cEvidence)
evidence.appendChild(setCEvidence)

cLocation = input("Enter location: ")
setCLocation = doc.createTextNode(cLocation)
location.appendChild(setCLocation)

inputComments = input("Enter any further comments for this report: ")
setComments = doc.createTextNode(inputComments)
comments.appendChild(setComments)

# Saves XML file
filename = input("Enter filename: ")
if ".xml" not in filename:
    filename = filename + ".xml"

doc.writexml( open(filename, 'w'),
               indent="    ",
               addindent="    ",
               encoding="UTF-8",
               newl='\n')

#Early cleanup of the objects which are now no longer needed
doc.unlink()
