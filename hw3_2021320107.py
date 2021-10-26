# DO NOT ADD ANY 'import' STATEMENT!!!
# Remove 'pass' statement
# And add your code at the location of 'IMPLEMENT HERE!' comment
# You can define your own function to use
# But you can't modify the name and arguments of the functions
# And you can't add code that is not function definition in other space

# P01
def list2set(lst):
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    lst2.sort()
    return lst2

# P02
def reverse(s):
    reversed_s = s[::-1]
    return reversed_s

# P03
def partition_and_drop(lst, p, n):
    lst_True = []
    lst_False = []
    for i in lst:
        if p(i) == False:
            lst_False.append(i)
        else:
            lst_True.append(i)
    if len(lst_True) > n:
        lst_True = lst_True[0:n]
    if len(lst_False) > n:
        lst_False = lst_False[0:n]
    new_lst = [lst_True, lst_False]
    return tuple(new_lst)

# P04
def isRotate(s1, s2):
    lst = [0 for n in range(len(s1))]
    for i in range(len(s1)):
        lst[i] = s1[-1] + s1[:-1]
        s1 = lst[i]
    if s2 in lst:
        return True
    else:
        return False

# P05
def strange(string, repeat):
    result = ''
    for s in string:
        result += s * repeat
    return result

# P06
def ORank(scores):
    lst = []
    for i in range(len(scores)):
        tu = tuple(scores[i])
        lst.append(tu)
    lst = sorted(lst, key = lambda x : (-x[4], -x[1], -x[2], -x[3]))
    for i in range(len(scores)):
        lst[i] = lst[i][0]
    return lst

# P07
def clock_travel(lst, s, t):
    if s < t:
        dist_right = t - s
        dist_left = len(lst) - dist_right
    else:
        s, t = t, s
        dist_left = t - s
        dist_right = len(lst) - dist_left      
    if dist_right > dist_left:
        return -1
    elif dist_right == dist_left:
        return 0
    else:
        return 1


# P08
def double_zip(labels, values):
    lst = []
    if len(values) % 2:
        del values[-1]
    for i in range(len(labels)):
        tu = (labels[i], values[2*i:2*(i+1)])
        lst.append(tu)
    return lst

# P09
def evenly_dedup(lst):
    lst2 = []
    count = 1
    lst2.append(lst[0])
    lst2.append(lst[1])
    for i in range(2, len(lst)):
        if lst[i-2] == lst[i-1] and lst[i-1] != lst[i]:
            count += 1
        if count % 2:
            lst2.append(lst[i])
        else:
            if lst[i] not in lst2:
                lst2.append(lst[i])
    return lst2

# P10
def select_category(lst):
    cat_name_list = [
        "Aces", "Deuces", "Threes", "Fours", "Fives", "Sixes",
        "4 of a Kind", "Full House", "Small Straight", "Large Straight", "Yacht"
        ]
    
    sum_lst = [0 for n in range(6)]
    for j in range(6):
        for i in range(5):
            if lst[i] == j+1:
                sum_lst[j] += j+1
    
    sum_lst2 = [0 for n in range(5)]
    count_four_lst = [0 for n in range(6)]
    for i in range(6):
        count_four_lst[i] = lst.count(i+1)
    if 4 in count_four_lst or 5 in count_four_lst:
        for i in lst:
            sum_lst[0] += i

    count_fh_lst = [0 for n in range(6)]
    for i in range(6):
        count_fh_lst[i] = lst.count(i+1)
    if 2 in count_fh_lst and 3 in count_fh_lst:
        for i in lst:
            sum_lst2[1] += i
            
    ss_lst = []
    for i in lst:
        if i not in ss_lst:
            ss_lst.append(i)
    ss_lst.sort()
    if ss_lst in [[1,2,3,4], [2,3,4,5], [3,4,5,6]]:
        sum_lst2[2] = 15
    
    ls_str = sorted(lst)
    if ls_str in [[1,2,3,4,5], [2,3,4,5,6]]:
        sum_lst2[3] = 30
    
    count_ya_lst = [0 for n in range(6)]
    for i in range(6):
        count_ya_lst[i] = lst.count(i+1)
    if 5 in count_ya_lst:
        sum_lst2[4] = 50

    all_score_list = sum_lst + sum_lst2
    
    tmp = max(all_score_list)
    ind = all_score_list.index(tmp)
    tu = tuple([cat_name_list[ind], all_score_list[ind]])
    return tu

