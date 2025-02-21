import streamlit as st

# Dictionary of study resources based on common goals
study_resources = {
    "python": [
        "[Python Crash Course - Book](https://nostarch.com/pythoncrashcourse)",
        "[Automate the Boring Stuff with Python - Free Book](https://automatetheboringstuff.com/)",
        "[CS50’s Introduction to Programming with Python - Harvard](https://cs50.harvard.edu/python/)"
    ],
    "data science": [
        "[Kaggle Courses - Free](https://www.kaggle.com/learn)",
        "[IBM Data Science Professional Certificate - Coursera](https://www.coursera.org/professional-certificates/ibm-data-science)",
        "[Hands-On Machine Learning with Scikit-Learn - Book](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/)"
    ],
    "calculus": [
        "[Paul’s Online Math Notes - Free](http://tutorial.math.lamar.edu/)",
        "[MIT OpenCourseWare - Single Variable Calculus](https://ocw.mit.edu/courses/mathematics/18-01-single-variable-calculus-fall-2006/)",
        "[3Blue1Brown Calculus Series - YouTube](https://www.youtube.com/playlist?list=PLZHQObOWTQDOjZROHuBgtVZJwxKDB5urQ)"
    ],
    "ai": [
        "[Deep Learning Specialization - Coursera](https://www.coursera.org/specializations/deep-learning)",
        "[Fast.ai Practical Deep Learning - Free](https://course.fast.ai/)",
        "[Deep Learning with Python - Book](https://www.manning.com/books/deep-learning-with-python)"
    ]
}

def generate_study_plan(goals, strengths, weaknesses):
    """Generates a study plan with relevant resource suggestions."""
    
    if not goals.strip():
        return "❌ Please enter your goals to generate a study plan."

    study_plan = "### 📖 Personalized Study Plan\n\n"
    study_plan += f"🎯 **Goals:** {goals}\n\n"
    study_plan += f"✅ **Strengths:** {strengths if strengths.strip() else 'Not provided'}\n\n"
    study_plan += f"⚠ **Weaknesses:** {weaknesses if weaknesses.strip() else 'Not provided'}\n\n"

    study_plan += "#### 📌 Recommended Steps:\n"
    study_plan += "- 🔹 Break your goals into smaller, achievable milestones.\n"
    study_plan += "- 🔹 Leverage your strengths to stay motivated.\n"
    study_plan += "- 🔹 Address weaknesses with targeted practice and strategies.\n"
    study_plan += "- 🔹 Set a study schedule with dedicated time for each task.\n"
    study_plan += "- 🔹 Track progress and adjust the plan as needed.\n\n"

    # Find relevant study resources based on goals
    resources = []
    goal_words = goals.lower().split()  # Split input into individual words for better matching

    for key, links in study_resources.items():
        if any(word in key for word in goal_words):  # Check if any word in goal matches resources
            resources.extend(links)

    if resources:
        study_plan += "#### 📚 Suggested Resources:\n"
        for resource in resources:
            study_plan += f"- {resource}\n"
    else:
        study_plan += "🔍 No specific resources found for your goals. Try using broader keywords!\n"

    return study_plan

# Streamlit UI
st.set_page_config(page_title="📚 Smart Study Planner", page_icon="📖", layout="centered")
st.title("📚 Smart Study Planner")

goals = st.text_area("🎯 Enter Your Goals (e.g., Master Python, Learn AI, Ace Calculus):")
strengths = st.text_area("✅ List Your Strengths (e.g., Problem-solving, Time management):")
weaknesses = st.text_area("⚠ Mention Your Weaknesses (e.g., Math anxiety, Procrastination):")

if st.button("Generate Study Plan"):
    study_plan = generate_study_plan(goals, strengths, weaknesses)
    st.markdown(study_plan)
