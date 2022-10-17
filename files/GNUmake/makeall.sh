#!/bin/zsh

set -x

/bin/rm -f tst *.o *.d
make -rR -f Makefile1 -np xxx | ./dag-from-make.pl | dot -Tsvg -o Makefile1.svg

/bin/rm -f tst *.o *.d
make -rR -f Makefile1.withdependencies -np xxx | ./dag-from-make.pl | dot -Tsvg -o Makefile1.withdependencies.svg
make -f Makefile1.withdependencies tst
make -rR -f Makefile1.withdependencies -np xxx | ./dag-from-make.pl | dot -Tsvg -o Makefile1.withdependencies.after.build.svg

/bin/rm -f tst *.o *.d
make -rR -f Makefile2 -np xxx | ./dag-from-make.pl | dot -Tsvg -o Makefile2.svg
