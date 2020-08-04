import num2words
def recite(start_verse, end_verse):
    verse = []
    gifts = {
1:'a Partridge in a Pear Tree.',
2:'two Turtle Doves, \n',
3:'three French Hens, \n',
4:'four Calling Birds, \n',
5:'five Gold Rings, \n',
6:'six Geese-a-Laying, \n',
7:'seven Swans-a-Swimming, \n',
8:'eight Maids-a-Milking, \n',
9:'nine Ladies Dancing, \n',
10:'ten Lords-a-Leaping, \n',
11:'eleven Pipers Piping, \n',
12:'twelve Drummers Drumming, \n'
}
    days= {
1:'first',
2:'second',
3:'third',
4:'fourth',
5:'fifth',
6:'sixth',
7:'seventh',
8:'eighth',
9:'nineth',
10:'tenth',
11:'eleventh',
12:'twelveth'
}
    for i in range (start_verse, end_verse+1):
        verse.append(''.join('On the ' + days[i] + ' day of Christmas my true love gave to me: \n' + ''.join(gifts[x] for x in range(i,0,-1)) + '\n'))
    verse = ''.join([str(y) for y in verse])
    return(verse)
                



            


