import client_moodle
import json

private_key="JVlzF9h4oeN3fyaOoSYgA1HiW82SlS1iptEqtB4lDQAeCK2k8C"
lol = [0.0, -0.003042220897435867, 0.004020255328129496, 0.04865164537726995, 0.00010426485081555187, -5.79641553758037e-09, 3.0199854510495646e-08, 7.167533211339566e-13, -2.7670322726536744e-11, 1.7159164997190694e-14, 5.164450739281546e-17]
retval = client_moodle.get_errors(private_key, lol)
retval1=client_moodle.submit(private_key, lol)
print(retval, retval1)