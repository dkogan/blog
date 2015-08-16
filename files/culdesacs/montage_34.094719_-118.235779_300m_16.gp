# Generated by osmgnuplot.pl from
#   http://notes.secretsauce.net/notes/2015/08/13_rendering-openstreetmap-tiles-in-gnuplot.html
#
# Command used:
#   osmgnuplot.pl --center 34.094719,-118.235779 --rad 300m --zoom 16

attenuation = 1

set autoscale noextend

set output "attayloryard.png"
set terminal pngcairo enhanced color size 627,627 font ",10"

set title "Inconvenient locations from 3rd/New Hampshire near Taylor Yard"
set xlabel "Longitude"
set ylabel "Latitude"


set size ratio -1./cos(34.094719 * pi/180.0)
plot "montage_34.094719_-118.235779_300m_16.png" binary filetype=png dx=2.14576721191406e-05 dy=1.77693558863918e-05 center=(-118.234874010086,34.0936193271881) using ($1/attenuation):($2/attenuation):($3/attenuation) with rgbimage notitle, '-' using 2:1 with points pt 7 ps 3 notitle
34.095020 -118.236320
34.094849 -118.236145
34.094719 -118.235779
34.094639 -118.235474
34.094620 -118.235405
34.094543 -118.235138
e

set output
set terminal x11
