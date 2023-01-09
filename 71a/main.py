length = int(input())
for i in range(length):
    ans = input()
    if len(ans) > 10:
        ans = f"{ans[0]}{len(ans)-2}{ans[-1]}"
    print(ans)