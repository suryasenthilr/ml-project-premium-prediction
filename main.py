import streamlit as st
from prediction_helper import predict

# Set the page configuration
st.set_page_config(
    page_title="Health Insurance Cost Predictor - Surya S",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 50%, #2E7D32 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    }

    .section-header {
        color: #4CAF50;
        font-size: 1.3em;
        font-weight: bold;
        margin: 2rem 0 1rem 0;
        border-bottom: 3px solid #4CAF50;
        padding-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .info-card {
        background: rgba(76, 175, 80, 0.1);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }

    .prediction-result {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-top: 2rem;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    }

    .metric-container {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(76, 175, 80, 0.3);
        margin: 0.5rem 0;
        text-align: center;
    }

    .stButton > button {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.2em;
        font-weight: bold;
        border-radius: 25px;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 1rem;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
    }

    .risk-indicator {
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin: 0.5rem 0;
        text-align: center;
    }

    .low-risk {
        background: #C8E6C9;
        color: #2E7D32;
    }

    .medium-risk {
        background: #FFF3E0;
        color: #F57C00;
    }

    .high-risk {
        background: #FFCDD2;
        color: #D32F2F;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🏥 Health Insurance Cost Predictor</h1>
    <h2>by Surya S</h2>
    <h3>AI-Powered Premium Estimation</h3>
    <p>Get accurate insurance cost predictions based on your health profile</p>
</div>
""", unsafe_allow_html=True)

# Define categorical options
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create sidebar with information
with st.sidebar:
    st.markdown("### 📋 How to Use")
    st.info("""
    **Steps:**
    1. Fill all personal details
    2. Select your health information
    3. Choose insurance preferences
    4. Click 'Predict Cost'
    5. View your estimated premium
    """)

    st.markdown("### 💡 Cost Factors")
    st.warning("""
    **Key factors affecting cost:**
    - Age and health condition
    - Smoking habits
    - BMI category
    - Medical history
    - Insurance plan type
    - Number of dependants
    """)

    st.markdown("### 📊 Plan Comparison")
    st.markdown("""
    **🥉 Bronze:** Basic coverage, lower premium

    **🥈 Silver:** Balanced coverage and cost

    **🥇 Gold:** Comprehensive coverage, higher premium
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Personal Information Section
    st.markdown('<div class="section-header">👤 Personal Information</div>', unsafe_allow_html=True)

    row1 = st.columns(3)
    with row1[0]:
        age = st.number_input('Age', min_value=18, step=1, max_value=100, value=30, help="Your current age")
    with row1[1]:
        gender = st.selectbox('Gender', categorical_options['Gender'], help="Select your gender")
    with row1[2]:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'],
                                      help="Your marital status")

    # Family & Financial Information
    st.markdown('<div class="section-header">👨‍👩‍👧‍👦 Family & Financial Details</div>', unsafe_allow_html=True)

    row2 = st.columns(3)
    with row2[0]:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20, value=2,
                                               help="Family members covered")
    with row2[1]:
        income_lakhs = st.number_input('Annual Income (Lakhs)', step=1, min_value=0, max_value=200, value=10,
                                       help="Your annual income in lakhs")
    with row2[2]:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'],
                                         help="Your current employment type")

    # Health Information
    st.markdown('<div class="section-header">🏥 Health Information</div>', unsafe_allow_html=True)

    row3 = st.columns(3)
    with row3[0]:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'],
                                    help="Your Body Mass Index category")
    with row3[1]:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'],
                                      help="Your smoking habits")
    with row3[2]:
        genetical_risk = st.number_input('Genetic Risk Score', step=1, min_value=0, max_value=5, value=2,
                                         help="Family history risk (0=Low, 5=High)")

    # Medical History & Location
    st.markdown('<div class="section-header">📋 Medical History & Location</div>', unsafe_allow_html=True)

    row4 = st.columns(2)
    with row4[0]:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'],
                                       help="Your current medical conditions")
    with row4[1]:
        region = st.selectbox('Region', categorical_options['Region'], help="Your geographical region")

    # Insurance Plan Selection
    st.markdown('<div class="section-header">🛡️ Insurance Plan</div>', unsafe_allow_html=True)

    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'],
                                  help="Choose your preferred plan")

    # Plan details
    plan_details = {
        'Bronze': {'coverage': '₹3-5 Lakhs', 'premium': 'Low', 'features': 'Basic coverage, Emergency care'},
        'Silver': {'coverage': '₹5-10 Lakhs', 'premium': 'Medium', 'features': 'Balanced coverage, Preventive care'},
        'Gold': {'coverage': '₹10+ Lakhs', 'premium': 'High', 'features': 'Comprehensive coverage, Premium facilities'}
    }

    if insurance_plan:
        plan_info = plan_details[insurance_plan]
        st.info(
            f"**{insurance_plan} Plan:** {plan_info['features']} | Coverage: {plan_info['coverage']} | Premium: {plan_info['premium']}")

