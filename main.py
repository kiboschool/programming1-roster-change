# See the Instructions tab.
# Scroll down to see where you should write your solution
roster = [
  "Thibaut Courtois",
  "Dani Carvajal",
  "Brahim Díaz",
  "Éder Militão",
  "Jesús Vallejo",
  "Nacho",
  "Eden Hazard",
  "Toni Kroos",
  "Karim Benzema",
  "Takefusa Kubo",
  "Álvaro Odriozola",
  "Luka Modrić",
  "Marco Asensio",
  "Marcelo",
  "Andriy Lunin",
  "Martin Ødegaard",
  "Casemiro",
  "Federico Valverde",
  "Luka Jović",
  "Sergio Ramos",
  "Lucas Vázquez",
  "Gareth Bale",
  "Dani Ceballos",
  "Vinícius Júnior",
  "Raphaël Varane",
  "Rodrygo",
  "Isco",
  "Ferland Mendy",
  "Mariano"
]

# Write your solution below

# Print the current roster
print("\nThe current Real Madrid roster:\n")
for player in roster:
  print(player)

# Remove players using pop()
roster.pop(24)
roster.pop(19)
roster.pop(15)
roster.pop(10)
roster.pop(9)
roster.pop(2)

# Add players using append()
roster.append("Eduardo Camavinga")
roster.append("David Alaba")


# Print the new roster
print("\n------")
print("\nThe new Real Madrid roster:\n")
for player in roster:
  print(player)