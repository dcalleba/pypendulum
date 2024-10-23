import pendulum

#dcallebautdanielrobert
# Obtenir la date et l'heure actuelles
maintenant = pendulum.now()
print("Date et heure actuelles : ", maintenant)

# Ajouter du temps à une date
dans_une_semaine = maintenant.add(weeks=1)
print("Date et heure dans une semaine : ", dans_une_semaine)

# Formater une date
date_formatee = maintenant.format('DD.MM.YYYY HH:mm:ss')
print("Date formatée : ", date_formatee)

# Différence entre deux dates
diff = pendulum.now() - pendulum.parse('1949-03-20')
print("Il s'est écoulé ", diff.in_words(), " depuis le 1er janvier 2022.")

# Parser une date en string
date_en_string = '2025-04-03'  # format: YYYY-MM-DD
date_parsee = pendulum.parse(date_en_string)
print("La date parsée est : ", date_parsee)
print("ok")