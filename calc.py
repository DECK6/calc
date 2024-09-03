import streamlit as st

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

st.title("간단한 계산기")

num1 = st.number_input("첫 번째 숫자를 입력하세요")
num2 = st.number_input("두 번째 숫자를 입력하세요")

operation = st.selectbox("연산을 선택하세요", ["+", "-", "*", "/"])

if st.button("계산"):
    result = calculate(num1, num2, operation)
    st.write(f"결과: {result}")