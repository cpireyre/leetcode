def alertNames(names, times):
    def hhmmToMm(time):
        return 60 * int(time[0:2]) + int(time[3:5])

    beeps = dict()
    for name, time in zip(names, map(hhmmToMm, times)):
        if name not in beeps:
            beeps[name] = [time]
        else:
            beeps[name].append(time)
    for times in beeps.values():
        times.sort()
    res = []
    for name, times in beeps.items():
        if any(True for i in range(len(times) - 2) if times[i] + 60 >= times[i + 2]):
            res.append(name)
    res.sort()
    return res
# Runtime: 825 ms, faster than 74.39% of Python3 online submissions for Alert Using Same Key-Card Three or More Times in a One Hour Period.
# Memory Usage: 37.5 MB, less than 96.64% of Python3 online submissions for Alert Using Same Key-Card Three or More Times in a One Hour Period.


keyName = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"]
keyTime = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]
print(alertNames(keyName, keyTime))
keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
print(alertNames(keyName, keyTime))
