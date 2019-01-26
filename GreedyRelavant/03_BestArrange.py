"""
会议安排
 一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲．
 给你每一个项目开始的时间和结束的时间（给你一个数组，里面是一个个具体的项目）
 你来安排宣讲的日程，要求会议室进行的宣讲场次最多
 返回这个最多的宣讲场次
 策略：　结束时间早的先做　依据结束时间　会议放进小根堆里
"""
# 用数组排序的方式实现
class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def get_max_meeting_num(meetings, start):
    if not meetings:
        return 0
    # 先对meetings排序
    meetings.sort(key=lambda meeting: meeting.end, reverse=False)
    result = 0
    for i in range(len(meetings)):
        if meetings[i].start >= start:
            result += 1
            start = meetings[i].end

    return result


# 用堆排序的方式实现
import heapq
class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def get_max_meeting_num1(meetings, start):
    if not meetings:
        return 0
    # 向将meetings中所有元素入队
    meetingQ = []
    for i in range(len(meetings)):
        heapq.heappush(meetingQ, meetings[i])

    result = 0
    while meetingQ:
        topM = heapq.heappop(meetingQ)
        if topM.start >= start:
            result += 1
            start = topM.end
    return result


if __name__ == '__main__':
    mlist = [Meeting(3, 4), Meeting(5, 8), Meeting(1, 3), Meeting(2, 6), Meeting(2, 5)]
    print(get_max_meeting_num(mlist, 0))
    print(get_max_meeting_num1(mlist, 0))

