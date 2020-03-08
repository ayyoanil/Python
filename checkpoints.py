tc_count = int(input())

def  find_optimum_cost(cost_list, fuel_needed, start, end):
    cost = 0
    cheap_check_point = cost_list.index(min(cost_list[start:end]))

    cost += cost_list[cheap_check_point] *  sum(fuel_needed[cheap_check_point:end])

    if cheap_check_point == 0:
        return cost
    
    cost += find_optimum_cost(cost_list, fuel_needed, start, cheap_check_point)

    return cost


for tc in range(0, tc_count):
    cp_count = int(input())
    fuel_cost = [int(val) for val in input().split(' ')]
    fuel_needed = [int(val) for val in input().split(' ')]

    cost = find_optimum_cost (fuel_cost, fuel_needed, 0, cp_count)

    print(cost)

