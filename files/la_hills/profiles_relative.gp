reset
set output "profiles_relative.svg"
set terminal svg

unset grid
set xlabel "Flat distance (ft)"
set ylabel "Relative elevation (ft)"


plot [61:575] \
     "fargo.dat"  using ($1):($2-500)     with lines title "Fargo Street (rising East from the 2 fwy)", \
     "baxter.dat" using ($1):($2-500)     with lines title "Baxter Street (rising East from the 2 fwy)", \
     "eldred.dat" using ($1-710):($2-477) with lines title "Eldred St (rising West from Avenue 50)"

set output
