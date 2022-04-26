import random

lambetazo = ["Queridos", "Apreciados", "Distinguidos", "Honorables", "Estimados", "Respetados"]  #se define una lista
potenciales_marranos = ["compatriotas ", "conciudadanos", "amigos", "coterraneos", "copartidarios", "electores"]
condicion = ["en mi gobierno", "con su apoyo", "siendo elegido", "con su ayuda", "si me siguen", "durante mi mandato"]
compromiso = ["voy a derrotar", "venceré", "eliminaré", "acabaré", "luncharé contra", "combatiré"]
ilusion_guerrero = ["la violencia y", "la delincuencia y", "la corrupción y", "la inflacion y", "la pobreza y", "el desplazamiento"]
promesa = ["trabajaré por", "garantizaré", "protegeré", "velaré por", "promoveré", "defenderé"]
beneficio = ["la educacion", "el empleo", "la seguridad", "la paz", "la igualdad", "la salud"]
dependiendo_votos = ["del pais", "de la ciudad", "de la comunidad", "de la poblacion", "para toda la gente", "de cada colombiano"]

lambetazo_selecc = random.choice(lambetazo) #se utiliza la librería para seleccionar un elemento al azar de la lista sujetos
marranos_selecc = random.choice(potenciales_marranos)
condiciones_selecc = random.choice(condicion)
compromiso_selecc = random.choice(compromiso)
ilusion_guerrero_selecc = random.choice(ilusion_guerrero)
promesa_selecc = random.choice(promesa)
beneficio_selecc = random.choice(beneficio)
dependiendo_votos_selecc = random.choice(dependiendo_votos)

print("letra generada: " + lambetazo_selecc + " " + marranos_selecc + " " + condiciones_selecc + " " + compromiso_selecc + " " + ilusion_guerrero_selecc + " " + promesa_selecc + " " + beneficio_selecc + " " + dependiendo_votos_selecc )