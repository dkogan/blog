set terminal svg
set output "leaks.svg"

set style data points
set xlabel  "Line number"
set ylabel  "Leak (bytes)"
set xtics
plot 'leaks.dat' notitle   
