set output "winner.svg"
set terminal svg

set title "Emacs memory consumption as clients are created/destroyed"
set xlabel "Time(s)"
set ylabel "Memory usage (kB)"
plot \
  "memory.noconfig.log"       with lines title "Empty init.el", \
  "memory.winneronly.log"     with lines title "Only unpatched winner-mode", \
  "memory.winner.patched.log" with lines title "Only patched winner-mode"
