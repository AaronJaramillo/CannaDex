
#Cannabis api

import requests
import json


##### RETREIVING STRAIN SPECIFIC INFO ###############

class Profile:
	### name, genetics Lineage, company, rating 
	#### user specifics
	
	start_url = "https://www.smokereports.com/api/v1.0/"
	api = "a7a31d7e1698e5e65e4523fbb0edfcb1b7fe53e4"
	##types = strains, dispo, comp, extracts, edibles

	def get_raw_info(self, types, lookup_id):
		self.Get_url = Profile.start_url + types + "/" + lookup_id
		self.raw_info = requests.get(self.Get_url)
		self.text_info = self.raw_info.text
		self.json_data = json.loads(self.text_info)
		#print(json.dumps(self.json_data, sort_keys=True, indent=4))
		
		if types == "strains":
			self.strain_info = self.json_data['data']
###### clickable
	def get_reviews(self, lookup_url):
		review_url = lookup_url + '/reviews'
		self.review_info = requests.get(review_url)
		self.review_info = self.review_info.text
		self.review_json = json.loads(self.review_info)
		self.reviews = self.review_json['data']
		self.reviews_meta = self.review_json['meta']
		self.review_count = self.reviews_meta['pagination']['count']
		self.euphoria = self.reviews['euphoria']
		self.creativity = self.reviews['creativity']
		self.pain_relief = self.reviews['pain_relief']
		self.appetite_gain = self.reviews['appetite_gain']
		self.calming = self.reviews['calming']
		self.anxiety = self.reviews['anxiety']
		self.earthy = self.reviews['earthy']
		self.spicy = self.reviews['spicy']
		self.fruity = self.reviews['fruity']
		self.sour = self.reviews['sour']
		self.dry_mouth = self.reviews['dry_mouth']

	def get_effects(self, lookup_id):
		self.effects = []
		self.levels = []
		self.flavor_url = Profile.start_url + "strains/" + lookup_id + "/effectsFlavors"
		self.flavors = requests.get(self.flavor_url)
		#self.flavors_json = json.loads(self.flavors.text)

		self.flavors_json = json.loads(self.flavors.text)
		self.flavors_json = self.flavors_json['data']
	

		if type(self.flavors_json) is bool:
			pass
		else:

			for key in self.flavors_json.keys():
				self.effects.append(key)
				self.levels.append(self.flavors_json[key])

		

				
		# for category, level in self.flavors_json['data']:
		# 	self.effects.append(category)
		# 	self.levels.append(level)



		#self.flavors_json = self.flavors_json['data']
		# self.euphoria = self.flavors_json['euphoria']
		# self.creativity = self.flavors_json['creativity']
		# self.munchies = self.flavors_json['appetite_gain']

	def parseStrain_info(self):
		
		self.strain_name = self.strain_info['name']

		self.strain_genes = self.strain_info['genetics']['names']

		self.strain_nationality = self.strain_info['lineage']

		self.company = self.strain_info['seedCompany']['name']

		self.strain_image = self.strain_info['image']

		self.strain_reviews = self.strain_info['reviews']['count']

	def level_out(self, effect, level):
		############ PASS THROUGH Entire OBJECT INSTEAD DONT FORGET IDIOT######
		if level is None:
			pass
		else:

			lev = float(level)
			lev = int(lev)
			level_bar = "="
			print(effect,": ", lev)
			x = 1
			while x < lev:
				level_bar = level_bar + "="
				x = x+1
			print(level_bar)
			output = effect + ": " + str(lev)

			return output

	def profile_out(self, types, lookup_id):

		self.get_raw_info(types, lookup_id)
		self.parseStrain_info()
		self.get_effects(lookup_id)
		print("========================", self.strain_name, "==========================")
		print("Name: ", self.strain_name)
		print("Genetics: ", self.strain_genes)
		print("Region: ", json.dumps(self.strain_nationality, sort_keys=True, indent=4))
		print("Company: ", self.company)
		x = 0
		while x < len(self.effects):
			self.level_out(self.effects[x], self.levels[x])
			x += 1
		print("======================================================================")




def search(keyWord):
	#search = input("Enter a Strain to Search for: ")
	search = keyWord
	strain_info = requests.get("https://www.smokereports.com/api/v1.0/strains/search/" + search)
	return searchResults(strain_info)

def searchData(meta):
	searchStats = "Total: " + str(meta['total']) + " - Current Page: " + str(meta['current_page']) + " - total pages: " + str(meta["total_pages"])
	print(searchStats)
	return searchStats

def searchResults(getRequest):
	results = []
	
	info = json.loads(getRequest.text)
	try:
		meta = info["meta"]["pagination"]
		info = info["data"]
	except:
		pass
	try:
		metaSearch = searchData(meta)
	except:
		pass

	x = 0
	while x < len(info):
		# print(x,": ",info[x]['name'])
		results.append(info[x])
		x = x+1 
	try:
		results.append(metaSearch)
	except (TypeError, KeyError):
		pass
	try:
		results.append(meta['links']['previous'])
	except (TypeError, KeyError) as e:
		pass
	try:
		results.append(meta['links']['next'])
	except (TypeError, KeyError):
		pass
		
	return results

def choose(resultList):
	select = input("Select the strain number you want or type 'previous'/'next': ")

	if select == 'next':

		r = requests.get(resultList[-1])
		return choose(searchResults(r))

	if select == 'previous':
		r = requests.get(resultList[-2])
		return choose(searchResults(r))

	select = int(select)

	if select > 0 and select < 9:
		print(select)
		select = int(select)
		return resultList[select]


# def main():
# 	strain = Profile()

# 	results = []
# 	print("=======================Welcome to CANNADEX============================")
# 	results = search() 
# 	# strain.profile_out("strains", "VUJCJ4TYMG000000000000000")
# 	print("======================================================================")
# 	#select = choose(results)

# 	strain.profile_out("strains", choose(results))




# main()





	





