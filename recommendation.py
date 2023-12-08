import pandas as pd
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv("file.tsv", sep='\t', names=column_names)
movie_titles = pd.read_csv('Movie_Id_Titles.csv')
data = pd.merge(df, movie_titles, on='item_id')

t = 0
while not t:
    print("*******************Movie Recommendation System**************************")
    print("1:Get the data\n2:Check out all the movies and their respective IDs\n3:Check the head of the data\n4:"
          "Calculate mean rating of all movies\n5:Calculate count rating of all movies"
          "\n6:creating dataframe with 'rating' count values\n7:Exit")
    n=int(input('Enter the number between(1-7) : '))
    print()
    if n == 1:
        print(df.head())
    elif n == 2:
        print(movie_titles.head())
    elif n == 3:
        print(data.head())
    elif n == 4:
        print(data.groupby('title')['rating'].mean().sort_values(ascending=False).head())
    elif n == 5:
        print(data.groupby('title')['rating'].count().sort_values(ascending=False).head())
    elif n == 6:
        ratings = pd.DataFrame(data.groupby('title')['rating'].mean())

        ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

        print(ratings.head())

    elif n == 7:
        print("End")
        t = 1
    else:
        print("Enter Proper Input")
    print("\n")

print("****************************************************************")


