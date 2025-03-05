#!/usr/bin/python3

import sys
import os
import re

def report_solution_to_console(vars):
    for w in days_of_week:
        annotation = ''
        if human_annotate is not None:
            for s in shifts.keys():
                m = re.match(rf'{w} - ', s)
                if not m: continue
                if vars[human_annotate][s].value():
                    annotation = f" ({human_annotate} SCHEDULED)"
                    break
            if not len(annotation):
                annotation = f" ({human_annotate} OFF)"

        print(f"{w}{annotation}")

        for s in shifts.keys():
            m = re.match(rf'{w} - ', s)
            if not m: continue

            annotation = ''
            if human_annotate is not None:
                annotation = f" ({human_annotate} {shifts[s][human_annotate]})"
            print(f"    ---- {s[m.end():]}{annotation}")

            for h in humans:
                if vars[h][s].value():
                    print(f"         {h} ({shifts[s][h]})")

def report_solution_summary_to_console(vars):
    print("\nSUMMARY")

    for h in humans:
        print(f"-- {h}")
        print(f"   benefit: {benefits[h].value():.3f}")

        counts = dict()
        for a in availabilities:
            counts[a] = 0

        for s in shifts.keys():
            if vars[h][s].value():
                counts[shifts[s][h]] += 1

        for a in availabilities:
            print(f"   {counts[a]} {a}")

        if len(benefit_boost_leq_bound) == 0: continue
        print('   --------')
        for b in benefit_boost_leq_bound.keys():
            print(f'   vars_Nshifts_leq[{b}] = {vars_Nshifts_leq[h][b].value()}')


def report_solution_to_ics(filename, vars):

    import icalendar
    import datetime
    import pytz
    tz = pytz.timezone('US/Pacific')

    year  = 2024
    month = 12


    dayofweek_ordinal = dict( SUNDAY    = 0,
                              MONDAY    = 1,
                              TUESDAY   = 2,
                              WEDNESDAY = 3,
                              THURSDAY  = 4,
                              FRIDAY    = 5,
                              SATURDAY  = 6 )

    calendar = icalendar.Calendar()
    for s in shifts.keys():

        m = re.match(r'([a-z]+) *- *(.*?) *([0-9].*?) - ([0-9].*?) *$',
                     s,
                     flags = re.I)

        if m is None:
            print("could not parse event")
            raise
        dow   = m.group(1)
        what  = m.group(2)
        when0 = m.group(3)
        when1 = m.group(4)

        def parse_date(when):
            m = re.match(r'([0-9]+):([0-9]+) *([AP]M)$', when)
            if m is None:
                raise Exception(f"Couldn't parse '{when}'")
            hour   = int(m.group(1))
            minute = int(m.group(2))
            if hour != 12:
                if m.group(3) == 'PM':
                    hour += 12
            else:
                if m.group(3) == 'AM':
                    hour = 0
            return hour,minute


        when0 = parse_date(when0)
        when1 = parse_date(when1)

        when0 = datetime.datetime(year, month, 1+dayofweek_ordinal[dow],
                                  *when0)
        when1 = datetime.datetime(year, month, 1+dayofweek_ordinal[dow],
                                  *when1)

        human_assigned = None
        for h in humans:
            if vars[h][s].value():
                human_assigned =  f"{h} ({shifts[s][h]})"
                break
        if human_assigned is None:
            raise Exception(f"{s}: no human assigned!")

        event = icalendar.Event()
        event.add('summary', f"{what} - {human_assigned}")
        event.add('dtstart', tz.localize(when0))
        event.add('dtend',   tz.localize(when1))
        calendar.add_component(event)

    with open(filename, 'wb') as f:
        f.write(calendar.to_ical())


human_annotate = None


days_of_week = ('SUNDAY',
                'MONDAY',
                'TUESDAY',
                'WEDNESDAY',
                'THURSDAY',
                'FRIDAY',
                'SATURDAY')

humans = ['ALICE', 'BOB',
          'CAROL', 'DAVID', 'EVE', 'FRANK', 'GRACE', 'HEIDI', 'IVAN', 'JUDY']

