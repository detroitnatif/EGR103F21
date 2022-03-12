
## notes from class 9/10

def ratings(age):
    print('G rated is fine')
    movies = ['G']
    if age < 17:
        print('R with parent/guardian')
        print('No NC-17')
        movies += ['PG', 'PG13', 'R']
    elif age==17:
        print('No NC-17')
        print('R by yourself!')
        movies += ["PG", 'PG13', 'R']
    else:
        print('see everything')
        movies += ["PG", "PG13", "R"]
    return movies
    
    
    
    
if __name__ == '__main__':
    print(ratings(3))
    print(ratings(15))
    print(ratings(23))
    
print(__name__)
 
