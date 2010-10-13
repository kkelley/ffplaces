import sqlite3

firefox_places = "A:\\places.sqlite"

cn = sqlite3.connect(firefox_places)
cu = cn.cursor()

dt = cu.execute("select mp.id, mp.url from moz_places as mp, moz_bookmarks as mb where mp.id = mb.id")

td = []
for row in dt:
    x = i[1].find("?utm_source=feedburner")
    if x is -1:
        x = i[1].find("?utm-source=feedburner")
        if x is -1:
            continue
        else:
            td.append([i, x])
    else:
        td.append([i, x])

nd = []
for i in td:
    it = i[0]
    it[1] = it[1][:i[1]]
    nd.append(it)

sq = []
for i in nd:
    query = 'update moz_places set url="%s" where id=%s' % (i[1], i[0])
    sq.append(query)

for i in sq:
    cu.execute(i)

cn.commit()
cu.close()
cn.close()
