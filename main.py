with open('sneakers - Nike_shoes_2023-04-16.csv', 'r') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        cipo = {'title': adatok[0], 'color_breif': adatok[1], 'fullPrice': adatok[2], 'currentPrice': adatok[3], 'publish_date': adatok[4]}

    print(f'Valassz, melyik szempont alapjan rendezzem a cipoket?\n1 - title\n2 - color\n3 - full price\n4 - current price\n5 - publish date\n')
    valasz = int(input('Add meg a lehetoseg szamat! '))