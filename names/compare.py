str1 = "Abel Newman, Addison Clarke, Ahmad Watts, Aleah Valentine, Ali Collier, Alvaro Robbins, Amiah Hobbs, Andre Carrillo, Ashlee Randall, Aydan Calderon, Camryn Doyle, Carley Gallegos, Carsen Tyler, Clay Wilkinson, Cloe Norris, Daphne Hamilton, Dashawn Green, Davion Arias, Devyn Aguirre, Diego Chaney, Dulce Hines, Eden Howe, Franklin Cooper, Giancarlo Warren, Grace Bridges, Hallie Vazquez, Hayley Morgan, Irvin Krause, Jaden Hawkins, Jadyn Mays, Jaydin Sawyer, Jordin Schneider, Josie Cole, Josie Dawson, Justine Soto, Kale Sawyer, Kameron Osborne, Leia Foley, Lennon Hunt, Leon Cochran, Logan Morrow, Luciana Ford, Malcolm Nelson, Malcolm Tucker, Maliyah Serrano, Marisol Morris, Marley Rivers, Megan Porter, Nathalie Little, Nelson Acevedo, Pablo Berg, Peyton Lloyd, Piper Hamilton, Ralph Roth, Raven Christensen, River Johnson, Salma Meza, Sanai Harrison, Selah Hansen, Trace Gates, Victoria Roach, William Maldonado, Winston Austin, Zara Suarez"

str2 = "Ahmad Watts, Franklin Cooper, Jaydin Sawyer, Sanai Harrison, Jaden Hawkins, Cloe Norris, Pablo Berg, Giancarlo Warren, Camryn Doyle, Aleah Valentine, Grace Bridges, Daphne Hamilton, Irvin Krause, Justine Soto, Josie Cole, Winston Austin, Ashlee Randall, Leon Cochran, Kale Sawyer, Alvaro Robbins, Malcolm Tucker, Jadyn Mays, Josie Dawson, Clay Wilkinson, Logan Morrow, Salma Meza, Trace Gates, Hayley Morgan, Dulce Hines, Abel Newman, Nathalie Little, Zara Suarez, Leia Foley, William Maldonado, Marley Rivers, Addison Clarke, Kameron Osborne, Aydan Calderon, Ali Collier, Marisol Morris, Peyton Lloyd, Eden Howe, Victoria Roach, Dashawn Green, Carley Gallegos, Selah Hansen, Hallie Vazquez, Piper Hamilton, Lennon Hunt, Andre Carrillo, Devyn Aguirre, River Johnson, Maliyah Serrano, Diego Chaney, Davion Arias, Nelson Acevedo, Malcolm Nelson, Raven Christensen, Luciana Ford, Amiah Hobbs, Megan Porter, Carsen Tyler, Jordin Schneider, Ralph Roth"

dups1 = str1.strip().split(",")
for index, name in enumerate(dups1):
    dups1[index] = name.strip()
dups1.sort()
print(dups1)

dups2 = str2.strip().split(",")
for index, name in enumerate(dups2):
    dups2[index] = name.strip()
dups2.sort()
print(dups2)


def compare(dups1, dups2):
    for i in range(len(dups1)):
        if not (dups1[i] == dups2[i]):
            return False
    return True


print(f'Movement of truth!!! Is dups1 == dups2: {compare(dups1, dups2)}')