with col2:
    # Risk Assessment Panel
    st.markdown('<div class="section-header">⚠️ Risk Assessment</div>', unsafe_allow_html=True)

    # Calculate risk factors
    risk_score = 0
    risk_factors = []

    if age > 50:
        risk_score += 1
        risk_factors.append("Age > 50")
    if smoking_status in ['Regular', 'Occasional']:
        risk_score += 2
        risk_factors.append("Smoking habits")
    if bmi_category in ['Obesity', 'Overweight']:
        risk_score += 1
        risk_factors.append("BMI concerns")
    if medical_history != 'No Disease':
        risk_score += 2
        risk_factors.append("Medical history")
    if genetical_risk > 3:
        risk_score += 1
        risk_factors.append("High genetic risk")

    # Display risk level
    if risk_score <= 2:
        risk_level = "Low Risk"
        risk_class = "low-risk"
        risk_icon = "🟢"
    elif risk_score <= 4:
        risk_level = "Medium Risk"
        risk_class = "medium-risk"
        risk_icon = "🟡"
    else:
        risk_level = "High Risk"
        risk_class = "high-risk"
        risk_icon = "🔴"

    st.markdown(f"""
    <div class="metric-container">
        <h3>{risk_icon} Risk Level</h3>
        <div class="risk-indicator {risk_class}">
            {risk_level}
        </div>
        <p><strong>Risk Score:</strong> {risk_score}/7</p>
    </div>
    """, unsafe_allow_html=True)

    # Risk factors
    if risk_factors:
        st.markdown("**Risk Factors:**")
        for factor in risk_factors:
            st.markdown(f"• {factor}")
    else:
        st.success("✅ No major risk factors identified!")

    # Premium estimate indicator
    base_premium = 15000  # Base premium
    plan_multiplier = {'Bronze': 0.8, 'Silver': 1.0, 'Gold': 1.3}
    risk_multiplier = 1 + (risk_score * 0.15)
    age_multiplier = 1 + ((age - 25) * 0.02) if age > 25 else 1
    dependant_cost = number_of_dependants * 3000

    estimated_premium = int(
        (base_premium * plan_multiplier.get(insurance_plan, 1) * risk_multiplier * age_multiplier) + dependant_cost)

    st.markdown(f"""
    <div class="metric-container">
        <h3>💰 Estimated Range</h3>
        <h2>₹{estimated_premium - 5000:,} - ₹{estimated_premium + 5000:,}</h2>
        <small>Annual premium estimate</small>
    </div>
    """, unsafe_allow_html=True)

# Create input dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Prediction button
st.markdown("---")
if st.button('🔍 Get Accurate Premium Quote', key="predict_btn"):
    with st.spinner('Calculating your personalized premium...'):
        try:
            prediction = predict(input_dict)

            # Display results with enhanced styling
            st.markdown(f"""
            <div class="prediction-result">
                <h2>🎯 Your Health Insurance Premium</h2>
                <h1 style="font-size: 3em; margin: 1rem 0;">₹{prediction:,}</h1>
                <p style="font-size: 1.2em;">Annual Premium Amount</p>
                <div style="margin-top: 2rem; display: flex; justify-content: space-around;">
                    <div>
                        <h4>Monthly</h4>
                        <h3>₹{int(prediction / 12):,}</h3>
                    </div>
                    <div>
                        <h4>Quarterly</h4>
                        <h3>₹{int(prediction / 4):,}</h3>
                    </div>
                    <div>
                        <h4>Half-Yearly</h4>
                        <h3>₹{int(prediction / 2):,}</h3>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Additional insights
            st.markdown("### 💡 Premium Breakdown Insights")

            col_a, col_b, col_c = st.columns(3)

            with col_a:
                st.info(f"""
                **Plan Impact**
                {insurance_plan} Plan
                Coverage level affects base premium
                """)

            with col_b:
                st.warning(f"""
                **Risk Factors**
                Risk Score: {risk_score}/7
                {risk_level} category
                """)

            with col_c:
                st.success(f"""
                **Family Size**
                {number_of_dependants + 1} members covered
                Dependants: {number_of_dependants}
                """)

            # Recommendations
            st.markdown("### 🎯 Recommendations")
            recommendations = []

            if smoking_status != 'No Smoking':
                recommendations.append("🚭 Quit smoking to reduce premium by 15-25%")
            if bmi_category in ['Obesity', 'Overweight']:
                recommendations.append("🏃‍♂️ Maintain healthy BMI to get better rates")
            if risk_score > 4:
                recommendations.append("🏥 Regular health checkups can help manage costs")
            if insurance_plan == 'Bronze':
                recommendations.append("⭐ Consider Silver/Gold for better coverage")

            if recommendations:
                for rec in recommendations:
                    st.info(rec)
            else:
                st.success("✅ You're getting a great rate! Your profile shows low risk factors.")

        except Exception as e:
            st.error("Sorry, there was an error calculating your premium. Please check your inputs and try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p><strong>Health Insurance Cost Predictor by Surya S</strong> - AI-Powered Premium Estimation</p>
    <p><em>Disclaimer: This is an estimated calculation. Actual premiums may vary based on insurer policies and medical examinations.</em></p>
</div>
""", unsafe_allow_html=True)