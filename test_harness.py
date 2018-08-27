from player_object import Player

row = None
p = Player(row)

# Setup
p.fg_attempted = 17
p.free_throws_attempted = 12
p.free_throws_made = 10
p.offense_rebounds = 9
p.defense_rebounds = 6
p.stl = 2
p.ast = 12
p.blk= 5
p.pf = 2
p.to = 3
p.pts = 16


# Test run
gs = p.get_gamescore()
gs_old = p.get_gamescore_old()

print('gamescore: {0} | gamescore2 {1} | Passes: {2}'.format(
    gs, gs_old, gs == gs_old))


gskm = p.get_km_gamescore()
gskm_old = p.get_km_gamescore_old()

print('gamescore km: {0} | gamescore km2 {1} | Passes: {2}'.format(
    gskm, gskm_old, gskm == gskm_old))