def empire(events):


def atreides(events):



def harcoon(events):
    if events == 1:
        chest = int(input('Ваша разведка при выполнении задания наткнулись на странный сундук, '
                          'обрисованный древними рунами. \n'
              'Какое решение вы примете? Опасайтесь в сундуке может быть как драгоценности, так и нечисть \n'
              '1) Открыть его и посмотреть что внутри \n'
              '2) Поберечься и приказать закопать сундук \n'
                          'Ответ - '))
        result = random.randint(0, 1)
        if chest == 1:
            if result == 1:
                if result == 1:
                    print('Поздравляем!!! Вы открыли сундук и нашли внутри специи')
                    spice += 5
                else:
                    army /= 1.25
                    print('О нет!!! '
                          'Вам не повезло, вы открыли сундук, а внутри вирусная инфекция! Скорее спасайтесь!!! \n'
                          'В результате вируса вы потеряли бойцов')
        elif chest == 2:
            print('Мудрое решение! Лучше перестраховаться!')
        else:
            print('Воины не разобрали вашего указа и закопали сундук там где его никто не найдет!')

    if events == 2:
        sleep = int(input('Сегодня ночью вашему бойцу приснился сон, в котором якобы можно модернизировать технику \n'
                          'Если вы примите его рекомендации, то можно нехило увелечить количество техники!\n'
                          'Однако есть шанс, что это был просто сон и вы можете потерять технику в результате'
                          'неудачных опытов. Какое решение примете?\n'
                          '1) Послушать бойца и провести опыты \n'
                          '2) Проигнорировать бойца и отправить его готовить пищу для отряда \n'
                          'Ответ - '))
        result = random.randint(0, 1, 2)
        if sleep == 1:
            if result == 1:
                print('Его сон оказался вещим и опыты прошли успешно! В результате опытов ваша техника увелечилась '
                      'в 1.25 раза!!! Вам очень повезло! \n')
                tech *= 1.25
            else:
                print('Опыты прошли безуспешно. Вам не удалось увелечить количество техники. \n'
                      'Из-за выхода техники из строя вы потеряли 20 единиц техники. Очень жаль\n')
                tech -= 20
        if sleep == 2:
            if result == 0 or result == 2:
                print('Возможно вы приняли верное решение. Боец ушел расстроенный со своими чертежами \n')
            else:
                print('Боец ушел расстроенный, Возможно, стоило мягче к нему отнестись.\n')
                murder = int(input('Вечером вам доложили, что этот боец минирует лагерь. Как вы к этому отнесетесь?\n'
                      '1) Произвести публичную казнь, для мотивации отряда\n'
                      '2) Убить его по-тихому чтобы не подимать шума\n'
                      'Ответ -'))
                if murder == 2:
                    print('Убийство свершилось успешно, терракт предотвращен.\n'
                          'Однако по лагерю пошли слухи и вы потеряли репутацию. \n')
                    rep -= 5
                elif murder == 1:
                    print('Некоторая часть войска не разделилас вами ваших интересов и произошел бунт \n'
                          'В результате предотвращения бунта вы потеряли бойцов, а именно 2500!\n'
                          'Впредь будьте внимательнее!!!')
                    army -= 2500
    if events == 3:
        print('Ночью, один из подчиненных увидел вас с новой наложницей. Об этом быстро узнали во всем лагере.\n'
              'Вы потеряли репутацию, многие назвали вас извращенцем. Вам должно быть стыдно!!!\n')
        rep -= 5
    if events == 4:
        game = int(input('Посреди ночи вы слышите какеи-то крики. \n'
              'Проверив, Вы обнаружили, что бойцы вашего лагеря устроили азартные игры.\n'
              'Какое решение вы примете?\n'
              '1) Разогнать всех под угрозой расправы\n'
              '2) Попробовать поиграть вместе с ними, дабы сплочиться с коллективом\n'
              'Ответ - '))
        if game == 1:
            print('Бойцы были очень недовольны вашим поступком. '
                  'Однако, ваш гнев заставляет войско еще больше уважать вас.\n'
                  'Ваша репутация повысилась')
            rep += 5
        if game == 2:
            print('Вы вошли во вкус и проиграли очень много своим же бойцам. Часть бойцов вас осуждает.\n'
                  'Вы теряете специи из собственных сбережений и ваша репутация снижается.\n')
            rep -= 5

def freeman(events):
