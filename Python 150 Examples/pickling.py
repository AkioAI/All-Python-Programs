import pickle

imelda=('More Mayhem'
        'IMelda May'
        '2011',
        ((1,  'Pulling the rug'),
         (2,  'Physco'),
         (3,  'Mayhem'),
         (4,  'Kentish town Waltz')))

with open("imelda",'wb') as pickle_file:
    pickle.dump(imelda, pickle_file)