#########################################################################
# From this line, the code below is to test your answer functions
# So NEVER MODIFY IT
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def main():
    problems = ("list2set", "reverse", "partition_and_drop", "isRotate", "strange", "ORank", "clock_travel", "double_zip", "evenly_dedup", "select_category")
    testcases = {
        "list2set": (
            list2set,
            [[1, 2, 3, 4, 5], [1, 6, 3, 3, 1, 2, 0], [-2, 5, -5, 2, -2, 5]],
            [[1, 2, 3, 4, 5], [0, 1, 2, 3, 6], [-5, -2, 2, 5]]
        ),
        "reverse": (
            reverse,
            ["hello", "Bye"],
            ["olleh", "eyB"]
        ),
        "partition_and_drop": (
            partition_and_drop,
            [
             (list(range(100)), lambda x: x%2, 15),
             (list(range(100)), lambda x: x%3, 10),
             (list(range(100)), isPrime, 10),
             (list(range(10)), isPrime, 100),
             (list(range(50, 100)), isPrime, 5)
            ],
            [
             ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]),
             ([1, 2, 4, 5, 7, 8, 10, 11, 13, 14], [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]),
             ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]),
             ([2, 3, 5, 7], [0, 1, 4, 6, 8, 9]),
             ([53, 59, 61, 67, 71], [50, 51, 52, 54, 55])
            ]
        ),
        "isRotate": (
            isRotate,
            [("Hello", "loHel"), ("Korea University", "iversityKorea Un"), ("Hello", "loleH"), ("Korea Univ", "a UnivKore"), ("Hello", "loByeHel")],
            [True, True, False, True, False]
        ),
        "strange": (
            strange,
            [("everybodystaysafe", 3), ("washyourhandseverytime", 2), ("howwasyourholiday", 1), ("wehadaveryniceholiday", 2), ("hopeyoudidtoo", 5)],
            ["eeevvveeerrryyybbbooodddyyyssstttaaayyysssaaafffeee", "wwaasshhyyoouurrhhaannddsseevveerryyttiimmee", "howwasyourholiday", "wweehhaaddaavveerryynniicceehhoolliiddaayy", "hhhhhooooopppppeeeeeyyyyyooooouuuuudddddiiiiidddddtttttoooooooooo"]
        ),
        "ORank": (
            ORank,
            [
             [["Hakjoo", 100, 70, 50, 90], ["Jeongsoo", 100, 30, 100, 90], ["Jaeho", 80, 50, 20, 100]],
             [["A", 12, 30, 48, 63], ["B", 30, 63, 48, 12], ["C", 50, 48, 70, 90]],
             [["A", 1, 2, 3, 4], ["B", 4, 3, 2, 1], ["C", 2, 3, 1, 4], ["D", 4, 1, 2, 3]]
            ],
            [
             ["Jaeho", "Hakjoo", "Jeongsoo"],
             ["C", "A", "B"],
             ["C", "A", "D", "B"]
            ]
        ),
        "clock_travel": (
            clock_travel,
            [(list(range(12)), 1, 7), (list(range(12)), 1, 3), (list(range(13)), 1, 7), (list(range(12)), 1, 9), (list(range(16)), 1, 9)],
            [0, 1, 1, -1, 0]
        ),
        "double_zip": (
            double_zip,
            [([1, 2], ['a', 'b', 'c', 'd']), ([1, 2, 3], ['a', 'b']), (['c'], ['plus', 'plus']), (['hi', 'yee'], ['ho', 'ho', 'yo', 'yo', 'howaboutme?']), ([1, 2, 3], [4, 5, 6, 7, 8, 9, 10])],
            [[(1, ['a', 'b']), (2, ['c', 'd'])], [(1, ['a', 'b']), (2, []), (3, [])], [('c', ['plus', 'plus'])], [('hi', ['ho', 'ho']), ('yee', ['yo', 'yo'])], [(1, [4, 5]), (2, [6, 7]), (3, [8, 9])]]
        ),
        "evenly_dedup": (
            evenly_dedup,
            [[1, 1, 2, 3, 3, 4], [1, 1, 2, 2, 3, 3, 4, 4], [1, 2, 3, 4, 5], [1, 2, 2, 3, 4, 5], [1, 2, 3, 3, 4, 4, 5, 5]],
            [[1, 1, 2, 3, 4], [1, 1, 2, 3, 3, 4], [1, 2, 3, 4, 5], [1, 2, 2, 3, 4, 5], [1, 2, 3, 3, 4, 5, 5]]
        ),
        "select_category": (
            select_category,
            [[1, 4, 5, 5, 5], [3, 3, 4, 4, 4], [1, 1, 1, 1, 1], [1, 2, 3, 4, 5], [5, 5, 5, 1, 4]],
            [("Fives", 15), ("Full House", 18), ("Yacht", 50), ("Large Straight", 30), ("Fives", 15)]
        )
    }
    for fn in problems:
        correct = True
        testfunc, inputs, outputs = testcases[fn]
        for i in range(len(inputs)):
            result = testfunc(*(inputs[i])) if isinstance(inputs[i], tuple) else testfunc(inputs[i])
            if result != outputs[i]:
                print(fn + ": Incorrect output for " + str(i+1)+"-th input")
                correct = False
        if correct:
            print(fn + ": Correct for all inputs")

main()
