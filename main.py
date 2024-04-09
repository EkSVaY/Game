import story
import random
import events


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
kvartal = 0


if story.story_line():
    '''
    PART_1. The history of Arakis
    '''
    if story.a_part_1(rep_atreides, army_atreides, tech_atreides, spice_atreides):
        rep_atreides += 200
    else:
        army_atreides -= 4
        rep_atreides -= 50
        worms_freeman -= 1

    input("\nPress Enter\n")

    if story.h_part_1(rep_harcoon, army_harcoon, tech_harcoon, spice_harcoon):
        army_freeman -= 5
        rep_harcoon += 50
    else:
        army_harcoon -= 4
        rep_harcoon -= 50

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

    story.part_1_final(amount_spice)
    input("\nЧтобы начать год - Press Enter\n")

    '''
    RANDOM EVENTS
    '''
    for i_events in rand_events:

        kvartal += 1

        atr_kvest = events.atreides(i_events)
        input("\nPress Enter\n")
        har_kvest = events.harcoon(i_events)
        input("\nPress Enter\n")
        emp_kvest = events.empire(i_events)
        input("\nPress Enter\n")
        free_kvest = events.freeman(i_events)

        if i_events == 1:

            if atr_kvest:
                army_atreides -= 9
                tech_atreides += 1
            else:
                army_atreides -= 1010
                rep_harcoon += 100

            if emp_kvest:
                army_freeman -= 5
                if conspiracies_empire > 0:
                    conspiracies_empire -= 1
            else:
                conspiracies_empire += 1

            if free_kvest:
                water_freeman /= 2
                army_freeman /= 4
                belief_freeman += 100

            if har_kvest == 1:
                spice_harcoon += 5
            elif har_kvest == 2:
                army_harcoon = int(army_harcoon * 0.75)

        if i_events == 2:

            if atr_kvest:
                spice_atreides += 5
                rep_atreides += 100
            else:
                water_freeman += 100
                rep_atreides -= 10

            if emp_kvest:
                money_empire -= 500000
                fleet_empire -= 6
                approval_empire -= 3

            if free_kvest:
                water_freeman -= 1500
            else:
                army_freeman /= 2

            if har_kvest == 1:
                tech_harcoon = int(tech_harcoon * 1.25)
            elif har_kvest == 2:
                tech_harcoon -= 20
            elif har_kvest == 3:
                rep_harcoon -= 5
            elif har_kvest == 4:
                army_harcoon -= 2500

        if i_events == 3:
            if not atr_kvest:
                army_atreides -= 1000
                spice_atreides -= 2
            else:
                rep_atreides += 10

            if emp_kvest == 1:
                fleet_empire -= 20
            elif emp_kvest == 2:
                fleet_empire -= 10
            elif emp_kvest == 3:
                approval_empire -= 1
                fleet_empire -= 20

            if free_kvest == 2:
                worms_freeman -= 2
            elif free_kvest == 3:
                worms_freeman -= 1
            elif free_kvest == 4:
                army_harcoon /= 2
                worms_freeman -= 1
            elif free_kvest == 5:
                army_harcoon -= 10000
                army_atreides -= 10000
                worms_freeman -= 2

            if har_kvest:
                rep_harcoon -= 5

        if i_events == 4:

            if atr_kvest:
                rep_atreides -= 10

            if emp_kvest == 2:
                approval_empire -= 1
            elif emp_kvest == 3:
                approval_empire += 1

            if free_kvest == 1:
                army_freeman *= 2
            elif free_kvest == 2:
                worms_freeman *= 2
            elif free_kvest == 3:
                belief_freeman *= 2
            elif free_kvest == 4:
                worms_freeman *= 2

            if har_kvest:
                rep_harcoon += 5
            else:
                spice_harcoon -= 2
                rep_harcoon -= 5

        spice_atreides += 5
        spice_harcoon += 5
        print(f"Итоги за {kvartal} квартал года")
        print(f"\nДом Атридесов: Репутация {rep_atreides}, Армия {army_atreides},"
              f" Техника {tech_atreides}, Специи {spice_atreides}\n")
        print(f"Дом Харконненов: Репутация {rep_harcoon}, Армия {army_harcoon},"
              f" Техника {tech_harcoon}, Специи {spice_harcoon}\n")
        print(f"Империя: Деньги {money_empire}, флот {fleet_empire}, заговоры {conspiracies_empire},"
              f" доверие великих домов {approval_empire}\n")
        print(f"Фримены: Люди {army_freeman}, Шаи-Хулуды {worms_freeman}, Вода {water_freeman},"
              f" Вера {belief_freeman}\n")
        input("\nPress Enter\n")
else:
    print("Игра окончена!")
