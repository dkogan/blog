#!/usr/bin/perl


# this is a perl script because #! has a 127-byte limit and my title wouldn't
# fit

use autodie;

my $pipe;
open
  $pipe, '|-',
  'feedgnuplot --lines --xlabel "Time(s)" --ylabel "Memory consumption (kB)" --title "Memory consumption with an extra frame, without and then with an extra frame again" --hardcopy client_first_notfirst.svg';

while(<DATA>)
{
    print $pipe $_;
}

__END__
28060
28060
28060
29044
29044
28968
28968
29224
29224
28760
28760
28876
29136
28944
29204
29204
29244
29244
29352
29364
29364
29364
29312
29312
29244
29244
29244
28984
29244
29044
29304
29084
29344
29344
29344
29344
29472
29476
29476
29476
29520
29520
29532
29532
29556
29556
29664
29556
29556
29556
29556
29556
29556
29556
29556
29556
29556
29680
29680
29680
29680
29556
29556
29768
29556
29556
29556
29668
29668
29668
29668
29776
29776
29776
29828
29828
29828
29840
29840
29832
29832
29832
29832
29832
29832
29836
29836
29836
29876
29876
29876
29900
29900
29912
29912
29912
30024
29912
29912
29912
29912
29912
29912
29912
29912
29912
30036
30036
30036
30100
30100
30100
30100
30100
30100
30100
30100
30100
30100
30100
30104
30104
30104
30160
30100
30100
30220
30100
30216
30216
30216
30216
30100
30100
30100
30100
30100
30100
30100
30100
30100
30100
30100
30356
30356
30356
30356
30360
30360
30416
30100
30360
30100
30360
30100
30100
30100
30352
30352
30352
30352
30520
30520
30520
30520
30520
30520
30572
30572
30696
30572
30572
30572
30572
30572
30576
30576
30632
30656
30656
30656
30656
30632
30632
30776
30632
30632
30632
30632
30632
30632
30632
30748
30748
30756
30756
30756
30756
30756
30756
30892
30892
30920
30916
30916
30928
30928
30928
30928
30928
30928
30928
30940
30940
30940
30940
30940
30940
31040
31024
31024
31148
31024
31024
31028
31032
31032
31032
31032
31060
31060
31116
31112
31120
31120
31120
31120
31236
31236
31236
31252
31252
31252
31252
31252
31252
31252
31260
31260
31260
31260
31260
31260
31260
31260
31368
31260
31260
31260
31260
31336
31336
31328
31328
31328
31328
31260
31260
31260
31260
31448
31448
31500
31264
31580
31264
31524
31264
31264
31264
31264
31264
31500
31500
31500
31500
31620
31620
31620
31620
31524
31264
31688
31316
31576
31264
31584
31584
31584
31584
31712
31712
31760
31792
31792
31792
31792
31792
31792
31792
31792
31792
31792
31796
31796
31796
31796
31796
31796
31920
31920
31920
31920
31852
31852
31796
31796
32056
31796
32056
31796
31796
31796
31796
31796
31796
31796
32020
32024
31796
32056
32056
32056
32188
32188
32280
32292
32280
32280
32280
32280
32280
32280
32280
32280
32280
32284
32284
32280
32280
32296
32296
32296
32296
32296
32296
32296
32296
32348
32348
32348
32348
32396
32396
32320
32320
32440
32440
32452
32452
32492
32416
32380
32504
32504
32316
32316
32316
32316
32316
32316
32316
32316
32536
32536
32536
32536
32536
32536
32516
32516
32664
32664
32792
32792
32792
32792
32792
32792
32820
32820
32832
32832
32832
32832
32892
32892
32892
32888
32908
32896
32896
32896
32968
32968
32968
32968
32968
32968
32968
32968
32968
32968
32968
32972
32972
32972
32972
32972
32972
32972
32972
32972
32972
32972
32972
33064
33064
33064
33064
33060
33060
33092
33092
33100
33100
33100
33100
33140
33140
33140
33140
33140
33140
33140
33208
33208
33208
33232
33232
33232
33232
33232
33232
33232
33232
33232
33316
33316
33316
33316
33316
33316
33316
33316
33372
33372
33372
33372
33372
33372
33400
33400
33400
33400
33444
33444
33520
33520
33508
33508
33508
33508
33472
33472
33472
33472
33472
33512
33512
33472
33472
33516
33516
33516
33672
33672
33688
33688
33684
33792
33684
33808
33684
33816
33684
33684
33684
33964
33964
33964
33964
33624
33624
33744
33744
33624
33624
33832
33832
33832
33832
33904
33904
33900
33900
33900
33900
33904
33932
33932
33932
33932
33972
33972
33972
33972
33972
33972
33972
33972
33972
33972
34208
34208
34208
34208
33980
33980
34176
34176
34176
34176
34176
34180
34168
34168
34040
34040
34040
34040
34220
34220
34304
34304
34308
34308
34308
34308
34492
34492
34492
34492
34476
34444
34444
34428
34428
34260
34260
34260
34260
34404
34404
34404
34404
34588
34508
34508
34516
34628
34516
34628
34508
34508
34508
34508
34024
34568
34568
34568
34740
34740
34656
34656
34656
34656
34656
34656
34776
34700
34700
34700
34824
34824
34824
34824
34660
34660
34660
34660
34692
34692
34692
34732
34696
34696
34788
34788
34788
34868
34868
34868
35044
35044
34916
34916
34820
34820
34904
34904
34872
34872
34852
34852
34964
34964
34964
34964
34964
35200
35200
35200
35200
34844
34844
34960
34960
34960
35120
35120
35132
35252
35252
35252
35252
35284
35284
35284
35284
35284
35284
35284
35284
35284
35284
35284
35284
35316
35316
35316
35316
35316
35316
35316
35316
35428
35372
35372
35372
35372
35372
35316
35316
35316
35316
35320
35320
35320
35424
35424
35424
35424
35320
35320
35320
35320
35320
35320
35320
35320
35580
35580
35580
35580
35700
35700
35700
35700
35700
35700
35700
35700
35704
35700
35700
35700
35816
35816
35700
35700
35700
35700
35700
35700
35700
35700
35704
35704
35704
35704
35704
35704
35704
35704
35724
35724
35824
35856
35940
35852
36000
35992
35992
36056
36056
36128
36128
36452
36452
36564
36564
36652
36652
36760
36760
37088
37088
37244
37244
37388
37388
37516
37516
37660
37660
37992
37992
38176
38176
38520
38520
38768
38596
38904
38636
38984
38632
39016
38632
39132
39132
39384
39384
39688
39364
39616
39620
39640
39748
39748
40012
40012
40132
40132
40184
40184
40524
40524
40636
40680
40752
40752
40836
40836
40984
40984
41124
41124
41496
41496
41792
41608
41932
41672
42092
42092
42236
42236
42296
42296
42144
42200
42228
42228
42320
42320
42664
42708
42752
42808
43204
43260
43316
43496
43552
43612
43612
43928
43928
44332
44332
44560
44560
44700
44700
44752
44752
44752
44752
44752
44768
44764
44764
44868
44868
44944
44944
45060
45060
45376
45188
45512
45512
45996
45996
45788
45788
46200
46200
46296
46296
46348
46348
46476
46476
46600
46656
46796
46836
46884
47144
47204
47640
47640
47552
47552
47556
47556
47628
47664
47664
47664
48000
48056
48588
48588
48928
48680
49196
49196
49568
49568
49716
49664
49804
49860
50340
50340
50692
50460
50876
50876
50952
51008
51008
51008
51008
51008
51156
51156
51156
51156
51156
51156
51156
52304
52304
52688
52688
52688
52688
52688
52688
52688
52688
52688
52688
52688
52688
52884
52884
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
52872
53132
53132
53132
53132
53176
53176
53180
53148
53148
53148
53148
53148
53148
53148
53148
53148
53148
53248
53248
53248
53248
53248
53344
53344
53344
53344
53344
53344
53344
53348
53348
53320
53320
53320
53320
53320
53320
53320
53320
53320
53320
53320
53320
53320
53320
53320
53320
53480
53480
53480
53480
53480
53480
53480
53480
53320
53320
53320
53320
53320
53320
53320
53320
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53548
53740
53740
53740
53740
53740
53740
53744
53744
53744
53744
53744
53744
53784
53784
53784
53784
53784
53784
53784
53784
53784
53784
53784
53784
53784
53784
53784
53784
53784
53784
53868
53868
53868
53868
53868
53868
53868
53868
53908
53908
53908
53908
53908
53908
53908
54056
54056
54056
54056
54068
54068
54068
54068
54068
54068
54068
54068
54068
54068
54068
54068
54068
54068
54108
54108
54108
54108
54132
54116
54120
54120
54120
54120
54120
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54116
54284
54272
54272
54272
54272
54272
54272
54272
54376
54376
54376
54376
54300
54300
54300
54300
54424
54424
54300
54300
54300
54300
54428
54428
54428
54428
54428
54428
54428
54428
54428
54544
54544
54544
54544
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54576
54752
54752
54720
54720
54708
54684
54684
54684
54684
54708
54708
54712
54712
54712
54712
54712
54712
54828
54828
54828
54828
54844
54844
54844
54844
54844
54844
54844
54844
54844
54844
54844
54844
54844
54844
54844
54844
54844
54844
54936
54936
54932
54932
54932
54932
54932
54932
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
54976
55140
55140
55140
55140
55140
55140
55140
55140
55140
55140
55140
55140
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55188
55356
55356
55356
55356
55356
55356
55364
55364
55364
55364
55364
55364
55436
55436
55436
55436
55436
55436
55444
55444
55444
55444
55444
55444
55444
55444
55444
55444
55444
55444
55444
55444
55444
55444
55444
55444
55592
55592
55592
55592
55592
55592
55592
55592
55592
55652
55652
55652
55652
55632
55560
55560
55560
55560
55560
55560
55560
55560
55560
55560
55616
55620
55620
55620
55620
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55744
55892
55892
55892
55892
55892
55892
55912
55912
55912
55892
55892
55900
55900
55900
55900
55900
55900
55900
55900
55904
55896
55896
55896
55896
55896
55896
55896
55896
55896
55896
55896
55896
55896
56036
56036
56036
56036
56036
56036
56036
56036
56036
56036
56036
56036
56036
56036
56036
56160
56160
56160
56160
56156
56124
56128
56128
56128
56128
56128
56128
56128
56128
56128
56128
56112
56112
56112
56112
56112
56112
56112
56112
56280
56280
56280
56280
56280
56280
56280
56280
56280
56280
56288
56288
56288
56260
56260
56260
56260
56260
56260
56260
56260
56260
56260
56420
56420
56420
56420
56420
56420
56420
56420
56420
56420
56420
56420
56420
56420
56420
56420
56420
56420
56480
56480
56532
56532
56532
56532
56532
56532
56532
56532
56592
56592
56592
56592
56592
56592
56592
56592
56592
56592
56700
56700
56700
56640
56640
56640
56640
56640
56640
56640
56640
