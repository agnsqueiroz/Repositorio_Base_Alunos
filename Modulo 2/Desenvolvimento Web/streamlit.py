import streamlit as st

st.title("Operações básicas")

def is_int(n):
    try:
        int(n)
        return True
    except:
        return False

def operacao(nome, func, key1, key2, btn_key):
    st.write(f"### {nome}")
    num1 = st.text_input("Num 1", key=key1)
    num2 = st.text_input("Num 2", key=key2)
    if st.button(nome, key=btn_key):
        if is_int(num1) and is_int(num2):
            n1 = int(num1)
            n2 = int(num2)
            if nome == "Dividir" and n2 == 0:
                st.write("Não pode dividir por zero")
            else:
                st.write("Resultado:", func(n1, n2))
        else:
            st.write("Digite números inteiros")

col1, col2, col3, col4 = st.columns(4)

with col1:
    operacao("Somar", lambda num1, num2: num1 + num2, "s1", "s2", "btn1")
with col2:
    operacao("Dividir", lambda num1, num2: num1 / num2, "d1", "d2", "btn2")
with col3:
    operacao("Subtrair", lambda num1, num2: num1 - num2, "sub1", "sub2", "btn3")
with col4:
    operacao("Multiplicar", lambda num1, num2: num1 * num2, "m1", "m2", "btn4")
