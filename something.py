import re
def solve_regex(captcha, n):
    return sum(int(c) for c in re.findall(fr'(\d)(?=.{{{n-1}}}\1)', captcha+captcha[:n]))


captcha = open('input.txt').read().strip()
print(solve_regex(captcha, 1))
print(solve_regex(captcha, len(captcha) // 2))