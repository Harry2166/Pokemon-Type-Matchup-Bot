# This program is to present all the strengths, weaknesses, immunities of each pokemon type combination

types = ['Bug', 'Dark', 'Dragon',
        'Electric', 'Fairy', 'Fighting',
        'Fire',	'Flying',	'Ghost',
        'Grass', 'Ground',	'Ice',
       'Normal', 'Poison',	'Psychic',
        'Rock', 'Steel', 'Water'] # List of all typings in Pokemon as of Generation 8 arranged in alphabetical order

strength = [['Dark','Grass', 'Psychic'], ['Ghost', 'Psychic'], ['Dragon'], ['Flying', 'Water'], ['Dark', 'Dragon', 'Fighting'], ['Dark', 'Ice', 'Normal', 'Rock', 'Steel'],
            ['Bug', 'Grass', 'Ice', 'Steel'], ['Bug', 'Fighting', 'Grass'], ['Ghost', 'Psychic'], ['Ground', 'Rock', 'Water' ], ['Electric', 'Fire', 'Poison', 'Rock', 'Steel'],
            ['Dragon', 'Flying', 'Grass', 'Ground'], [], ['Fairy', 'Grass'], ['Fighting', 'Poison'], ['Bug', 'Fire', 'Flying', 'Ice'], ['Fairy', 'Ice', 'Rock'], 
            ['Fire', 'Ground', 'Rock']] # List of all the strenghts that each pokemon typing has against each other arranged in alphabetical order

weakness = [['Fire', 'Flying', 'Rock'], ['Bug','Fairy','Fighting'], ['Dragon', 'Fairy', 'Ice'], ['Ground'], ['Poison', 'Steel'], ['Fairy', 'Flying', 'Psychic'], 
            ['Ground', 'Rock', 'Water'], ['Electric', 'Ice', 'Rock'], ['Dark', 'Ghost'], ['Bug', 'Fire', 'Flying', 'Ice', 'Poison'], ['Grass', 'Ice', 'Water'],
            ['Fighting', 'Fire', 'Rock', 'Steel'], ['Fighting'], ['Ground', 'Psychic'], ['Bug', 'Dark', 'Ghost'], ['Fighting', 'Grass', 'Ground', 'Steel', 'Water'], 
            ['Fighting', 'Fire', 'Ground'], ['Electric', 'Grass']] # List of all the weaknesses that each pokemon typing has against each other arranged in alphabetical order

resistances = [['Fighting', 'Grass', 'Ground'], ['Dark', 'Ghost'], ['Electric', 'Fire', 'Grass', 'Water'], ['Electric', 'Flying', 'Steel'], ['Bug', 'Dark', 'Fighting'], 
            ['Bug', 'Dark', 'Rock'], ['Bug', 'Fairy', 'Fire', 'Grass', 'Ice', 'Steel'], ['Bug', 'Fighting', 'Grass'], ['Bug', 'Poison'], ['Electric', 'Grass', 'Ground', 'Water'],
            ['Poison', 'Rock'], ['Ice'], [], ['Fighting', 'Poison', 'Bug', 'Grass', 'Fairy'], ['Fighting', 'Psychic'], ['Fire', 'Flying', 'Normal', 'Poison'], 
            ['Bug', 'Fairy', 'Dragon', 'Grass', 'Ice', 'Flying', 'Normal', 'Psychic', 'Rock', 'Steel'], ['Fire', 'Ice', 'Steel', 'Water']]
            #this list shows all resistances that each pokemon type has

immunities = [[], ['Psychic'], [], [], ['Dragon'], [], [], ['Ground'], ['Normal', 'Fighting'], [], ['Electric'], [], ['Ghost'], [], [], [], ['Poison'], []]
            #this list shows all immunities that each pokemon type has

# # created by Harry2166
