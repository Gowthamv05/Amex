import streamlit as st
import pandas as pd

# Sample Data for Amex Cards
cards_data = [
    {
        "Card Name": "Amex Gold Card",
        "Min Salary": 25000,
        "Max Salary": 75000,
        "Annual Fee": 2000,
        "Benefits": "4x rewards on dining, 2x on shopping, travel vouchers",
        "Maximize Benefits": "Focus on dining and shopping spends to maximize points. Redeem points for travel vouchers or shopping credits.",
        "Rewards Strategy": "Spend primarily on dining to earn 4x points. Combine points for travel redemptions through Amex Travel or transfer to partner airlines.",
        "Fee Waiver": "Fee waiver on spending INR 1.5 lakh annually.",
        "Spend Categories": ["Dining", "Shopping", "Travel"],
        "Referral Link": "https://americanexpress.com/en-in/referral/platinum-travel?ref=gOWTHVYVIs&XL=MIMNS"
    },
    {
        "Card Name": "Amex Platinum Travel Card",
        "Min Salary": 50000,
        "Max Salary": 150000,
        "Annual Fee": 5000,
        "Benefits": "joining bonus 10K, while spending 1.9L another 15k bonus then while spending 4 lakhs another 25K bonus.3X on multiplier.",
        "Maximize Benefits": "Use for travel-related purchases. Reach annual spending milestones for vouchers.",
        "Rewards Strategy": "Earn accelerated points on travel bookings. Redeem vouchers for flights or Flipkart voucher ot hotel stays to maximize value." ,
        "Fee Waiver": "Fee waiver on spending INR 7 lakh annually, can negotiate with customer care for fee waiver/discount.",
        "Spend Categories": ["Travel", "Hotel stays"],
        "Referral Link": "https://americanexpress.com/en-in/referral/platinum-travel?ref=gOWTHVYVIs&XL=MIMNS"
    },
    {
        "Card Name": "Amex SmartEarn Credit Card",
        "Min Salary": 37500,
        "Max Salary": 600000,
        "Annual Fee": 495,
        "Benefits": "10x rewards on Flipkart, Uber, and more; 5x on Amazon",
        "Maximize Benefits": "Utilize accelerated rewards categories like Flipkart and Uber for maximum points.",
        "Rewards Strategy": "Redeem points for online shopping vouchers or transfer to loyalty programs for added value.",
        "Fee Waiver": "Fee waiver on spending INR 40,000 annually.",
        "Spend Categories": ["Online Shopping", "Uber", "Dining"],
        "Referral Link": "https://americanexpress.com/en-in/referral/platinum-travel?ref=gOWTHVYVIs&XL=MIMNS"
    },
    # Add other cards similarly with different spend categories...
]

def recommend_card(salary, spend_categories):
    recommendations = []
    for card in cards_data:
        if card["Min Salary"] <= salary <= card["Max Salary"]:
            if any(spend_category in card["Spend Categories"] for spend_category in spend_categories):
                recommendations.append(card)
    return recommendations

# Streamlit App
st.title("Amex Card Recommender")
st.write("Enter your salary and preferred spending categories to find the best-suited American Express card for you.")

# User Input for Salary
salary = st.number_input("Enter your monthly salary (in INR):", min_value=0, step=1000)

# User Input for Spend Categories (using multiselect for multiple categories)
spend_categories = st.multiselect(
    "Select your nature of spends:",
    ["Online Shopping", "Travel", "Hotel Stays", "Dining", "Uber", "Offline Shopping"]
)

if salary > 0 and spend_categories:
    recommendations = recommend_card(salary, spend_categories)

    if recommendations:
        st.subheader("Recommended Cards")
        for card in recommendations:
            st.markdown(f"### {card['Card Name']}")
            st.write(f"**Annual Fee:** INR {card['Annual Fee']}")
            st.write(f"**Benefits:** {card['Benefits']}")
            st.write(f"**How to Maximize Benefits:** {card['Maximize Benefits']}")
            st.write(f"**Rewards Strategy:** {card['Rewards Strategy']}")
            st.write(f"**Fee Waiver:** {card['Fee Waiver']}")
            st.write(f"[Apply Now]({card['Referral Link']})")
            st.write("---")
    else:
        st.write("Sorry, we couldn't find a suitable card for your salary range and selected spending categories.")

st.write("For more details, visit [American Express India](https://www.americanexpress.com/in/).")
