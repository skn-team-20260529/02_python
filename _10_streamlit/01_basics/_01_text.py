import streamlit as st

# 위와 같이 가져오면 이 파일은 이제 스트림릿으로 실행할 수 있는 파일이 됨

#실행 명령어
# streamlit run [파일명].py

#제목
st.title("Hello, Streamlit!🤩🤩")

st.header("Text")
st.subheader(":green[Hey], divider=rainbow, divider= Streamlit!")

# text : 단순 글자
st.text("text test: welcome to streamlit")

#write : 단순 글자뿐만 아니라 마크다운, 표, 리스트, 차트, 입력 타입 등에 따라 출력방식 정해짐
st.write("write test: welcome to streamlit")
st.write("`write` test: **welcome** to streamlit")
st.write("## write test: **welcome** to streamlit")
st.write("""
|구분|내용|
|---|---|
|1|1|
|2|2|
|3|3|
""")


st.markdown("### markdown test: **welcome** to streamlit")
st.html("<h1>html test: **welcome** to streamlit</h1>")


st.subheader(":red[magic]", divider="rainbow")

"streamlit magic"
"변수나 리터럴 값이 출력 구문 내에 없어도 화면에 값을 기록하는 기능"
100
lst = [10, 20, 30]
lst
dct = {"A": 10, "B": 20}
dct


# 코드블록
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python", line_numbers=True)

# latex: 수식
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# badge: 뱃지
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

#metric : 측량/측정
st.subheader(":blue[metric]", divider="rainbow")
a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)
c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)

from numpy.random import default_rng as rng

changes = list(rng(4).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)

row = st.container(horizontal=True)
with row:
    st.metric(
        "Line", 10, delta, chart_data=data, chart_type="line", border=True
    )
    st.metric(
        "Area", 10, delta, chart_data=data, chart_type="area", border=True
    )
    st.metric(
        "Bar", 10, delta, chart_data=data, chart_type="bar", border=True
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