shifts = {'SUNDAY - SANDING 9:00 AM - 4:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'DAVID': 'PREFERRED',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'DISFAVORED',
           'HEIDI': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'JUDY':  'NEUTRAL'},
          'WEDNESDAY - SAWING 7:30 AM - 2:30 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'DAVID': 'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'EVE':   'REFUSED',
           'JUDY':  'REFUSED'},
          'THURSDAY - SANDING 9:00 AM - 4:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'DAVID': 'PREFERRED',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'PREFERRED',
           'HEIDI': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'JUDY':  'PREFERRED'},
          'SATURDAY - SAWING 7:30 AM - 2:30 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'DAVID': 'PREFERRED',
           'FRANK': 'PREFERRED',
           'HEIDI': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'EVE':   'REFUSED',
           'JUDY':  'REFUSED',
           'GRACE': 'REFUSED'},
          'SUNDAY - SAWING 9:00 AM - 4:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'DAVID': 'PREFERRED',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'JUDY':  'PREFERRED',
           'HEIDI': 'REFUSED'},
          'MONDAY - SAWING 9:00 AM - 4:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'DAVID': 'PREFERRED',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'PREFERRED',
           'IVAN':  'PREFERRED',
           'JUDY':  'PREFERRED',
           'HEIDI': 'REFUSED'},
          'TUESDAY - SAWING 9:00 AM - 4:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'DAVID': 'PREFERRED',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'NEUTRAL',
           'IVAN':  'PREFERRED',
           'JUDY':  'PREFERRED',
           'HEIDI': 'REFUSED'},
          'WEDNESDAY - PAINTING 7:30 AM - 2:30 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'EVE':   'REFUSED',
           'JUDY':  'REFUSED',
           'DAVID': 'REFUSED'},
          'THURSDAY - SAWING 9:00 AM - 4:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'DAVID': 'PREFERRED',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'PREFERRED',
           'IVAN':  'PREFERRED',
           'JUDY':  'PREFERRED',
           'HEIDI': 'REFUSED'},
          'FRIDAY - SAWING 9:00 AM - 4:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'DAVID': 'PREFERRED',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'PREFERRED',
           'IVAN':  'PREFERRED',
           'JUDY':  'DISFAVORED',
           'HEIDI': 'REFUSED'},
          'SATURDAY - PAINTING 7:30 AM - 2:30 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'FRANK': 'PREFERRED',
           'HEIDI': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'EVE':   'REFUSED',
           'JUDY':  'REFUSED',
           'GRACE': 'REFUSED',
           'DAVID': 'REFUSED'},
          'SUNDAY - PAINTING 9:45 AM - 4:45 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'JUDY':  'PREFERRED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'MONDAY - PAINTING 9:45 AM - 4:45 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'PREFERRED',
           'IVAN':  'PREFERRED',
           'JUDY':  'NEUTRAL',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'TUESDAY - PAINTING 9:45 AM - 4:45 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'NEUTRAL',
           'IVAN':  'PREFERRED',
           'JUDY':  'PREFERRED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'WEDNESDAY - SANDING 9:45 AM - 4:45 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'DAVID': 'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'JUDY':  'NEUTRAL',
           'EVE':   'REFUSED'},
          'THURSDAY - PAINTING 9:45 AM - 4:45 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'NEUTRAL',
           'IVAN':  'PREFERRED',
           'JUDY':  'PREFERRED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'FRIDAY - PAINTING 9:45 AM - 4:45 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'PREFERRED',
           'FRANK': 'PREFERRED',
           'GRACE': 'PREFERRED',
           'IVAN':  'PREFERRED',
           'JUDY':  'DISFAVORED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'SATURDAY - SANDING 9:45 AM - 4:45 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'DAVID': 'PREFERRED',
           'FRANK': 'PREFERRED',
           'HEIDI': 'DISFAVORED',
           'IVAN':  'PREFERRED',
           'EVE':   'REFUSED',
           'JUDY':  'REFUSED',
           'GRACE': 'REFUSED'},
          'SUNDAY - PAINTING 11:00 AM - 6:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'PREFERRED',
           'IVAN':  'NEUTRAL',
           'JUDY':  'NEUTRAL',
           'DAVID': 'REFUSED'},
          'MONDAY - PAINTING 12:00 PM - 7:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'PREFERRED',
           'IVAN':  'NEUTRAL',
           'JUDY':  'NEUTRAL',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'TUESDAY - PAINTING 12:00 PM - 7:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'NEUTRAL',
           'HEIDI': 'REFUSED',
           'JUDY':  'REFUSED',
           'DAVID': 'REFUSED'},
          'WEDNESDAY - PAINTING 12:00 PM - 7:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'NEUTRAL',
           'JUDY':  'PREFERRED',
           'EVE':   'REFUSED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'THURSDAY - PAINTING 12:00 PM - 7:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'NEUTRAL',
           'JUDY':  'PREFERRED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'FRIDAY - PAINTING 12:00 PM - 7:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'NEUTRAL',
           'JUDY':  'DISFAVORED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'SATURDAY - PAINTING 12:00 PM - 7:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'NEUTRAL',
           'FRANK': 'NEUTRAL',
           'IVAN':  'NEUTRAL',
           'JUDY':  'DISFAVORED',
           'EVE':   'REFUSED',
           'HEIDI': 'REFUSED',
           'GRACE': 'REFUSED',
           'DAVID': 'REFUSED'},
          'SUNDAY - SAWING 12:00 PM - 7:00 PM':
          {'ALICE': 'PREFERRED',
           'BOB':   'PREFERRED',
           'CAROL': 'NEUTRAL',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'NEUTRAL',
           'JUDY':  'PREFERRED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'MONDAY - SAWING 2:00 PM - 9:00 PM':
          {'ALICE': 'PREFERRED',
           'BOB':   'PREFERRED',
           'CAROL': 'DISFAVORED',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'DISFAVORED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'TUESDAY - SAWING 2:00 PM - 9:00 PM':
          {'ALICE': 'PREFERRED',
           'BOB':   'PREFERRED',
           'CAROL': 'DISFAVORED',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'HEIDI': 'REFUSED',
           'JUDY':  'REFUSED',
           'DAVID': 'REFUSED'},
          'WEDNESDAY - SAWING 2:00 PM - 9:00 PM':
          {'ALICE': 'PREFERRED',
           'BOB':   'PREFERRED',
           'CAROL': 'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'DISFAVORED',
           'EVE':   'REFUSED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'THURSDAY - SAWING 2:00 PM - 9:00 PM':
          {'ALICE': 'PREFERRED',
           'BOB':   'PREFERRED',
           'CAROL': 'DISFAVORED',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'DISFAVORED',
           'HEIDI': 'REFUSED',
           'DAVID': 'REFUSED'},
          'FRIDAY - SAWING 2:00 PM - 9:00 PM':
          {'ALICE': 'PREFERRED',
           'BOB':   'PREFERRED',
           'CAROL': 'DISFAVORED',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'HEIDI': 'REFUSED',
           'JUDY':  'REFUSED',
           'DAVID': 'REFUSED'},
          'SATURDAY - SAWING 2:00 PM - 9:00 PM':
          {'ALICE': 'PREFERRED',
           'BOB':   'PREFERRED',
           'CAROL': 'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'DISFAVORED',
           'EVE':   'REFUSED',
           'HEIDI': 'REFUSED',
           'GRACE': 'REFUSED',
           'DAVID': 'REFUSED'},
          'SUNDAY - PAINTING 12:15 PM - 7:15 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'PREFERRED',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'NEUTRAL',
           'DAVID': 'REFUSED'},
          'MONDAY - PAINTING 2:00 PM - 9:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'DISFAVORED',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'DISFAVORED',
           'DAVID': 'REFUSED'},
          'TUESDAY - PAINTING 2:00 PM - 9:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'DISFAVORED',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'REFUSED',
           'DAVID': 'REFUSED'},
          'WEDNESDAY - PAINTING 2:00 PM - 9:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'DISFAVORED',
           'EVE':   'REFUSED',
           'DAVID': 'REFUSED'},
          'THURSDAY - PAINTING 2:00 PM - 9:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'DISFAVORED',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'DISFAVORED',
           'DAVID': 'REFUSED'},
          'FRIDAY - PAINTING 2:00 PM - 9:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'DISFAVORED',
           'EVE':   'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'GRACE': 'NEUTRAL',
           'HEIDI': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'REFUSED',
           'DAVID': 'REFUSED'},
          'SATURDAY - PAINTING 2:00 PM - 9:00 PM':
          {'ALICE': 'NEUTRAL',
           'BOB':   'NEUTRAL',
           'CAROL': 'DISFAVORED',
           'FRANK': 'NEUTRAL',
           'HEIDI': 'NEUTRAL',
           'IVAN':  'DISFAVORED',
           'JUDY':  'DISFAVORED',
           'EVE':   'REFUSED',
           'GRACE': 'REFUSED',
           'DAVID': 'REFUSED'}}

