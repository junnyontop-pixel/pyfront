# app.py
import pyfront as pf

def my_awesome_ui():
    # 프론트엔드 컴포넌트 짜듯이 파이썬 코드로 구조를 선언합니다.
    return pf.v_stack(
        pf.h1("PyFront 컴포넌트 엔진 가동!", text_color="indigo-600", class_name="text-3xl font-extrabold text-center"),
        pf.p("자바스크립트나 HTML을 전혀 쓰지 않고 오직 파이썬으로만 만든 화면입니다.", text_color="gray-600"),
        
        pf.h_stack(
            pf.button("확인", bg="indigo", text_color="white", p=3, rounded=True, class_name="font-semibold shadow-md hover:bg-indigo-600 transition-all"),
            pf.button("취소", bg="gray", text_color="white", p=3, rounded=True, class_name="font-semibold shadow-md hover:bg-gray-600 transition-all")
        ),
        
        # 카드 뉴스 스타일의 UI 컴포넌트 예시
        pf.div(
            pf.p("💡 다음 단계 예고", class_name="font-bold text-sm text-green-600 mb-1"),
            pf.p("여기에 상태(State) 시스템을 연결하면 버튼을 누를 때 화면이 실시간으로 바뀌게 됩니다.", text_color="gray-700"),
            bg="white", p=5, rounded="xl", class_name="border border-gray-200 shadow-sm"
        ),
        class_name="max-w-md w-full p-8 bg-white rounded-2xl shadow-xl border border-gray-100"
    )

# 컴파일 시작!
if __name__ == "__main__":
    app = my_awesome_ui()
    pf.build(app)