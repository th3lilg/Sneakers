cipok = []
with open('sneakers - Nike_shoes_2023-04-16.csv', 'r') as forrasfajl:
    forrasfajl.seek(0)
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        cipo = list({'title': adatok[0], 'color_breif': adatok[1], 'fullPrice': adatok[2], 'currentPrice': adatok[3], 'publish_date': adatok[4]})
        cipok.append(adatok)
        # sorrend = lambda title, color, full_price, current_price, publish_date: adatok[0], adatok[1], adatok[2], adatok[3], adatok[4]
    # print(cipok)

    print(f'Valassz, melyik szempont alapjan rendezzem a cipoket?\n1 - title\n2 - color\n3 - full price\n4 - current price\n5 - publish date\n')
    valasz = int(input('Add meg a lehetoseg szamat! '))
    print(sorted(cipok, key=lambda sorrend: adatok[valasz - 1]))

# sorted(cipo[valasz - 1])