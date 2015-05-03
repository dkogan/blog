reset
set output "profiles_full.svg"
set terminal svg

unset grid
set xlabel "Flat distance (ft)"
set ylabel "Elevation (ft)"
set title "Elevation profiles of steep LA streets"


plot "fargo.dat"  with lines title "Fargo Street (rising East from the 2 fwy)", \
     "baxter.dat" with lines title "Baxter Street (rising East from the 2 fwy)", \
     "eldred.dat" with lines title "Eldred St (rising West from Avenue 50)"

set output

