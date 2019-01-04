import vexdb as v

# print v.getTeams(team="8768A")[0]

print v.getNumTeams(country="United States")
tmp = v.getTeams(country="United States", get_all=True)
print tmp[3000]["team_name"]