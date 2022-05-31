import random

sujetos = ["Kania", "bebé", "princess" , "mami"]
intenciones = ["yo quiero", "yo puedo", "yo vengo a", "voy a"]
verbos = ["encendelte", "amalte", "ligal", "jugal"]
advs = ["suave", "lento", "lápido", "fuelte"]
complementos1 = ["hasta que salga el sol" , "toda la noche", "hasta e l amanecer", "todo el día"]
complementos2 = ["sin anestesia", "sin compromiso", "feis to feis" , "sin miedo"]

sujetos1 = random.choice(sujetos)
intencion1 = random.choice(intenciones)
verbo1 = random.choice(verbos)
advs1 = random.choice(advs)
comp1 = random.choice(complementos1)
comp2 = random.choice(complementos2)

print( "letra generada: " + sujetos1 + " " + intencion1 + " "+ verbo1 + " " + advs1 + " " + comp1 + " " + comp2)