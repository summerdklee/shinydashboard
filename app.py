from shiny.express import input, render, ui

ui.input_slider("num", "원을 움직여 숫자를 선택하세요.", 0, 100, 20) # num은 변수


@render.code
def txt():
    return f"숫자*2는 {input.num() * 2}입니다."