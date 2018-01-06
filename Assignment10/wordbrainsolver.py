""" ec602 """
# Copyright 2017 Jiali Ge ivydany@bu.edu
# Copyright 2017 Siyuan Tang sytang7@bu.edu
# Copyright 2017 Pei Jia leojia@bu.edu

from sys import argv


def word_dic(k, word, wdic):
    """ dic for small/big_w """
    if k == len(word) - 1:
        wdic.setdefault(word[k], {})['end'] = True
    else:
        word_dic(k + 1, word, wdic.setdefault(word[k], {}))


def neighbor(num, grid):
    """ find neighbors """
    all_neighbor = [[] for letter in grid]
    for i in range(num ** 2):
        irow = i // num
        icol = i % num
        if icol < num - 1:
            all_neighbor[i].append(i + 1)
            if irow > 0:
                all_neighbor[i].append(i - num + 1)
            if irow < num - 1:
                all_neighbor[i].append(i + num + 1)
        if icol > 0:
            all_neighbor[i].append(i - 1)
            if irow > 0:
                all_neighbor[i].append(i - num - 1)
            if irow < num - 1:
                all_neighbor[i].append(i + num - 1)
        if irow > 0:
            all_neighbor[i].append(i - num)
        if irow < num - 1:
            all_neighbor[i].append(i + num)
    return all_neighbor


def grid_drop(grid, num, ncor):
    """ update grid """
    l_grid = list(grid)
    for i in sorted(ncor):
        irow = ord(i) // num
        icol = ord(i) % num
        if irow != 0:
            while irow != 0:
                l_grid[irow * num + icol] = l_grid[(irow - 1) * num + icol]
                l_grid[(irow - 1) * num + icol] = " "
                irow -= 1
        else:
            l_grid[icol] = " "
    return ''.join(l_grid)


def find_word(i, grid, n_word, dic, result,
              fword, all_length, all_neighbor, unvisit, str_l):
    """ word by word """
    num_word = len(fword)
    if grid[i] in dic:
        unvisit[i] = False
        if str_l[n_word][num_word].isalpha() is True:
            if grid[i] == str_l[n_word][num_word]:
                fword += chr(i)
        else:
            fword += chr(i)
        if len(fword) == all_length[n_word]:
            if 'end' in dic[grid[i]]:
                result.append(fword)
            return result
        for letter1 in all_neighbor[i]:
            if unvisit[letter1]:
                find_word(letter1, grid, n_word, dic[grid[i]], result,
                          fword, all_length, all_neighbor, unvisit, str_l)
                unvisit[letter1] = True


def find_solution(grid1, n_word, dic, tem, solution,
                  all_length, all_neighbor, num, str_l):
    """ find solution """
    num_grid = len(grid1)
    for start in range(num_grid):
        if grid1[start] == " ":
            continue
        if str_l[n_word][0].isalpha() is True:
            if grid1[start] != str_l[n_word][0]:
                continue
        result = []
        unvisited = [True] * len(grid1)
        find_word(start, grid1, n_word, dic, result, '',
                  all_length, all_neighbor, unvisited, str_l)
        for words in result:
            word_tem = ''
            temp = tem
            for k in words:
                word_tem = word_tem + grid1[ord(k)]
            temp = temp + ' ' + word_tem
            if n_word == len(all_length) - 1:
                solution.append(temp)
            else:
                grid = grid1[:]
                grid = grid_drop(grid, num, words)
                find_solution(grid, n_word + 1, dic, temp, solution,
                              all_length, all_neighbor, num, str_l)
    return solution


def main():
    """ main """
    with open(argv[1]) as small_file:
        s_words = small_file.read().split()
    small_dic = {}
    for words1 in s_words:
        word_dic(0, words1, small_dic)

    with open(argv[2]) as big_file:
        b_words = big_file.read().split()
    b_dic = {}
    for words2 in b_words:
        word_dic(0, words2, b_dic)

    count = 0
    word_list = []
    try:
        while True:
            line2 = input().split('\n')
            if line2 is '':
                break
            word_list.append(''.join(line2))
            if '*' in line2[0]:
                while count < len(word_list):
                    str1 = []
                    all_length = []
                    num2 = len(word_list[count])
                    for ber in range(num2):
                        str1.append(word_list[count + ber])
                    str2 = ''.join(str1)
                    str_l = word_list[count + num2].split()
                    num_strl = len(str_l)
                    for ber1 in range(num_strl):
                        all_length.append(len(str_l[ber1]))

                    all_neighbor = neighbor(num2, str2)
                    solution = []
                    find_solution(str2, 0, small_dic, '', solution,
                                  all_length, all_neighbor, num2, str_l)
                    if len(solution) == 0:
                        find_solution(str2, 0, b_dic, '', solution,
                                      all_length, all_neighbor, num2, str_l)

                    num_sol = len(solution)
                    for k in range(num_sol):
                        solution[k] = solution[k][1:len(solution[k])]
                    solution = list(set(solution))
                    solution.sort()

                    if solution:
                        print('\n'.join(e for e in solution))
                    print('.')

                    count += (num2 + 1)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
