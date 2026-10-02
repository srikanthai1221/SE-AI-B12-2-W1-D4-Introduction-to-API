"""
grade_app.py
Student Grade Manager - the Day 2 grade system, now in the browser with Streamlit.
"""

import streamlit as st


# ---- Same grading logic as Day 2 (unchanged) ----
def get_grade(mark):
    """Return the letter grade for a mark between 0 and 100 (inclusive)."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


st.title("Student Grade Manager")

# ---- Keep the list in session_state so it survives reruns ----
# Streamlit reruns this whole file on every click. A plain `students = []`
# would be reset to empty each time; session_state persists between reruns.
if "students" not in st.session_state:
    st.session_state.students = []

# ---- Form to add a student ----
with st.form("add", clear_on_submit=True):
    name = st.text_input("Name")
    # min_value / max_value make the widget itself reject marks outside 0-100
    mark = st.number_input("Mark", min_value=0, max_value=100, step=1, value=0)
    submitted = st.form_submit_button("Add")

if submitted:
    clean_name = name.strip()
    if not clean_name:
        st.error("Please enter a student name.")
    elif not (0 <= mark <= 100):  # extra safety check
        st.error("Mark must be between 0 and 100.")
    else:
        st.session_state.students.append(
            {"Name": clean_name, "Mark": int(mark), "Grade": get_grade(mark)}
        )
        st.success(f"Added {clean_name}: {int(mark)} -> {get_grade(mark)}")

# ---- Table and class figures ----
if st.session_state.students:
    students = st.session_state.students
    marks = [s["Mark"] for s in students]

    col_table, col_stats = st.columns([2, 1])

    with col_table:
        st.subheader("Results")
        st.table(students)

    with col_stats:
        st.subheader("Class figures")
        st.metric("Average", f"{sum(marks) / len(marks):.1f}")
        st.metric("Highest", max(marks))
        st.metric("Lowest", min(marks))

    if st.button("Clear all students"):
        st.session_state.students = []
        st.rerun()
else:
    st.info("No students yet. Add one using the form above.")