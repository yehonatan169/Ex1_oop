
def dist(src, dest, elev):  # return the time to make the travel from source to destination
    speed = float(elev.speed)
    return (abs(int(src) - int(dest)) / speed) + float(elev.startTime) + float(elev.stopTime) + float(
        elev.closeTime) + float(elev.openTime)


def trampPossibilityExternal(c, el):
    allData = []
    rightIndex = -1
    minimum = 0
    u = 0
    for i in range(len(el)):
        data = trempPossibilityInternal(c, el[i].elevators_stations(), el[i].elevator_times(), i)
    if data is not None:
        allData.append(data)

    if len(allData) == 0:
        return -1

    for z in allData:
        if rightIndex == -1:
            minimum = z[7]
            rightIndex = u
        time = z[7]

        if time < minimum:
            minimum = time
            rightIndex = u
        u += 1

    if allData[rightIndex][0] == 1:
        c.index = allData[rightIndex][6]  # 5
    elif allData[rightIndex][1] == 1:
        el[allData[rightIndex][6]].elevators_stations().insert(allData[rightIndex][4], c.destention)
        el[allData[rightIndex][6]].elevator_times().insert(allData[rightIndex][4], allData[rightIndex][7]
                                                            + dist(c.source, c.destention, el[allData[rightIndex][6]]))

        for t in range(allData[rightIndex][4] + 1, len(el[allData[rightIndex][6]].elevator_times())):
            el[allData[rightIndex][6]].elevator_times()[t] += (
                    el[allData[rightIndex][6]].startTime + el[allData[rightIndex][6]].stopTime +
                    el[allData[rightIndex][6]].openTime + el[allData[rightIndex][6]].closeTime)

        c.index = allData[rightIndex][6]

    elif allData[rightIndex][2] == 1:
        el[allData[rightIndex][6]].elevator_times().insert(allData[rightIndex][3], allData[rightIndex][7] +
                                                            dist(c.source,
                                                                el[allData[rightIndex][6]].elevators_stations()
                                                                [allData[rightIndex][3] - 1],
                                                                el[allData[rightIndex][6]]))

        el[allData[rightIndex][6]].elevators_stations().insert(allData[rightIndex][3], c.source)

        for x in range(allData[rightIndex][3] + 1, len(el[allData[rightIndex][6]].elevators_stations())):
            el[allData[rightIndex][6]].elevator_times()[x] += (
                    el[allData[rightIndex][6]].startTime + el[allData[rightIndex][6]].stopTime +
                    el[allData[rightIndex][6]].openTime + el[allData[rightIndex][6]].closeTime)

        c.index = allData[rightIndex][6]
    else:
        el[allData[rightIndex][6]].elevator_times().insert(allData[rightIndex][3], allData[rightIndex][7] +
                                                            dist(c.source,
                                                                el[allData[rightIndex][6]].elevators_stations()
                                                                [allData[rightIndex][3] - 1],
                                                                el[allData[rightIndex][6]]))

        el[allData[rightIndex][6]].elevators_stations().insert(allData[rightIndex][3], c.source)

        for y in range(allData[rightIndex][3] + 1, len(el[allData[rightIndex][6]].elevator_times())):
            el[allData[rightIndex][6]].elevator_times()[y] += (
                    el[allData[rightIndex][6]].startTime + el[allData[rightIndex][6]].stopTime +
                    el[allData[rightIndex][6]].openTime + el[allData[rightIndex][6]].closeTime)

        el[allData[rightIndex][6]].elevator_times().insert(allData[rightIndex][4] + 1, allData[rightIndex][7] +
                                                            dist(c.source, c.destention, el[allData[rightIndex][6]]))

        el[allData[rightIndex][6]].elevators_stations().insert(allData[rightIndex][4] + 1, c.destention)
        for v in range(allData[rightIndex][4] + 2, len(el[allData[rightIndex][6]].elevator_times())):
            el[allData[rightIndex][6]].elevator_times()[v] += (
                    el[allData[rightIndex][6]].startTime + el[allData[rightIndex][6]].stopTime +
                    el[allData[rightIndex][6]].openTime + el[allData[rightIndex][6]].closeTime)

        c.index = allData[rightIndex][6]

    return rightIndex


