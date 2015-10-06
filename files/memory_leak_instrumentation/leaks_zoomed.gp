set terminal svg
set output "leaks_zoomed.svg"

set style data points
set xlabel  "Line number"
set ylabel  "Leak (bytes)"
set xtics
plot [] [0:4000] 'leaks.dat' notitle   
