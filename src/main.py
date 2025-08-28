# 로그인 시스템 만들기
import json

userlist = {

    "admin" : {
        "password" : "admin",
        "role" : "admin",
        "birth" : "YYYYMMDD"
    },

    "editor" :{
        "password" : "editor",
        "role" : "editor",
        "birth" : "YYYYMMDD"
    }

}

print("------ 이미 계정이 있으신가요? -----")

status = input("Y/N")



if status == "N":
    
    print("------ 회원가입 ------")

    while True :
        newID = input("아이디를 입력해주세요")

        if newID in userlist:
            print("중복된 아이디입니다. 다시 입력해주세요")
            continue

        while True:
            newPW = input("패스워드를 입력해주세요")

            if len(newPW) < 6 :
                print("너무 짧습니다. 최소 6자 이상으로 입력해주세요")
                continue
            else :
                break

        while True:
            newBT = input("생년월일을 입력해주세요 (YYYYMMDD): ")

            # 1. 길이와 숫자인지 확인
            if len(newBT) != 8 or not newBT.isdigit():
                print("X 형식이 잘못되었습니다. 8자리 숫자로 입력해주세요.")
                continue

            # 2. 문자열 분리
            year = int(newBT[:4])
            month = int(newBT[4:6])
            day = int(newBT[6:])

            # 3. 범위 검사
            if year < 1920:
                print("X 연도는 1920년 이상이어야 합니다.")
            elif month < 1 or month > 12:
                print("X 월은 1에서 12 사이여야 합니다.")
            elif day < 1 or day > 31:
                print("X 일은 1에서 31 사이여야 합니다.")
            else:
                break  # 모든 조건 만족 시 탈출

        
        print("회원가입이 완료됐습니다 ^^")

        # 딕셔너리에 저장
        userlist[newID] = {
            "password" : newPW,
            "role" : "viewer",
            "birth" : newBT
        }
        break

elif status == "Y":

    print("----- 로그인 화면으로 이동중 ... ------")
    

print("------ 로그인 화면 -----")


# 로그인

while True:

    userID = input("아이디를 입력해주세요")

    if userID in userlist :
        userPW = input("비밀번호를 입력해주세요")
        if userPW in userlist[userID]["password"] :
            print("로그인 성공!")
            break
        else :
            print("비밀번호가 틀렸습니다")
            continue
    else:
        print("존재하지 않는 아이디 입니다.")
        continue


# 로그인 이후 화면

while True:

    print("\n==== 메뉴 ====")
    print("1. 내 정보 보기")
    print("2. 내 정보 수정")
    print("3. 회원 삭제 (관리자)")
    print("4. 모든 사용자 보기 (관리자, 편집자) ")
    print("5. 종료")

    number = input()

    if number == "1":
        print(f"아이디 : {userID}")
        print(f"\n비밀번호 : {userlist[userID]["password"]} ")
    
    elif number == "2":
        oldPW = input("기존 비밀번호를 입력해주세요")
        if oldPW == userlist[userID]["password"]:
            newnewPW = input("바꾸실 비밀번호를 입력해주세요")
            userlist[userID]["password"] = newnewPW
            print("비밀번호가 변경되었습니다!")

    elif number == "3":
        if userlist[userID]["role"]!= "admin" :
            print("관리자 권한이 없습니다")
            continue

        elif userlist[userID]["role"] == "admin" :
            removeID = input("삭제할 아이디 :")

            if removeID in userlist:
                del userlist[removeID]
                print(f"{removeID} 는 삭제되었습니다. ")
            
            else:
                print("해당 아이디는 존재하지 않습니다")
        
    elif number == "4":
        if userlist[userID]["role"] in ["admin" , "editor"]:
            print("------ 유저 목록 ------")
            print(json.dumps(userlist, indent=4, ensure_ascii=False))

        else :
            print("권한이 없습니다")
            continue

    elif number == "5":
        print("종료합니다.")
        break
    

        









#로그인기능
#

# viewer 는 자신의 정보만 수정
# editor 와 admin 은 모든 사용자의 정보 수정
# 탈퇴기능
# viewer, editor 는 자신의 계정만 삭제할 수 있고, admin 은 모든 사용자의 계정 삭제가능

# 정보가 업데이트될 시, 모든 사용자 목록을 구조적으로 다시 출력


