import random
import math
wight = 100
hight = 100
counter_of_animals = 10
counter_of_food = 20
counter_of_death = 0
animals_position_w = []
animals_position_h = []
food_position_w = []
food_position_h = []
animals_speed = []
animals_size = []
animals_strategy = []
animals_sex = []
animals_time_for_getting_food = []
choosen_food = []
who_alive = []
marrige_m = []
marrige_f = []
time = 0
male = 5
female = 5
iterations = 20
#start
for i in range(counter_of_animals):
    animals_size.append(1)
    animals_speed.append(1)
for a in range(male):
    animals_sex.append("m")
for a in range(female):
    animals_sex.append("f")
#КООРДИНАТЫ ЗВЕРЕЙ
for n in range(iterations):
    for i in range(counter_of_animals):
        a = random.randint(0,2)
        if a == 0:
            pos_w = random.randint(0,2) * 100
            pos_h = random.randint(0,hight + 1)
        else:
            pos_h = random.randint(0,2) * 100
            pos_w = random.randint(0, wight + 1)
        animals_position_h.append(pos_h)
        animals_position_w.append(pos_w)
    #КООРДИНАТЫ ЕДЫ
    for i in range(counter_of_food):
        food_w = random.randint(1,wight)
        food_h = random.randint(1,hight)
        food_position_h.append(food_h)
        food_position_w.append(food_w)
    #ПОИСК БЛИЖАЙШЕЙ ЕДЫ
    for i in range(counter_of_animals):
        pos_w = animals_position_w[i]
        pos_h = animals_position_h[i]
        S_min = 1000
        index = 0
        for a in range(counter_of_food):
            food_w = food_position_w[a]
            food_h = food_position_h[a]
            S = math.sqrt(abs(pos_w - food_w) ** 2 + abs(pos_h - food_h) ** 2)
            if S < S_min:
                index = a
                S_min = S
        time_to_get_food = S_min / animals_speed[i]
        animals_time_for_getting_food.append(time_to_get_food)
        choosen_food.append(index)
    #КТО ЧТО ЕСТ
    for i in range(counter_of_animals):
        _list = choosen_food
        if _list[i] != -1:
            choosen = _list[i]
        who_choose = []
        for a in range(len(_list)):
            if _list[a] == choosen:
                who_choose.append(a)
        time_min = 1000
        ind = -1
        for a in who_choose:
                if animals_time_for_getting_food[a] <= time_min:
                    time_min = animals_time_for_getting_food[a]
                    ind = a
        if ind != -1:
            who_alive.append(ind)
            choosen_food[ind] = -1
            who_choose.remove(ind)
            for c in who_choose:
                animals_speed[c] = -1
                animals_size[c] = -1
                animals_position_h[c] = -1
                animals_position_w[c] = -1
                animals_time_for_getting_food[c] = -1
                choosen_food[c] = -1
                animals_sex[c] = -1
                counter_of_death += 1
                who_choose.remove(c)
    #ПОИСК ПАРТНЕРА
    counter_of_f = 0
    counter_of_m = 0
    for i in who_alive:
        if animals_sex[i] == "m":
            counter_of_m += 1
        else:
            counter_of_f += 1
    if counter_of_m == 0 or counter_of_f == 0:
        print("Все погибли, Милорд.", "кол-во циклов - " + str(n + 1))
        raise SystemExit
    __list = who_alive
    for i in __list:
        if animals_sex[i] == "f":
            best_animal = -1
            best_char = -1
            if animals_size[i] > animals_speed[i]:
                _main = "size"
            elif animals_size[i] < animals_speed[i]:
                _main = "speed"
            else:
                _main = "any"
            for a in __list:
                if animals_sex[a] == "m":
                    if _main == "size" and animals_size[a] > best_char:
                        best_char = animals_size[a]
                        best_animal = a
                    elif _main == "speed" and animals_speed[a] > best_char:
                        best_char = animals_speed[a]
                        best_animal = a
                    elif _main == "any" and max(animals_size[a],animals_speed[a]) > best_char:
                        best_char = max(animals_size[a],animals_speed[a])
                        best_animal = a
                if best_animal != -1:
                    try:
                        __list.remove(best_animal)
                        __list.remove(i)
                        marrige_m.append(best_animal)
                        marrige_f.append(i)
                        if _main == "speed":
                            child_speed = best_char + random.randint(-2, 3)
                            if random.randint(0, 2) == 0:
                                child_size = animals_size[a]
                            else:
                                child_size = animals_size[i]
                        elif _main == "size":
                            child_size = best_char + random.randint(-2, 3)
                            if random.randint(0, 2) == 0:
                                child_speed = animals_speed[a]
                            else:
                                child_speed = animals_speed[i]
                        else:
                            child_size = max(animals_size[a], animals_size[i]) + random.randint(1, 3)
                            child_speed = max(animals_speed[a], animals_speed[i]) + random.randint(1, 3)
                        k = random.randint(0, 2)
                        if k == 0:
                            pos_w = random.randint(0, 2) * 100
                            pos_h = random.randint(0, hight + 1)
                        else:
                            pos_h = random.randint(0, 2) * 100
                            pos_w = random.randint(0, wight + 1)
                        animals_position_h.append(pos_h)
                        animals_position_w.append(pos_w)
                        animals_speed.append(child_speed)
                        animals_size.append(child_size)
                        if random.randint(0, 2) == 0:
                            animals_sex.append("f")
                        else:
                            animals_sex.append("m")
                    except ValueError:
                        е = 0
    #ЧИСТКА
    while -1 in animals_speed:
        animals_speed.remove(-1)
    while -1 in animals_sex:
        animals_sex.remove(-1)
    while -1 in animals_size:
        animals_size.remove(-1)
    animals_time_for_getting_food = []
    choosen_food = []
    animals_position_w = []
    animals_position_h = []
    marrige_m = []
    marrige_f = []
    who_alive = []
    counter_of_animals = len(animals_speed)
    print(counter_of_animals, animals_speed, animals_size, animals_sex)