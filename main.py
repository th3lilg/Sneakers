with open('sneakers - Nike_shoes_2023-04-16.csv', 'r') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        cipo = list({'title': adatok[0], 'color_breif': adatok[1], 'fullPrice': map(int, adatok[2]), 'currentPrice': map(int, adatok[3]), 'publish_date': map(int, adatok[4])})
        # sorrend = lambda title, color, full_price, current_price, publish_date: adatok[0], adatok[1], adatok[2], adatok[3], adatok[4]


        print(f'Valassz, melyik szempont alapjan rendezzem a cipoket?\n1 - title\n2 - color\n3 - full price\n4 - current price\n5 - publish date\n')
        valasz = int(input('Add meg a lehetoseg szamat! '))
        print(sorted(forrasfajl, key=lambda sorrend: adatok[valasz - 1]))

# sorted(cipo[valasz - 1])