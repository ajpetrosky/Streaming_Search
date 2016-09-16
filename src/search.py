import webbrowser
import sys
import argparse

#@author AndrewPetrosky

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument('--movie', action='store_true')
	parser.add_argument('title')

	args = parser.parse_args()

	webbrowser.open('https://www.netflix.com/search/' + args.title)
	webbrowser.open('https://www.amazon.com/s/ref=nb_ss_gw/102-1882688-6100927?initialSearch=1&url=search-alias%3Daps&field-keywords='
		+ args.title + '&Go.x=0&Go.y=0&Go=Go')
	#https://www.hbonow.com/feature/PROD775717/sisters?cid=undefined

if __name__ == "__main__":
 	main()