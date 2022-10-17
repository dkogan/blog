CC ?= gcc

CFLAGS += -MMD

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

tst: tst1.o tst2.o
	$(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)

clean:
	rm -f *.o *.d tst
.PHONY: clean

-include *.d
