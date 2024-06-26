import time
import gfaphic1
import random


def story_line():
    print(gfaphic1.GALAXY)
    time.sleep(3)
    print("\nНаша вселенная полна тайн и загадок. Одной из таких является тайна судьбы\nвеликих домов на планете"
          " Аракис…\n")
    time.sleep(3)
    print(gfaphic1.ARAKIS)
    time.sleep(3)
    print("\nПланета Аракис. Раньше поля этой планеты пестрили красотой красок, мировой океан занимал 70 %"
          " её площади,\n"
          "а её жители жили счастливо. Это прежде прекрасное место, наполненное жизнью, сейчас же лишь безжизненная"
          " пустыня.\nТак чем же оно привлекло великие дома?\n")
    time.sleep(3)
    print("\n«Специи – ценнейший ресурс, месторождение которого установлено лишь здесь!\nВам"
          " предстоит побороться за этот ресурс.\n")
    time.sleep(3)
    print("\nВам предстоит сделать сложный выбор: какую сторону конфликта на Аракисе будете представлять именно вы?\n"
          "1) Фримены - коренное население Аракиса. За долгие годы жизни в пустынных условиях полностью к ним"
          " приспособились.\n"
          "Умеют перерабатывать различные жидкости в питьевую воду. Разрозненные племена фрименов живут в разных"
          " местах Аракиса\n"
          "Являются настоящими владельцами Аракиса, ведь приручили самого сверепого хищника этих земель - Шаи-Хулуда."
          " Подвержены\n"
          "Фримены защищают свою планету от захватчиков всеми методами. Очень подвержены вере, ждут пришествие миссии\n"
          "Ресурсы: Люди, Вода, Шаи-Хулуды, Вера\n\n"
          "2) Дом Атридесов - опытные воины и отличные дипломаты. Империя вручила Аракис дому для заполучения\n"
          "контроля над специями. Атридесы предпочитают победу бескровными методами. Часто внушают свою веру\n"
          "другим народам. Имеют огромный военный и технический ресурс, стремятся увеличить репутацию\n"
          "Ресурсы: Репутация, Специи, Армия, Техника\n\n"
          "3) Дом Харконненов. Сумашедшие фанатики, эмоционально неуравновешенные бойцы. Стремяться уничтожить свох\n"
          "врагов любыми методами (заговоры, обман, убийства, террор). Получают широкую поддержку от Империи\n"
          "в борьбе против Фрименов. Очень пекуться о своей репутации и отвечают за неё головой перед империей\n"
          "Ресурс: Репутация, Специи, Армия, Техника\n\n"
          "4) Империя. Царство заговоров. Управляет всеми домами. Продаёт специи, следит, чтобы специи добывались.\n"
          "Ненавидит непослушные дома, стремится внушить страх всем во вселенной.\n"
          "Ресурсы: Одобрение великих домов, Заговоры, Космический флот, Деньги")
    time.sleep(3)
    print("\nПравила игры:\n"
          "- Выберите сторону!\n"
          "- Выбирайте варианты ответов цифрами!\n"
          "- Выбор влияет на ваши ресурсы и на ресурсы других сторон!\n"
          "- Случайные события независимо от вас дают положительный или отрицательный эффект на ресурсы!\n")
    return (int(input("Начинаем (1 - да, 2 - нет)? Ответ - "))) == 1


