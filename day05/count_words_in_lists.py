from collections import Counter

celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

counts = Counter(celestial_objects)

for key, value in counts.items():
    print("{:<12} {}".format(key,value))
