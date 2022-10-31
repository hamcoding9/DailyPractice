def solution(n, words):
    answer = [0, 0]
    players = [0] * n
    for i in range(len(words)):
        word = words[i]
        past_words = words[:i]
        now_player = i % n
        if len(past_words) == 0:
            players[now_player] += 1
            continue
        else:
            if past_words[-1][-1] != word[0] or word in past_words:
                answer[0] = now_player + 1
                answer[1] = players[now_player] + 1
                break
        players[now_player] += 1
    return answer