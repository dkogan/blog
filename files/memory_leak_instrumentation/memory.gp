set terminal svg
set output "memory.svg"

set style data points
set xlabel  "Time (s)"
set ylabel  "Memory usage (kB)"
set xtics
plot 'memory.dat' notitle with lines
