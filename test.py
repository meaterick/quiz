import random
import time

# 문제 리스트와 정답들 (문제: 정답) 형태로 설정
quiz_data = [
    ("2 + 2는 무엇인가?", "4"),
    ("Python에서 'print' 함수는 무엇을 하는가?", "출력"),
    ("10의 2승은?", "100"),
    ("컴퓨터 네트워크에서 IP는 무엇의 약자인가?", "Internet Protocol"),
    ("HTML의 의미는?", "HyperText Markup Language"),
    ("파이썬에서 리스트를 정의하려면 어떻게 해야 하는가?", "[]"),
    ("웹사이트에서 URL의 의미는?", "Uniform Resource Locator"),
    ("다음 중 가장 빠른 정렬 알고리즘은?", "퀵정렬"),
    ("HTML에서 링크를 생성하는 태그는?", "<a>"),
    ("Python에서 문자열을 정의하려면 무엇을 사용해야 하는가?", "따옴표"),
]

# 유저 점수와 순위
user_scores = []

# 퀴즈 진행 함수
def start_quiz():
    print("퀴즈 맞추기 게임에 오신 것을 환영합니다!")
    input("시작하려면 Enter를 눌러주세요...")

    score = 0

    # 문제 출제
    for i, (question, answer) in enumerate(quiz_data, 1):
        print(f"\n문제 {i}: {question}")
        user_answer = input("정답을 입력하세요: ").strip()
        
        if user_answer == answer:
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다! 정답은 '{answer}' 입니다.")

    # 퀴즈 종료 후 결과 출력
    print(f"\n퀴즈가 종료되었습니다! 당신의 점수는 {score}/{len(quiz_data)} 입니다.")
    
    # 순위 기록에 점수 저장
    user_scores.append(score)
    user_scores.sort(reverse=True)  # 내림차순으로 점수 정렬

    # 순위 출력
    print("\n--- 순위 ---")
    for rank, score in enumerate(user_scores, 1):
        print(f"{rank}위: {score}점")

    # 다시 플레이하거나 종료
    end_game()

# 다시 플레이하거나 종료하는 함수
def end_game():
    print("\n게임이 끝났습니다!")
    choice = input("다시 플레이하려면 '다시', 게임을 종료하려면 '끝내기'를 입력하세요: ").strip().lower()

    if choice == '다시':
        start_quiz()
    elif choice == '끝내기':
        print("게임을 종료합니다. 감사합니다!")
    else:
        print("잘못된 입력입니다. 게임을 종료합니다.")

# 게임 시작
if __name__ == "__main__":
    start_quiz()