def a_part_1(rep, army, tech, spice):
    print("=========================================================================================================\n"
          "                                               Глава 1\n"
          "=========================================================================================================\n")

    print("=========================================================================================================\n"
          "Прибытие Атрейдесов\n"
          "=========================================================================================================\n")
    time.sleep(1)
    print(gfaphic1.ARRIVAL)
    time.sleep(1)

    print(f"Дом Атридесов: Репутация {rep}, Армия {army}, Техника {tech}, Специи {spice}\n\n")

    time.sleep(1)
    print("Первыми на планету Аракис прибыли Атридесы...\n"
          "Они не приняли на себя гнева Аракиса, но были готовы к худшему.\n"
          "Их план покорения планеты состоял в настоящей дипломатии.\n"
          "Они пришли договориться с Фрименами!\n")

    time.sleep(3)
    print(gfaphic1.DESERT_CHALLENGE)

    while True:
        choise = int(input("\nГде в пустыне спрятался Фримен? (Выберите цифру 1 - 5): "))
        if choise == 2:
            print("\nПоздравляю, вы поймали Фримена! Но, кажется, он от этого не в восторге :(\n"
                  "Он начал что-то говорить, разберитесь с его речью и ответьте ему!")
            break
        else:
            print("Здесь никого нет!")

    print("\n-етёдйу ен ыв илсе, укинхет ушав юсв мижотчину ым, отсем ен ьседз ысрусер\n"
          "еижуч мищюуров, макажуч, ялмез ашан отэ!\n")

    dialog = int(input("1) А - Мы пришли договориться, не нужно никого убивать (Чувство)\n"
                       "2) А - Мы дадим отпор, если вы нападёте (Сила)\n"
                       "3) А - Мы пришли дать вашей планете 2 шанс (Разум)\n"
                       "Ответ - "))
    if dialog == 1 or dialog == 3:
        print("Ф - Вы понимаете мою речь и не желаете войны? Какие-то вы странные захватчики!\n"
              "Но в любом случае, держитесь подальше от наших мест, и не бегайте по песку, иначе\n"
              "спровоцируете Шаи-Хулуда")
        print("P.S. В качестве жеста доброй воли вы отпустили Фримена.")
        return True
    elif dialog == 2:
        print("Фримен выхватил кинжал и убил 4 людей, после чего скрылся в песках пустыни!\n"
              "Подождав вы услышали странный шум и тут появился он... ШАИ-ХУЛУД")
        time.sleep(5)
        print(gfaphic1.WORM)
        print("Вам пришлось сразиться с этим великим созданием, вы победили и показали свою силу!")
        return False


def h_part_1(rep, army, tech, spice):
    print("=========================================================================================================\n"
          "Прибытие Харконненов\n"
          "=========================================================================================================\n")

    print(f"Дом Харконненов: Репутация {rep}, Армия {army}, Техника {tech}, Специи {spice}\n")

    print("Харконнены прибыли на планету и, подобая своей жестокости, начали сразу же истреблять всё живое вокруг.\n"
          "Но они не ожидали, что для них уже подготовлена засада от Фрименов.\n")

    print(gfaphic1.QUES_2)

    shot = int(input("\nПоразите фрименов до того, пока они вас настигнут! Стреляйте, указывая номера целей! \n"
                     "Вы готовы стрелять? (1 - да, 2 - нет): "))
    if shot == 1:
        start = time.time()
        amount = 0
        for _ in range(5):
            gun_shot = int(input("\nВыстрелить в цель номер - "))
            if gun_shot in [9, 12, 5, 3, 1]:
                print("Точно в цель!")
                amount += 1
            else:
                print("Мимо!")
        end = time.time()
        if int(end - start) < 10 and amount == 5:
            print(f"\nВы уничтожили нападавших за {int(end-start)} секунд. Настала пора разворачивать своё\n"
                  f"собственное поселение. Пора начинать добычу cпеций. Как же жаль, что планета встретила\n"
                  f"вас именно так. Что же предвещает данное событие?")
            return True
        else:
            print("\nВы потеряли своих бойцов и с позором вернулись на свой корабль. Империя не простит такой\n"
                  "неудачи. Впредь будьте бдительнее к окружающему вас миру!")
            return False
    else:
        print("\nВы оказались не готовы к неожиданному нападению Фрименов! Вы потеряли своих бойцов и с позором"
              " вернулись\n"
              "на свой корабль. Империя не простит такой неудачи. Впредь будьте бдительнее к окружающему вас миру!\n")
        return False