def trempPossibilityInternal(c, stop_sta, time_sta, index_elev):
    i = 0
    arr_to_add = []
    for p in range(9):
        arr_to_add.append(0)

    # consider possibility for binary search for O(log(n)) to find first index bigger than c.time instead of current liniar search
    while i < len(time_sta) and time_sta[i] <= float(c.time):
        i += 1  # put back later
    if i == len(time_sta):
        return None

    while i + 1 < len(stop_sta):
        j = i
        while i + 1 < len(stop_sta) and stop_sta[i] < stop_sta[i + 1]:
            i += 1
        if stop_sta[j] <= c.source < c.destention <= stop_sta[i]:
            arr_to_add[5] = i - 1
            arr_to_add[6] = index_elev
            arr_to_add[8] = 1
            k = i
            l = j
            while c.source >= stop_sta[l]:
                if c.source == stop_sta[l]:
                    arr_to_add[1] = 1
                    arr_to_add[7] = time_sta[l]
                    break
                l += 1
                arr_to_add[3] = l
                arr_to_add[7] = time_sta[l - 1]

            while c.destention <= stop_sta[k]:
                if c.destention == stop_sta[k]:
                    arr_to_add[2] = 1
                    if arr_to_add[1] == 1:
                        arr_to_add[0] = 1
                    break

                arr_to_add[4] = k
                if c.destention > stop_sta[k - 1]:
                    break
                k -= 1

            return arr_to_add  # new line
        j = i
        while i + 1 < len(stop_sta) and stop_sta[i] > stop_sta[i + 1]:
            i += 1

        if stop_sta[j] >= c.source > c.destention >= stop_sta[i]:
            arr_to_add[5] = i - 1
            arr_to_add[6] = index_elev
            arr_to_add[8] = -1
            k = i
            l = j
            while c.source <= stop_sta[l]:
                if c.source == stop_sta[l]:
                    arr_to_add[1] = 1
                    l += 1
                    arr_to_add[3] = l
                    arr_to_add[7] = time_sta[l - 1]
                    break
                l += 1
                arr_to_add[3] = l
                arr_to_add[7] = time_sta[l - 1]

            while c.destention >= stop_sta[k]:
                if c.destention == stop_sta[k]:
                    arr_to_add[2] = 1
                    if arr_to_add[1] == 1:
                        arr_to_add[0] = 1
                    arr_to_add[4] = k
                    break
                arr_to_add[4] = k
                if c.destention < stop_sta[k - 1]:
                    break
                k -= 1
            return arr_to_add
    return None


def checkShortestTime(c, el):
    mine_time = 0
    min_current_time = 0
    elev_current_index = 0
    elevator_to_allocate = 0
    for i in el:
        time = 0
        for k in range(0, len(i.elevators_stations()) - 1):
            time += dist(i.elevators_stations()[k], i.elevators_stations()[k + 1], el[elev_current_index])
        time += dist(i.elevators_stations()[len(i.elevators_stations()) - 1], c.source, el[elev_current_index])
        current_time = dist(c.source, c.destention, el[elev_current_index])
        time += current_time

        if elev_current_index == 0:
            mine_time = time
            min_current_time = current_time

        if time < mine_time:
            mine_time = time
            min_current_time = current_time
            elevator_to_allocate = elev_current_index
        elev_current_index += 1

    if c.source != el[elevator_to_allocate].elevators_stations()[
        len(el[elevator_to_allocate].elevators_stations()) - 1]:
        el[elevator_to_allocate].elevators_stations().append(c.source)
        el[elevator_to_allocate].elevator_times().append(mine_time - min_current_time)

    el[elevator_to_allocate].elevators_stations().append(c.destention)

    el[elevator_to_allocate].elevator_times().append(mine_time)
    c.index = elevator_to_allocate

    return elevator_to_allocate


def proper_algo(calist, el):
    for k in calist:
        t = trampPossibilityExternal(k, el)
        if t != -1:
            continue
        t = checkShortestTime(k, el)
