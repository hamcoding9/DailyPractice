def solution(lottos, win_nums):
    wrong = [i for i in lottos if i not in win_nums]
    ranking = [1, 2, 3, 4, 5, 6, 6]
    return [ranking[len(wrong)-wrong.count(0)],ranking[len(wrong)]]