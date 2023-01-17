def funkce1():
    with open("D327971_fc1.i", "r") as file:
        file_content = file.readlines()

    # vložení řádků do listu(jen těch, které se týkají  souřadnic)
    vsechny_souradnice_list = []
    for n in file_content:
        if "X" in n and "Y" in n:
            vsechny_souradnice_list.append(n)

    # print(vsechny_souradnice_list)

    # ocislovani položek listu dle čísla nástroje(0 je bez nástroje)
    a = 0
    ocislovani_nastroji = []
    for n in vsechny_souradnice_list:

        if "T" in n:
            a = int(n[-3:-1])
            sliced_string = n[:-4]
            ocislovani_nastroji.append((sliced_string, a))
        elif "T" not in n:
            sliced_string = n[:-1]
            ocislovani_nastroji.append((sliced_string, a))

    # serazeni podle cisla nastroje
    serazeni_podle_nastroje = sorted(ocislovani_nastroji, key= lambda x: x[1])
    # print(serazeni_podle_nastroje)

    # rozdeleni na hodnotu X a Y, nasledne navyšeni hodnoty v ose Y podle pravidla v zadání
    rozdeleni = []
    for n in serazeni_podle_nastroje:
        result = n[0].split("X")
        result2 = result[1].split("Y")
        rozdeleni.append(result2)
    # print(rozdeleni)

    navyseni_v_ose_y = []
    for n in rozdeleni:
        # print(n[0], n[1])
        if float(n[0]) > 50:
            res = float(n[1]) + 10
            # print(n[0], str(res))
            vlozit = (n[0], str(res))
            navyseni_v_ose_y.append(vlozit)
        else:
            # print(n[0], n[1])
            vlozit = (n[0], n[1])
            navyseni_v_ose_y.append(vlozit)
    # print(navyseni_v_ose_y)

    # vytvoreni list of tuple, kde bude tuple = ("hodnotaX", "hodnotaY", "cislonastroje")

    trojtice = []
    for n in range(len(navyseni_v_ose_y)):
        result = (navyseni_v_ose_y[n][0], navyseni_v_ose_y[n][1], serazeni_podle_nastroje[n][1])
        trojtice.append(result)
    # print(trojtice)

    xy = 0
    output_text = ""
    for n in range(len(trojtice)):
        if trojtice[n][2] > xy:
            output_text += f"X{trojtice[n][0]}Y{trojtice[n][1]}T0{trojtice[n][2]}\n"
            xy = trojtice[n][2]
        else:
            output_text += f"X{trojtice[n][0]}Y{trojtice[n][1]}\n"
    # print(output_text)
    with open("cnc.txt", "w") as file:
        file.write(output_text)

def funkce2():
    with open("D327971_fc1.i", "r") as file:
        file_content = file.readlines()

    # vložení řádků do listu(jen těch, které se týkají  souřadnic)
    vsechny_souradnice_list = []
    for n in file_content:
        if "X" in n and "Y" in n:
            vsechny_souradnice_list.append(n)

    # print(vsechny_souradnice_list)

    # ocislovani položek listu dle čísla nástroje(0 je bez nástroje)
    a = 0
    ocislovani_nastroji = []
    for n in vsechny_souradnice_list:

        if "T" in n:
            a = int(n[-3:-1])
            sliced_string = n[:-4]
            ocislovani_nastroji.append((sliced_string, a))
        elif "T" not in n:
            sliced_string = n[:-1]
            ocislovani_nastroji.append((sliced_string, a))

    # serazeni podle cisla nastroje
    serazeni_podle_nastroje = sorted(ocislovani_nastroji, key= lambda x: x[1])
    # print(serazeni_podle_nastroje)

    # rozdeleni na hodnotu X a Y, nasledne navyšeni hodnoty v ose Y podle pravidla v zadání
    rozdeleni = []
    for n in serazeni_podle_nastroje:
        result = n[0].split("X")
        result2 = result[1].split("Y")
        rozdeleni.append(result2)
    # print(rozdeleni)

    navyseni_v_ose_y = []
    for n in rozdeleni:
        # print(n[0], n[1])
        if float(n[0]) > 50:
            res = float(n[1]) + 10
            # print(n[0], str(res))
            vlozit = (n[0], str(res))
            navyseni_v_ose_y.append(vlozit)
        else:
            # print(n[0], n[1])
            vlozit = (n[0], n[1])
            navyseni_v_ose_y.append(vlozit)
    # print(navyseni_v_ose_y)

    # vytvoreni list of tuple, kde bude tuple = ("hodnotaX", "hodnotaY", "cislonastroje")

    trojtice = []
    for n in range(len(navyseni_v_ose_y)):
        result = (navyseni_v_ose_y[n][0], navyseni_v_ose_y[n][1], serazeni_podle_nastroje[n][1])
        trojtice.append(result)
    # print(trojtice)

    pouze_bloky = []
    for n in range(len(trojtice)):
        if trojtice[n][2] == 0:
            pass
        else:
            result = (float(trojtice[n][0]), float(trojtice[n][1]))
            pouze_bloky.append(result)

    # print(pouze_bloky)
    vyp_min_x = sorted(pouze_bloky, key= lambda x: x[0])
    min_x = vyp_min_x[0][0]
    vyp_max_x = sorted(pouze_bloky, key= lambda x: x[0])
    max_x = vyp_max_x[-1][0]
    vyp_min_y = sorted(pouze_bloky, key= lambda x: x[1])
    min_y = vyp_min_y[0][1]
    vyp_max_y = sorted(pouze_bloky, key= lambda x: x[1])
    max_y = vyp_max_y[-1][1]


    print(f"Min_X = {min_x}\nMax_X = {max_x}\nMin_Y = {min_y}\nMax_Y = {max_y}")




