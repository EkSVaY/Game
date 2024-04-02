import story
import random

rep_atreides = 0
rep_harcoon = 0
army_atreides = 100_000
army_harcoon = 150_000
army_freeman = 5_000
spice_atreides = 0
spice_harcoon = 0
tech_atreides = 100
tech_harcoon = 110
money_empire = 6_000_000
fleet_empire = 100
conspiracies_empire = 0
approval_empire = 14
worms_freeman = 100
water_freeman = 15_000
belief_freeman = 0
rand_events = [1, 2, 3, 4]
random.shuffle(rand_events)


if story.story_line():
    '''
    PART_1. The history of Arakis
    '''
    if story.a_part_1(rep_atreides, army_atreides, tech_atreides, spice_atreides):
        rep_atreides += 10
    else:
        army_atreides -= 4
        rep_atreides -= 10
        worms_freeman -= 1

    input("\nPress Enter\n")

    if story.h_part_1(rep_harcoon, army_harcoon, tech_harcoon, spice_harcoon):
        army_freeman -= 5
        rep_harcoon += 10
    else:
        army_harcoon -= 4
        rep_harcoon -= 10

    input("\nPress Enter\n")

    amount_spice = story.i_part_1(money_empire, fleet_empire, conspiracies_empire, approval_empire)

    input("\nPress Enter\n")

    freeman_part_1 = story.f_part_1(army_freeman, worms_freeman, water_freeman, belief_freeman)

    if freeman_part_1 == 1:
        army_freeman -= 100
        tech_atreides -= 2
    elif freeman_part_1 == 2:
        army_freeman -= 200
        tech_atreides -= 1
    elif freeman_part_1 == 3:
        army_freeman -= 300
    else:
        tech_atreides -= 3

    input("\nPress Enter\n")



else:
    print("Игра окончена!")