def solution(bridge_length, weight, truck_weights):
    waiting_trucks = truck_weights[::-1]
    crossing_trucks = []
    out_time_list = []

    t = 0

    while waiting_trucks:
        t += 1
        print(t, out_time_list, crossing_trucks, waiting_trucks)
        if out_time_list[:1] == [t]:
            crossing_trucks.pop(0)
            out_time_list.pop(0)

        if sum(crossing_trucks) + waiting_trucks[-1] <= weight:
            crossing_trucks.append(waiting_trucks.pop())
            out_time_list.append(t + bridge_length)

    return out_time_list[-1]


if __name__ == '__main__':
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))