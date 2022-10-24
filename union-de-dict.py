# union de dictionnaires

dict1 = {"jean": (20, "Développeur"), "paul": (30, "Ingénieur")}
dict2 = {"Emili": (30, "Développeur"), "paul": (30, "Ingénieur")}

dict1 |= dict2
print(dict1)
