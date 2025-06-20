#천리길도 한 걸음 부터 문제 난이도 정렬, 난이도 같으면 완료한 사람 많은 순으로, 그것도 같으면 이름 순으로
def solution(problem_names, levels, completions):

    sorted_levels = sorted(zip(levels, completions, problem_names))
    if sorted_levels[0][0] == sorted_levels[1][0]:
        sorted_levels = sorted(zip(sorted_levels, completions))
        if sorted_levels[0][0][1] == sorted_levels[1][0][1]:
            sorted_levels = sorted(zip(sorted_levels, problem_names))

    answer = [sorted_levels]
    return answer