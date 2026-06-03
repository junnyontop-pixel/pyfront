import os

class Element:
    """HTML 엘리먼트를 표현하는 파이썬 기본 클래스"""
    def __init__(self, tag, *args, **kwargs):
        self.tag = tag
        # 문자열이나 다른 Element 객체들을 자식(Children)으로 받음
        self.children = args 
        # HTML 속성 및 스타일 속성을 받음
        self.attributes = kwargs

    def render(self) -> str:
        """파이썬 객체를 실제 HTML 문자열로 변환하는 핵심 컴파일 함수"""
        attrs = []
        classes = []

        # 파이썬의 키워드 인자(kwargs)를 HTML 속성 및 Tailwind 클래스로 변환
        for key, value in self.attributes.items():
            if key == "bg": # 배경색 단축 속성
                classes.append(f"bg-{value}-500")
            elif key == "text_color": # 글자색 단축 속성
                classes.append(f"text-{value}")
            elif key == "p": # 패딩
                classes.append(f"p-{value}")
            elif key == "rounded": # 라운드 값
                if isinstance(value, bool) and value:
                    classes.append("rounded-lg")
                else:
                    classes.append(f"rounded-{value}")
            elif key == "class_name": # 직접 Tailwind 클래스를 넣고 싶을 때
                classes.append(value)
            else:
                # 일반 HTML 속성 (예: id, href 등) 처리
                attrs.append(f'{key}="{value}"')

        # 모아진 Tailwind 클래스들을 하나로 합침
        if classes:
            attrs.append(f'class="{" ".join(classes)}"')

        attr_str = f" {' '.join(attrs)}" if attrs else ""

        # 자식 노드들을 재귀적으로 렌더링
        children_str = ""
        for child in self.children:
            if isinstance(child, Element):
                children_str += child.render() # 자식이 Element면 또 render() 호출
            else:
                children_str += str(child) # 자식이 문자열이면 그대로 추가

        return f"<{self.tag}{attr_str}>{children_str}</{self.tag}>"

# 레이아웃을 위한 특수 컴포넌트 (Flexbox 래핑)
def v_stack(*args, **kwargs):
    kwargs["class_name"] = f"flex flex-col gap-4 {kwargs.get('class_name', '')}".strip()
    return Element("div", *args, **kwargs)

def h_stack(*args, **kwargs):
    kwargs["class_name"] = f"flex flex-row gap-4 items-center {kwargs.get('class_name', '')}".strip()
    return Element("div", *args, **kwargs)


# 🚀 빌드 및 실행 엔진
def build(root_component, filename="index.html"):
    """작성된 파이썬 UI를 HTML 파일로 내뱉는 함수"""
    html_content = root_component.render()
    
    # Tailwind CSS가 기본 탑재된 HTML 템플릿
    full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PyFront 앱</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen flex items-center justify-center">
    <div id="root">
        {html_content}
    </div>
</body>
</html>"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"🎉 성공적으로 화면을 깎았습니다! '{filename}' 파일을 확인하세요.")

def __getattr__(name: str):
    """
    개발자가 pyfront.something()을 호출했는데 그런 함수가 없으면 
    파이썬이 이 함수를 찾아와서 'name'에 'something'을 넣어 실행합니다.
    """
    # 내장 함수나 특수 속성(__)은 통과시킵니다.
    if name.startswith("__"):
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
        
    # 개발자가 부른 이름 그대로 HTML 엘리먼트를 만드는 함수를 즉석에서 반환합니다!
    return lambda *args, **kwargs: Element(name, *args, **kwargs)