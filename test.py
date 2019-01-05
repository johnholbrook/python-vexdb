import vexdb as v

tmp = v.getAwards(season="In The Zone", get_all=True)

print len(tmp)

print tmp[3000]