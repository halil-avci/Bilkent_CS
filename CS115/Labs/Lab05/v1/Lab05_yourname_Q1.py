# -*- coding: utf-8 -*-
"""
@author: CS115
"""


def load_movies( filename ):
    file = open(filename,'r')
    movies = {}
    for line in file:
        data = line.split(',')
        first_char = data[1][0].upper()
        if first_char in movies:
            movies[first_char].append( (int(data[0]),data[1].strip()) )
        else:
            movies[first_char] = [(int(data[0]),data[1].strip())]
    file.close()
    return movies
    
def get_movies_by_name( movies,character ):
    try:
        return(movies[character.upper()])
    except:
        return []

def get_movies_by_year( movies, year ):
    found_movies = []
    for key in movies:
        for movie in movies[key]:
            if movie[0] == year:
                found_movies.append(movie[1])
    return found_movies

def print_list( lst ):
    for l in lst:
        print( l )
          
# def show_movies( movie_list, rows = 10 ):
#     if len(movie_list) > rows:
#         print(f'Showing first {rows} records')
#     if len(movie_list) < rows:
#         rows = len(movie_list)
#     for i in range(rows):
#             print( '\t',movie_list[i])
            
file = 'movie_data.csv'
movies = load_movies( file )
# write_movies(movies)
character = input('Enter first character of movies to search: ')
movies_char = get_movies_by_name( movies,character )
if movies_char:
    print(f'Movies with names starting with {character}: ')
    print_list( movies_char )
else:
    print(f'No movies with names starting with {character} found')

year = int(input('Enter year to search: '))
year_movies = get_movies_by_year( movies, year )
if year_movies:
    print_list( year_movies )
else:
    print(f'No movies from the year "{year}" found')