def i_part_1(money_empire, fleet_empire, conspiracies_empire, approval_empire):
    print("=========================================================================================================\n"
          "Империя\n"
          "=========================================================================================================\n")

    print(gfaphic1.EMPIRE)

    print(f"Империя: Деньги {money_empire}, флот {fleet_empire}, заговоры {conspiracies_empire},"
          f" доверие великих домов {approval_empire}\n")

    print("Получив первую информацию о событиях на Аракисе, Император распорядился составить план по добыче специй.\n"
          "Чтобы данный план отражал реальную потребность в специи, созвали представителей со всех великих домов\n")

    print("Обсудите с великими домами, какое количество специй необходимо добыть на Аракисе (Отвечайте цифрами)\n")

    dialog = int(input("ВД - Император, каждый год наблюдается тенденция увеличения потребления специи.\n"
                       "В этом году их потребление достигло 30 тысяч тонн. Нам необходимо увеличивать производство!\n"
                       "Выберите ответ:\n"
                       "1) Согласен. Добычу стоит повышать, таким образом мы повысим благополучие нашего населения.\n"
                       "2) Не согласен. Добычу необходимо снижать. Наш народ слишком привык к хорошему. Ради\n"
                       " специи мы жертвуем лучшими бойцами империи!\n"
                       "Ответ: "))
    if dialog == 1:
        print("\nВД - Это мудрое решение! Какое бы количество специй вы предложили добыть?\n")

        while True:
            amount_spice = int(input("Введите целое число (Тыс. тонн специй): "))
            if amount_spice > 50:
                print("ВД - Это слишком большое число, наши технологии в силах добыть не более 50 тысяч тонн!\n")
            elif amount_spice <= 30:
                print("ВД - Вы же сами сказали, что мы будем повышать добычу специи!\n")
            else:
                print(f"ВД - прекрасное решение! Добываем столько!\n")
                return amount_spice
    if dialog == 2:
        print("ВД - Это мудрое решение! Какое бы количество специй вы предложили добыть?\n")

        while True:
            amount_spice = int(input("\nВведите целое число (Тыс. тонн специй): "))
            if amount_spice > 30:
                print("ВД - Вы же сказали, что мы будем понижать использование специи!\n")
            elif amount_spice < 10:
                print("ВД - Император! Мы не можем полностью отказаться от специи, народ всбунтуется!\n")
            else:
                print(f"ВД - прекрасное решение! Добываем столько!\n")
                return amount_spice
    else:
        print("ВД - Вы ничего не ответили? Значит оставляем добычу специй на прежнем уровне!")
        return 30


def f_part_1(people, worms, water, belief):
    print("=========================================================================================================\n"
          "Фримены\n"
          "=========================================================================================================\n")

    print(f"Фримены: Люди {people}, Шаи-Хулуды {worms}, Вода {water}, Вера {belief}\n")

    print("Вы были озадачены прибытием сразу двух крупных групп захватчиков на вашу планету. Но это не впервой.\n"
          "В такие моменты все великие вожди Фрименов готовились к крупной борьбе. Вы начали с нападений на\n"
          "технику, добывающую специи\n")

    print("Сегодня вы получили карту предполагаемых мест добычи специй. Вы приняли решение разработать план нападения\n"
          "на технику дома Атрейдесов, используя только ваших людей (На каждую операцию - 100 человек)\n")

    print(gfaphic1.MAP)

    dead_freeman = 0

    for _ in range(3):
        fight = int(input("Какую точку вы будете атаковать: \n"))
        result = random.randint(0, 1)
        if fight in [1, 2, 3]:
            if result == 0:
                print("К сожалению, Атрейдесы были готовы к вашему нападению. Весь отряд был уничтожен\n")
                dead_freeman += 100
            elif result == 1:
                print("Операция прошла успешно. Ваш отряд уничтожил технику врага без проблем\n")
        else:
            print("Ваша группа заблудилась в песках Аракиса и пропала навсегда!\n")
            dead_freeman += 100

    print(f"Потери за операцию составили {dead_freeman}")

    if dead_freeman == 100:
        return 1
    elif dead_freeman == 200:
        return 2
    elif dead_freeman == 300:
        return 3
    return 0


def part_1_final(amount_spice):
    print("=========================================================================================================\n"
          "                                        Задача на год текущий год\n"
          "=========================================================================================================\n")
    print(f"Империя поручила домам Атридесов и Харконненов добыть {amount_spice} тонн специй.\n")
    print("Задачи Фрименов:\n"
          "- Выжить\n"
          "- Изгонять захватчиков\n"
          "- Пополнять свои ресурсы\n")
    print("Задачи Харконненов:\n"
          "- Собрать больше специи, чем Атридесы\n"
          "- Уничтожать фрименов\n"
          "- Пополнять свои ресурсы\n")
    print("Задачи Атридесов:\n"
          "- Вести депломатию\n"
          "- Собрать больше специи, чем Харконнены\n"
          "- Сохранить и приумножить свои ресурсы\n")
    print("Задачи Империи:\n"
          "- Сохранить своё величие\n"
          "- Следить за заговорами\n"
          "- Влиять на великие дома\n")


if __name__ == '__main__':
    story_line()
