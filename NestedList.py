if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}

    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        avg = float(float(sum(scores) / float(len(scores))))
        avg2dec = format(avg, '.2f')
        student_marks[name] = avg2dec
    query_name = raw_input()
    if query_name in student_marks:
        print student_marks[query_name]
