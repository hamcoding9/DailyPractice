from math import ceil

def add_out(records):
    visit = {}
    for record in records:
        r = record.split(" ")
        if r[2] == "IN":
            visit[r[1]] = visit.get(r[1], 0) + 1
        elif r[2] == "OUT":
            visit[r[1]] -= 1
    for v in visit:
        if visit[v] == 1:
            record = "23:59 " + str(v) + " OUT"
            records.append(record)
    return records

def calculate_time(in_time, out_time):
    in_time = int(in_time.split(":")[1]) + int(in_time.split(":")[0]) * 60
    out_time = int(out_time.split(":")[1]) + int(out_time.split(":")[0]) * 60
    return out_time - in_time
         
def solution(fees, records):
    records = add_out(records)
    answer = []
    in_dict, out_dict = {}, {}
    for record in records:
        r = record.split(" ")
        if r[2] == "IN":
            in_dict[r[1]] = in_dict.get(r[1], []) + [r[0]]
        elif r[2] == "OUT":
            out_dict[r[1]] = out_dict.get(r[1], []) + [r[0]]
    for car in sorted(in_dict):
        time = 0
        for (i, o) in zip(in_dict[car], out_dict[car]):
            time += calculate_time(i, o)
        if time > fees[0]:
            fee = fees[1] + fees[3] * ceil((time - fees[0])/fees[2])
        else:
            fee = fees[1]
        answer.append(fee)
    return answer