availabilities = ['PREFERRED', 'NEUTRAL', 'DISFAVORED']



import pulp
prob = pulp.LpProblem("Scheduling", pulp.LpMaximize)

vars = pulp.LpVariable.dicts("Assignments",
                             (humans, shifts.keys()),
                             None,None, # bounds; unused, since these are binary variables
                             pulp.LpBinary)

# Everyone works at least 2 shifts
Nshifts_min = 2
for h in humans:
    prob += (
        pulp.lpSum([vars[h][s] for s in shifts.keys()]) >= Nshifts_min,
        f"{h} works at least {Nshifts_min} shifts",
    )

# each shift is ~ 8 hours, so I limit everyone to 40/8 = 5 shifts
Nshifts_max = 5
for h in humans:
    prob += (
        pulp.lpSum([vars[h][s] for s in shifts.keys()]) <= Nshifts_max,
        f"{h} works at most {Nshifts_max} shifts",
    )

# all shifts staffed and not double-staffed
for s in shifts.keys():
    prob += (
        pulp.lpSum([vars[h][s] for h in humans]) == 1,
        f"{s} is staffed",
    )

# each human can work at most one shift on any given day
for w in days_of_week:
    for h in humans:
        prob += (
            pulp.lpSum([vars[h][s] for s in shifts.keys() if re.match(rf'{w} ',s)]) <= 1,
            f"{h} cannot be double-booked on {w}"
        )


