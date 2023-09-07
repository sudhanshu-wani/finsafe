import streamlit as st
import random
import time

# Financial advice for different age groups
age_advice = {
    "below 35": [
        "Consider investing in high-growth stocks for potential high returns.",
        "Explore opportunities in emerging technologies.",
        "Start building an emergency fund for unexpected expenses.",
        "Focus on skill development to boost earning potential.",
        "Consider investing in a diverse portfolio to spread risk."
    ],
    "35 to 50": [
        "Diversify your investments to balance risk and return.",
        "Invest in a mix of growth and income assets for steady returns.",
        "Consider exploring real estate investments.",
        "Prioritize retirement savings and explore tax-saving options.",
        "Continue building your emergency fund for financial security."
    ],
    "50 and above": [
        "Review and adjust your investment portfolio to manage risk.",
        "Consider transitioning to safer investments with steady returns.",
        "Focus on preserving capital and securing retirement income.",
        "Explore long-term care insurance options for healthcare needs.",
        "Consult with a financial advisor for retirement planning."
    ]
}

# Financial advice based on income
income_advice = {
    "below 10000": [
        "Build a budget to manage expenses effectively.",
        "Start saving consistently to build an emergency fund.",
        "Explore low-cost investment options for better returns."
    ],
    "10000 to 15000": [
        "Continue building your emergency fund for financial security.",
        "Explore investment options like mutual funds or ETFs.",
        "Consider diversifying your investments to spread risk."
    ],
    "15000 to 25000": [
        "Consider increasing your investment contributions for long-term growth.",
        "Explore index funds for low-cost, diversified exposure to the market.",
        "Focus on creating a well-structured financial plan."
    ],
    "25000 to 40000": [
        "Diversify your investments across asset classes to manage risk.",
        "Consider tax-efficient investment strategies.",
        "Explore options for retirement planning and saving.",
        "Invest in skill development for potential income growth."
    ],
    "40000 to 60000": [
        "Continue investing in a balanced portfolio for steady returns.",
        "Explore opportunities for higher education or certifications.",
        "Consider additional sources of income to boost savings.",
        "Review and optimize your investment strategy periodically."
    ],
    "60000 to 80000": [
        "Explore opportunities for real estate investments.",
        "Consider investing in retirement accounts for tax benefits.",
        "Focus on maintaining a good credit score for future financial needs."
    ],
    "80000 to 100000": [
        "Continue building wealth through diverse investment strategies.",
        "Consider estate planning to protect and pass on your assets.",
        "Review insurance coverage to ensure financial security.",
        "Explore opportunities for philanthropic contributions."
    ],
    "100000 to 150000": [
        "Diversify investments across multiple asset classes.",
        "Review and adjust investment portfolio to align with financial goals.",
        "Consider maximizing contributions to retirement accounts.",
        "Explore investment in higher education for career advancement."
    ],
    "150000 to 250000": [
        "Explore investment options in international markets for diversification.",
        "Consider advanced estate planning to minimize tax implications.",
        "Focus on sustainable investments aligned with personal values.",
        "Review and optimize investment strategy based on changing life goals."
    ],
    "250000 and above": [
        "Work with a financial advisor to develop a comprehensive wealth strategy.",
        "Consider philanthropic initiatives to give back to the community.",
        "Explore opportunities for legacy planning and wealth transfer.",
        "Focus on maintaining a balanced lifestyle while managing wealth."
    ]
}


# Streamlit app
st.set_page_config(page_title="FinSafe - Your Personal Financial Advisor", page_icon="💰")

# Header
st.title("Welcome to FinSafe")
st.write("Your Personal Financial Advisor for Smart Saving, Investing, and Debt Management")





# Input fields
age = st.number_input("Age:", min_value=0, max_value=100)
income = st.number_input("Monthly Income ($):", min_value=0, max_value=99999999)
debt = st.number_input("Debt ($):", min_value=0, max_value=99999999)

if "advice_counter" not in st.session_state:
            st.session_state.advice_counter = 0

if "advice_generated" not in st.session_state:
    st.session_state.advice_generated = False

if "first_load" not in st.session_state:
    st.session_state.first_load = True

generate_advice = st.button("Generate Advice")
# Display financial advice
if generate_advice:
    st.session_state.advice_counter += 1  # Increment the advice counter
    st.session_state.advice_generated = True

    with st.spinner("Generating advice for you..."):
        sleep_time = random.uniform(3, 6)  # Generate random sleep time between 2 to 4 seconds
        time.sleep(sleep_time)  # Simulate loading for 2 seconds

    # Display advice
if st.session_state.advice_generated:
    if st.session_state.first_load:
        st.session_state.first_load = False  # Set the flag to False

    if not st.session_state.first_load:
        st.subheader("Financial Advice:")

        if debt > 0:
            st.write("Priority: Pay off your debt as soon as possible to reduce financial stress.")

        if age >= 50:
            advice_age = age_advice["50 and above"]
        elif 35 <= age < 50:
            advice_age = age_advice["35 to 50"]
        else:
            advice_age = age_advice["below 35"]

        if income < 10000:
            advice_income = income_advice["below 10000"]
        elif 10000 <= income < 15000:
            advice_income = income_advice["10000 to 15000"]
        elif 15000 <= income < 25000:
            advice_income = income_advice["15000 to 25000"]
        elif 25000 <= income < 40000:
            advice_income = income_advice["25000 to 40000"]
        elif 40000 <= income < 60000:
            advice_income = income_advice["40000 to 60000"]
        elif 60000 <= income < 80000:
            advice_income = income_advice["60000 to 80000"]
        elif 80000 <= income < 100000:
            advice_income = income_advice["80000 to 100000"]
        elif 100000 <= income < 150000:
            advice_income = income_advice["100000 to 150000"]
        elif 150000 <= income < 250000:
            advice_income = income_advice["150000 to 250000"]
        else:
            advice_income = income_advice["250000 and above"]


        # Combine and display advice
        all_advice = advice_age + advice_income
        random.shuffle(all_advice)

        if "first_load" not in st.session_state:
            st.session_state.first_load = True

        if st.session_state.first_load:  # Check if it's the first time the page is loaded
            st.session_state.first_load = False
        else:
            # Display 3 to 4 advice points
            for advice in all_advice[:4]:
                st.write("- " + advice)

        
        

        #{st.session_state.advice_counter}

        st.write(f"FinSafe used: 324 times")


# Footer
st.markdown("---")
st.write("© 2023 FinSafe. All rights reserved.")
st.write("Disclaimer: The financial advice provided here is for educational purposes only and should not be considered as personalized financial advice. It is recommended to consult with a qualified financial advisor before making any investment decisions")
