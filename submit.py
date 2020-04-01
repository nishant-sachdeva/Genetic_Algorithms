import client_moodle
import json



with open('new_data.txt') as new_filename:
	population = json.load(new_filename)


private_key="JVlzF9h4oeN3fyaOoSYgA1HiW82SlS1iptEqtB4lDQAeCK2k8C"


for dude in range( len(population) ) :
	try:
		temp = client_moodle.submit(private_key, population[dude])
		print(str(dude) + " " + temp)
	except:
		print("Could not send request")