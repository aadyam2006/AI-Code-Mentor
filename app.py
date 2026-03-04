from code_chat import answer_question
import streamlit as st
from ai_analyzer import analyze_code
from flowchart import generate_flowchart

st.set_page_config(page_title="AI Code Mentor", page_icon="🤖")

st.title("🤖 AI Code Mentor")

st.write("Analyze code, detect bugs, estimate complexity, and visualize flowcharts.")

code = st.text_area(
    "Paste your code here",
    height=200
)

if st.button("Analyze Code"):

    if code.strip() == "":
        st.warning("Please paste some code first.")

    else:

        st.subheader("Your Code")
        st.code(code)

        result = analyze_code(code)

        st.subheader("AI Analysis")

        st.write("### Detected Language")
        st.success(result["language"])

        st.write("### Code Explanation")
        st.write(result["explanation"])

        st.write("### Possible Bugs")
        st.write(result["bugs"])

        st.write("### Estimated Time Complexity")
        st.write(result["complexity"])

        # show suggested fix
        if result["fix"]:
            st.subheader("Suggested Fix")
            st.code(result["fix"])

        st.subheader("Flowchart")
        st.subheader("Ask About Your Code")

question = st.text_input("Ask a question about the code")

if st.button("Ask AI Assistant"):

    if question.strip() == "":
        st.warning("Please ask a question.")
    else:

        answer = answer_question(code, question)

        st.write("### Assistant Answer")
        st.success(answer)

        chart = generate_flowchart(code)

        st.graphviz_chart(chart)