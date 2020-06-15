# La structure est très simple 
# car toutes les broches sont étiquetées. 
# Gauche (GND) vient à la broche 6 du Pi (GND),
# la broche droite (VCC) vient à 3V3 (broche 1) du PI.
# Selon le nombre de relais que vous souhaitez contrôler,
# vous devez connecter un nombre correspondant de GPIO aux broches IN.
# Il est recommandé de régler une petite résistance entre le PI et le relais,
# mais ce n'est pas absolument nécessaire avec 3V3.
#
# Si vous définissez 5 V au lieu de 3,3 V sur VCC,
# vous devez absolument mettre une résistance chacun (~ 1 kΩ) 
# entre les GPIO et les broches IN.

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
