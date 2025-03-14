import streamlit as st
import pandas as pd

def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"

st.set_page_config(page_title="Student Report Card", page_icon="📄", layout="centered")

st.markdown(
    """
    <style>
    /* Light Mode */
    .stApp {
        background-color: #ADE8F4; 
        color: #333333;
    }
    header[data-testid="stHeader"] {  
        background-color: #ADE8F4; 
    }
    h1, h2, h3 {
        color: #004085; 
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        border: 2px solid #0077B6; 
        border-radius: 5px;
        padding: 8px;
    }
    .stButton>button {
        background-color: #0077B6; 
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #0077B6; 
    }
    @media (prefers-color-scheme: dark) {
        .stApp {
            background-color: #0A203F; 
            color: #FFFFFF; 
        }
        header[data-testid="stHeader"] {
            background-color: #0A203F; 
        }
        h1, h2, h3 {
            color: #073B4C; 
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input {
            border: 2px solid #073B4C;
            border-radius: 5px;
            padding: 8px;
            background-color: #041F24; 
            color: white;
        }
        .stButton>button {
            background-color: #041F24; 
            color: white;
        }
        .stButton>button:hover {
            background-color: #041F24; 
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("📄 Student Report Card Generator ✨")
st.text("📚 Success isn’t just about grades, it’s about effort and improvement! 🚀")

students = []

if "students_data" not in st.session_state:
    st.session_state.students_data = []

with st.form("student_form"):
    st.subheader("📌 Enter Student Details")
    name = st.text_input("Student Name")
    roll_no = st.text_input("Roll Number")
    try:
        math = int(st.number_input("Math Marks📐", min_value=0, max_value=100))
        physics = int(st.number_input("Physics Marks⚛️", min_value=0, max_value=100))
        urdu = int(st.number_input("Urdu Marks📝", min_value=0, max_value=100))
        english = int(st.number_input("English Marks📖", min_value=0, max_value=100))
        computer = int(st.number_input("Computer Marks💻", min_value=0, max_value=100))
    except ValueError:
        st.error("Please enter valid numeric values for marks.")
    
    submitted = st.form_submit_button("Add Student")
    
    if submitted and name and roll_no:
        total_marks = math + physics + urdu + english + computer
        percentage = (total_marks / 500) * 100
        grade = calculate_grade(percentage)
        
        student_data = {
            "Name": name,
            "Roll No": roll_no,
            "Math": math,
            "Physics": physics,
            "Urdu": urdu,
            "English": english,
            "Computer": computer,
            "Total": total_marks,
            "Percentage": f"{percentage:.2f}%",
            "Grade": grade
        }
        
        st.session_state.students_data.append(student_data)
        st.success(f"Record of {name} inserted successfully!🎉")

if st.session_state.students_data:
    st.subheader("📋 Students Report Cards")
    df = pd.DataFrame(st.session_state.students_data)

    def highlight_grades(val):
        if val == "A+" or val == "A":
            return 'background-color: #28a745; color: white;' 
        elif val == "B":
            return 'background-color: #ffc107; color: black;' 
        elif val == "C":
            return 'background-color: #ffb84d; color: black;' 
        elif val == "F" or val == "Fail":
            return 'background-color: #dc3545; color: white;'  
        return ""

    styled_df = df.style.applymap(highlight_grades, subset=["Grade"])
    st.dataframe(styled_df, use_container_width=True)
