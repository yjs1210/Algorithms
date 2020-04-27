# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    curr_dist = 0 
    total_stops = 0
    curr_stop_idx = 0 

    while True:
        stop_to_make = 0 

        if (d - curr_dist) <= m:
            return total_stops
        
        for i in range(curr_stop_idx, len(stops)):
            if (stops[i] - curr_dist <= m):
                if (i == len(stops)-1):
                    if (d - stops[i] <=m):
                        return total_stops + 1
                    else:
                        return -1
                stop_to_make = stops[i]
            else:
                if stop_to_make == 0:
                    return -1
                else:
                    total_stops += 1
                    curr_stop_idx = i
                    curr_dist = stops[i-1]
                    break 
                
if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
