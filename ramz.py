def sum_dight(ramz_dight):
    result = 0
    for num in ramz_dight :
        result = ramz_dight[num] + result
    return result


def ramz_is_ok (ramz_dight):
    if ramz_dight["three"] + ramz_dight ["five"] == 14 and \
        ramz_dight["one"] == ramz_dight ["two"] *2 - 1 and\
        ramz_dight["four"] == ramz_dight ["two"] + 1 and\
        ramz_dight["two"] + ramz_dight ["three"] == 10 and\
        sum_dight(ramz_dight)== 30 :
           return True


for ramz in range (0,100000):
    ramz = str(ramz).zfill(5) 
    ramz_dight =  {}
    ramz_dight ["one"] = int(ramz[0])
    ramz_dight ["two"] = int(ramz[1])
    ramz_dight ["three"] =int( ramz[2])
    ramz_dight ["four"] = int(ramz[3])
    ramz_dight ["five"] = int(ramz[4])
    if ramz_is_ok(ramz_dight):
        print(ramz)