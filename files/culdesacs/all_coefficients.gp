set size ratio -1./cos(34.0691 * pi/180.0)

set output "all_coefficients.png"
set terminal pngcairo enhanced color size 1000,1000

set title "Coefficient of inconvenience from 3rd/New Hampshire"
set xlabel "Longitude"
set ylabel "Latitude"

plot "query_34.0690448_-118.292924_20miles.out" using 2:1:((($3-$4)/($4))) with points ps 0.5 pt 7 palette notitle

set output
set terminal x11
