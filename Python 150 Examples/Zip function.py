Names=['Peter Parker','Tony Stark','Wade Wilson','Bruce Wayne']
Heroes=['spiderman','Iron Man','Deadpool','Batman']
Universes=['Marvel','Marvel','Marvel','DC']
for Name,Hero,Universe in zip(Names,Heroes,Universes):       #zip can be use more than 2 list
    print(f'{Name} is actually {Hero} from {Universe}')        #fstring