#### Some explicit constraints; as an example
# DAVID can't work any PAINTING shift and is off on Thu and Sun
h = 'DAVID'
prob += (
    pulp.lpSum([vars[h][s] for s in shifts.keys() if re.search(r'- PAINTING',s)]) == 0,
    f"{h} can't work any PAINTING shift"
)
prob += (
    pulp.lpSum([vars[h][s] for s in shifts.keys() if re.match(r'THURSDAY|SUNDAY',s)]) == 0,
    f"{h} is off on Thursday and Sunday"
)

# Do not assign any "REFUSED" shifts
for s in shifts.keys():
    for h in humans:
        if shifts[s][h] == 'REFUSED':
            prob += (
                vars[h][s] == 0,
                f"{h} is not available for {s}"
            )


# Objective. I try to maximize the "happiness". Each human sees each shift as
# one of:
#
#   PREFERRED
#   NEUTRAL
#   DISFAVORED
#   REFUSED
#
# I set a hard constraint to handle "REFUSED", and arbitrarily, I set these
# benefit values for the others
benefit_availability = dict()
benefit_availability['PREFERRED']  = 3
benefit_availability['NEUTRAL']    = 2
benefit_availability['DISFAVORED'] = 1

# Not used, since this is a hard constraint. But the code needs this to be a
# part of the benefit. I can ignore these in the code, but let's keep this
# simple
benefit_availability['REFUSED' ] = -1000

# I want to favor people getting more extra shifts at the start to balance
# things out: somebody getting one more shift on their pile shouldn't take
# shifts away from under-utilized people
benefit_boost_leq_bound = \
    {2: .2,
     3: .3,
     4: .4,
     5: .5}

vars_Nshifts_leq = \
    pulp.LpVariable.dicts("Assignments",
                          (humans,benefit_boost_leq_bound.keys(),),
                          None,None, # bounds; unused, since these are binary variables
                          pulp.LpBinary)
# Constrain vars_Nshifts_leq variables to do the right thing
for h in humans:
    for b in benefit_boost_leq_bound.keys():
        prob += (pulp.lpSum([vars[h][s] for s in shifts.keys()])
                 >= (1 - vars_Nshifts_leq[h][b])*(b+1),
                 f"{h} at least {b} shifts: lower bound")
        prob += (pulp.lpSum([vars[h][s] for s in shifts.keys()])
                 <= Nshifts_max - vars_Nshifts_leq[h][b]*(Nshifts_max-b),
                 f"{h} at least {b} shifts: upper bound")

benefits = dict()
for h in humans:
    benefits[h] = \
        pulp.lpSum([vars[h][s] * benefit_availability[shifts[s][h]] \
                    for s in shifts.keys()]) + \
        pulp.lpSum([vars_Nshifts_leq[h][b] * benefit_boost_leq_bound[b] \
                    for b in benefit_boost_leq_bound.keys()])

benefit_total = \
    pulp.lpSum([benefits[h] \
                for h in humans])

prob += (
    benefit_total,
    "happiness",
)

solution_count = 0
while solution_count < 5:
    prob.solve()

    if pulp.LpStatus[prob.status] == "Optimal":
        print(f'===== Solution {solution_count} ======')
        report_solution_to_console(vars)
        report_solution_to_ics('/tmp/tst.ics', vars)
        report_solution_summary_to_console(vars)

        prob += ( pulp.lpSum([vars[h][s] \
                              for h in humans \
                              for s in shifts.keys() \
                              if vars[h][s].value() == 1]) <= len(shifts.keys())-1,
                  f'Do not repeatedly return solution {solution_count}' )
    else:
        break

    solution_count += 1
    print('==================')

print("Done!")
