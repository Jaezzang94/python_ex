score = int(input("성적을 입력하세요"))
if score >= 90:
    print("A 입니다.")
    if score >=98:
        print("장학금 대상자입니다")
elif score >= 80:
    print("B 입니다.")
elif score >= 70:
    print("C 입니다.")
elif score >= 60:
    print("D 입니다.")
else :
    print("F 입니다.")