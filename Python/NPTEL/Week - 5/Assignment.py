import sys

result = {}

ipList = sys.stdin.readlines()
if "\n" in ipList:
    ipList.remove("\n")
for ip in ipList:
    ip.replace('\n', '')
    name1 = ip.split(':')[0]
    name2 = ip.split(':')[1]

    if name1 not in result:
        result[name1] = {"b5": 0, "b3": 0, "sw": 0, "gw": 0, "sl": 0, "gl": 0}
    if name2 not in result:
        result[name2] = {"b5": 0, "b3": 0, "sw": 0, "gw": 0, "sl": 0, "gl": 0}
    setlist = ip.split(':')[2].split(',')
    cnt_p1 = 0
    cnt_p2 = 0
    for set in setlist:
        p1 = int(set.split('-')[0])
        p2 = int(set.split('-')[1])
        result[name1]["gw"] += p1
        result[name1]["gl"] += p2  # win count of one player is loss count of other player
        result[name2]["gw"] += p2
        result[name2]["gl"] += p1
        if p1 < p2:
            result[name2]["sw"] += 1
            result[name1]["sl"] += 1
            cnt_p2 += 1
        else:
            result[name1]["sw"] += 1
            result[name2]["sl"] += 1
            cnt_p1 += 1

    if cnt_p1 < cnt_p2:
        if len(setlist) <= 3:
            result[name2]["b3"] += 1
        else:
            result[name2]["b5"] += 1
    else:
        if len(setlist) <= 3:
            result[name1]["b3"] += 1
        else:
            result[name1]["b5"] += 1


for key in sorted(result, key=lambda x: (result[x]["b5"], result[x]["b3"], result[x]["sw"], result[x]["gw"]
                                         , result[x]["sl"], result[x]["gl"])
                        , reverse=True):
    print(key, result[key]["b5"], result[key]["b3"], result[key]["sw"], result[key]["gw"], result[key]["sl"]
          , result[key]["gl"])


