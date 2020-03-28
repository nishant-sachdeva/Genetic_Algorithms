import client_moodle
import json



with open('bestPopulation.txt') as new_filename:
	population = json.load(new_filename)


private_key="JVlzF9h4oeN3fyaOoSYgA1HiW82SlS1iptEqtB4lDQAeCK2k8C"


for dude in population:
	try:
		temp = client_moodle.submit(private_key, dude)
		print(temp)
	except:
		print("Could not send request")