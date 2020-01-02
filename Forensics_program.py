characteristics = {"hair": {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"},
                   "face": {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"},
                   "eyes": {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"},
                   "gender": {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"},
                   "race": {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}}


people = {'Eva': {'hair': 'blonde', 'face': 'oval', 'eyes': 'blue', 'gender': 'female', 'race': 'white'},
          'Larisa': {'hair': 'brown', 'face': 'oval', 'eyes': 'brown', 'gender': 'female', 'race': 'white'},
          'Matej': {'hair': 'black', 'face': 'oval', 'eyes': 'blue', 'gender': 'male', 'race': 'white'},
          'Miha': {'hair': 'brown', 'face': 'square', 'eyes': 'green', 'gender': 'male', 'race': 'white'}}

with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()

perpetrator = []

for key, value in characteristics.items():
    for key, value in value.items():
        if value in dna:
            perpetrator.append(key)

for key, value in people.items():
    if set(value.values()) == set(perpetrator):
        print(f'{key} is the perpetrator.')
