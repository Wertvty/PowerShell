def raindrops(number):
    idk = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    
    return ''.join(sound for factor, sound in idk if number % factor == 0) or str(number)