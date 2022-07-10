import pandas as pd
from IPython.display import display
import random
l = random.randint(1,4)
df = pd.read_csv('Pokemon.csv')
display(df)
if l == 1:
    print('################################Displaying pokemon names with Legendary status.###############################\n\n')
    display(df.Name[df.Legendary == True])
    print('\n\n')
elif l == 2:
    print('################################Getting pokemon name from user input and then printing details about the pokemon.###############################\n\n')
    print('Enter name of pokemon : ')
    m = random.randint(0,800)
    name = df.Name.unique()[m]
    print('\n\nEntered name :', name, '\nDetails are as follows:\n\n')
    display(df[df.Name == name])
elif l == 3:
    print('################################Displaying info of a pokemon who will be the only one fullfilling any one of the following criteria####################\
###########\n\nMaximum Total\nMaximum Total + Legendary Status\nMaximum Total + Legendary + 3rd Generation.\n\n')
    i = df[df.Total == max(df.Total)].Total.value_counts().values[0]
    j = df[(df.Total == max(df.Total)) & (df.Legendary == True)].Total.value_counts().values[0]
    k = df[(df.Total == max(df.Total)) & (df.Legendary == True) & (df.Generation == 3)].Total.value_counts().values[0]
    if i == 1:
        display(df[df.Total == max(df.Total)])
    elif j == 1:
        display(df[(df.Total == max(df.Total)) & (df.Legendary == True)])
    elif k == 1:
        display(df[(df.Total == max(df.Total)) & (df.Legendary == True) & (df.Generation == 3)])
elif l == 4:
    print('################################Displaying info of pokemon/s of 6th Generation.###############################\n\n')
    display(df[df.Generation == 6])
    print('\n\n')
