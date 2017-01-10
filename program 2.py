print('------ Greenvale Police Department ------\n')

from xml.dom import minidom

address = input("Please enter filename: ")
if ".xml" in address:
    address = "C:\\Users\\Elliot\\Desktop\\CrimeDatabase\\" + address
else:address = "C:\\Users\\Elliot\\Desktop\\CrimeDatabase\\" + address + ".xml"

doc = minidom.parse(address)

print()

crimes = doc.getElementsByTagName("crime")

for crime in crimes:
    crimeType = crime.getElementsByTagName("crimeType")[0]
    victim = crime.getElementsByTagName("victim")[0]
    witness = crime.getElementsByTagName("witness")[0]
    evidence = crime.getElementsByTagName("evidence")[0]
    location = crime.getElementsByTagName("location")[0]

    print("Type: %s\nVictim: %s\nWitness: %s\nEvidence: %s\nLocation: %s" % (crimeType.firstChild.data,
                    victim.firstChild.data, witness.firstChild.data, evidence.firstChild.data, location.firstChild.data))


if crimeType.firstChild.data == "Theft":
    items = doc.getElementsByTagName("itemStolen")

    for itemStolen in items:
        itemDesc = itemStolen.getElementsByTagName("itemDesc")[0]
        itemColour = itemStolen.getElementsByTagName("itemColour")[0]
        itemReg = itemStolen.getElementsByTagName("itemReg")[0]
        itemMake = itemStolen.getElementsByTagName("itemMake")[0]
        itemModel = itemStolen.getElementsByTagName("itemModel")[0]


        if itemDesc.firstChild.data =="Car":
            print ("\nAdditional information for car theft:")
            print ("Car Colour: %s\nCar Registration: %s\nMake: %s\nModel: %s\n" % (itemColour.firstChild.data,
                                itemReg.firstChild.data, itemMake.firstChild.data, itemModel.firstChild.data))
            
        elif itemDesc.firstChild.data != "Car":
            print ("Item description: %s\nColour: %s\nMake: %s"% (itemDesc.firstChild.data,
                                    itemColour.firstChild.data, itemMake.firstChild.data))

else: print ("Not a theft")

print ("\nThank you for using this crime reporting system")
