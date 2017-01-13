####kivyMain.py

### Holds the UI and UX driver functions

#############
#
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import cannabisAPI as cann
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput
from kivy.graphics import Line
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
import json

# class Cannadex(GridLayout):
# 	def __init__(self, **kwargs):
# 		super(Cannadex, self).__init__(**kwargs)
		 
# 		self.add_widget(Label(text="Search: "))
# 		self.search = TextInput(multiline=False)
# 		self.add_widget(self.search)
# 		
# 		

Builder.load_file("kivyMain.kv")

#searchResults = Builder.load_file("searchresults.kv")

class SearchScreen(Screen):
	pass

class ResultScreen(Screen):
	pass

class StrainProfile(Screen):
	pass

class ReviewScreen(Screen):
	pass

class kivyMain(App):
	results = ['none'] * 10
	resultNames = []
	def build(self):
		self.sm = ScreenManager()
		self.sm.add_widget(SearchScreen(name='searcher'))
		
		return self.sm
	def getImages(self, src):
		image = AsyncImage(source=src)
		return image
	def setImages(self):
		self.strain_image = self.getImages(self.strain.strain_image)
		##add children via ucpc lookup
	def searched(self, searchTerm):
		self.strain = cann.Profile()
		
		self.results = cann.search(searchTerm)
		x = 0 

		while x < len(self.results):
			name = self.results[x]
			try:
				self.resultNames.append(name['name'])
			except TypeError:
				pass
			x += 1
		self.resultlen = len(self.resultNames)
		self.sm.add_widget(ResultScreen())
		return self.sm

	def profileOut(self, index):
		strain_obj = self.results[index]
		lookup = strain_obj['ucpc']
		self.strain.profile_out("strains", lookup) 
		try:
			for i in self.strain.effects:
				output = self.strain.level_out(self.strain.effects[i], self.strain.levels[i])
				self.flavor.add_widget(Button(text=output, height='100sp'))
			self.flavor.size = (1, 1)
		except:
			pass
		self.sm.add_widget(StrainProfile(name='Profile'))
		return self.sm
		
	def reviewStrain(self):
		self.strain.get_reviews(self.strain.Get_url)
		self.sm.add_widget(ReviewScreen(name='Reviews'))
		return self.sm
if __name__ == "__main__":
	kivyMain().run()
