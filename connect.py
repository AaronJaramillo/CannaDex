### DB layer 

for connecting to a different database for userprofiles and biometrics




Get_url = "https://www.smokereports.com/api/v1.0/strains/VUJCJ4MPQ2000000000000000"

def getStrain(Get_url):

	strain_info = requests.get(Get_url)
	info = json.loads(strain_info.text)
	#print(json.dumps(info, sort_keys=True, indent=4))
	info = info['data']
	#strain_name = i
	strain_name = info['name']

	strain_genes = info['genetics']['names']

	strain_nationality = info['lineage']

	company = info['seedCompany']['name']

	print("The strain", strain_name, "is a prime cross of", strain_genes, "originally from the", strain_nationality, "region, it's high quality genetics were brought to market by", company)



getStrain(Get_url)