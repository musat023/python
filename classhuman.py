#class Human:

#    def _init_(self, fname, lname):
#        self.first_name = fname
#        self.last_name = lname

#    def _str_(self):
#        return f"{self.first_name} {self.last_name}"

#    def set_name(self, new_fname, new_lname):
#        self.first_name = new_fname
#        self.last_name = new_lname

#h = Human("Petr", "Kozák")
##h.first_name = "Petra"
##h.last_name = "Kozákova"
#print(h)

#h2 = Human("jan", "z Vysočan")
#print(h2)








class Character:

    def _init_(self, name, universe, power):
        self.character_name = name
        self.character_universe = universe
        self.character_power = power

    def _str_(self):
        return f"{self.character_name}, {self.character_universe}, {self.character_power}"
    
ch = Character("Thor", "Marvel", "Mjolnir")
ch2 = Character("Spiderman", "Marvel", "cobweb")

print(ch)
print(ch2)