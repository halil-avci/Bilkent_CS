# -*- coding: utf-8 -*-
"""
@author: CS115
"""


def load_movies( filename ):
    movies = {}
    file = open(filename,'r')
    for line in file:
        data = line.split(',')

        if int(data[0]) in movies:
            movies[int(data[0])].append(data[1].strip())
        else:
            movies[int(data[0])] = [data[1].strip()]
    file.close()
    return movies

def get_movies_by_year( movies,year ):
    try:
        return(movies[year])
    except:
        return []

def get_movies_by_keyword( movies, keyword ):
    found_movies = []
    for key in movies:
        for movie in movies[key]:
            if keyword.lower() in movie.lower():
                found_movies.append((key,movie))
    return found_movies
            
def print_list( lst ):
    for l in lst:
        print( l )
          
            
file = 'movie_data.csv'
movies = load_movies( file )
year = int(input('Enter year to search: '))
movies_year = get_movies_by_year( movies,year )
if movies_year:
    print(f'Movies made in {year}: ')
    print_list( movies_year )
else:
    print(f'No movies from {year} found')

keyword = input('Enter keyword to search: ')
keyword_movies = get_movies_by_keyword( movies, keyword )
if keyword_movies:
    print_list( keyword_movies )
else:
    print(f'No movies with the keyword "{keyword}" found')
