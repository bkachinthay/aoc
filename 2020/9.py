from common import numbers 

def A(nums, pre):
    checklist = nums[:pre]
    for n in nums[pre:]:
        is_valid = False
        for cn in checklist:
            if (n-cn) != cn and (n-cn) in checklist:
                is_valid = True
                break
        # print('n : ', n, is_valid)
        if not is_valid:
            return n
        checklist.pop(0)
        checklist.append(n)

def B(nums, pre):
    inv_num = A(nums, pre)
    sum_list = []
    for n in nums:
        new_sum_list = []
        for s, contigous_set in sum_list:
            if s+n == inv_num:
                new_cont_set = contigous_set +  [n]
                return min(new_cont_set) + max(new_cont_set)
            elif s+n < inv_num:
                new_sum_list.append([s+n, contigous_set + [n]])
        new_sum_list.append([n, [n]])
        sum_list = new_sum_list

s1 = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".strip().split('\n')

assert A(list(map(int, s1)), 5) == 127
assert B(list(map(int, s1)), 5) == 62

if __name__ == '__main__':
    print(A(list(numbers('9.txt')), 25))
    print(B(list(numbers('9.txt')), 25))
