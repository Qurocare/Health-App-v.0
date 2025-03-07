import streamlit as st
from score_calculator import calculate_physical_score, calculate_mental_score, calculate_lifestyle_score

# Streamlit App
st.title("Comprehensive Health Score Calculator")

# Input parameters for Physical Health
st.header("Physical Health Parameters")
physical_params = {
    'systolic': st.number_input("Systolic Pressure (mmHg)", min_value=0),
    'diastolic': st.number_input("Diastolic Pressure (mmHg)", min_value=0),
    'heart_rate': st.number_input("Heart Rate (BPM)", min_value=0),
    'respiratory_rate': st.number_input("Respiratory Rate (breaths/min)", min_value=0),
    'temperature': st.number_input("Body Temperature (°C)", min_value=0.0),
    'oxygen_saturation': st.number_input("Oxygen Saturation (%)", min_value=0),
}

# Input parameters for Mental Health
st.header("Mental Health Parameters")
mental_params = {
    'cortisol': st.number_input("Cortisol Levels (µg/dL)", min_value=0.0),
    'serotonin': st.number_input("Serotonin Levels (ng/mL)", min_value=0),
    'vitamin_d': st.number_input("Vitamin D Levels (ng/mL)", min_value=0),
}

# Input parameters for Lifestyle
st.header("Lifestyle Parameters")
lifestyle_params = {
    'sleep_hours': st.number_input("Sleep Hours per Night", min_value=0),
    'steps': st.number_input("Physical Activity (Steps per day)", min_value=0),
    'screen_time': st.number_input("Screen Time (hours/day)", min_value=0.0),
}

# Calculate scores
physical_score = calculate_physical_score(physical_params)
mental_score = calculate_mental_score(mental_params)
lifestyle_score = calculate_lifestyle_score(lifestyle_params)

# Normalize scores
normalized_physical_score = (physical_score / 50) * 100
normalized_mental_score = (mental_score / 25) * 100
normalized_lifestyle_score = (lifestyle_score / 25) * 100

# Weighted total score
total_score = (
    (normalized_physical_score * 0.5) +
    (normalized_mental_score * 0.25) +
    (normalized_lifestyle_score * 0.25)
)

if st.button("Show Total Score"):
    st.subheader(f"Your Total Health Score: {total_score:.2f}")

# Alerts function
def get_parameter_alerts(physical_score, mental_score, lifestyle_score, physical_params, mental_params, lifestyle_params):
    alerts = []

    # Physical Health Alerts
    if physical_params['systolic'] < 90 or physical_params['systolic'] > 180:
        alerts.append(("Critical", "Critical Alert: Systolic Pressure out of range!"))
    elif physical_params['systolic'] < 100 or physical_params['systolic'] > 160:
        alerts.append(("Moderate", "Moderate Alert: Systolic Pressure is borderline."))

    if physical_params['diastolic'] < 50 or physical_params['diastolic'] > 120:
        alerts.append(("Critical", "Critical Alert: Diastolic Pressure out of range!"))
    elif physical_params['diastolic'] < 60 or physical_params['diastolic'] > 100:
        alerts.append(("Moderate", "Moderate Alert: Diastolic Pressure is borderline."))

    if physical_params['heart_rate'] < 50 or physical_params['heart_rate'] > 140:
        alerts.append(("Critical", "Critical Alert: Heart Rate out of range!"))
    elif physical_params['heart_rate'] < 60 or physical_params['heart_rate'] > 120:
        alerts.append(("Moderate", "Moderate Alert: Heart Rate is borderline."))

    if physical_params['respiratory_rate'] < 10 or physical_params['respiratory_rate'] > 30:
        alerts.append(("Critical", "Critical Alert: Respiratory Rate out of range!"))
    elif physical_params['respiratory_rate'] < 12 or physical_params['respiratory_rate'] > 24:
        alerts.append(("Moderate", "Moderate Alert: Respiratory Rate is borderline."))

    if physical_params['temperature'] < 35 or physical_params['temperature'] > 39.4:
        alerts.append(("Critical", "Critical Alert: Body Temperature out of range!"))
    elif physical_params['temperature'] < 36 or physical_params['temperature'] > 38:
        alerts.append(("Moderate", "Moderate Alert: Body Temperature is borderline."))

    if physical_params['oxygen_saturation'] < 90:
        alerts.append(("Critical", "Critical Alert: Oxygen Saturation is dangerously low!"))
    elif physical_params['oxygen_saturation'] < 95:
        alerts.append(("Moderate", "Moderate Alert: Oxygen Saturation is borderline."))

    # Mental Health Alerts
    if mental_params['cortisol'] < 2 or mental_params['cortisol'] > 30:
        alerts.append(("Critical", "Critical Alert: Cortisol levels are dangerously low or high!"))
    elif mental_params['cortisol'] < 5 or mental_params['cortisol'] > 25:
        alerts.append(("Moderate", "Moderate Alert: Cortisol levels are borderline."))

    if mental_params['serotonin'] < 50 or mental_params['serotonin'] > 350:
        alerts.append(("Critical", "Critical Alert: Serotonin levels are dangerously low or high!"))
    elif mental_params['serotonin'] < 101 or mental_params['serotonin'] > 283:
        alerts.append(("Moderate", "Moderate Alert: Serotonin levels are borderline."))

    if mental_params['vitamin_d'] < 10 or mental_params['vitamin_d'] > 200:
        alerts.append(("Critical", "Critical Alert: Vitamin D levels are dangerously low or high!"))
    elif mental_params['vitamin_d'] < 30 or mental_params['vitamin_d'] > 100:
        alerts.append(("Moderate", "Moderate Alert: Vitamin D levels are borderline."))

    # Lifestyle Alerts
    if lifestyle_params['sleep_hours'] < 4 or lifestyle_params['sleep_hours'] > 12:
        alerts.append(("Critical", "Critical Alert: Sleep hours are not in the recommended range!"))
    elif lifestyle_params['sleep_hours'] < 6 or lifestyle_params['sleep_hours'] > 10:
        alerts.append(("Moderate", "Moderate Alert: Sleep hours are borderline."))

    if lifestyle_params['steps'] < 3000 or lifestyle_params['steps'] > 20000:
        alerts.append(("Critical", "Critical Alert: Step count is outside the healthy range!"))
    elif lifestyle_params['steps'] < 5000 or lifestyle_params['steps'] > 15000:
        alerts.append(("Moderate", "Moderate Alert: Step count is borderline."))

    if lifestyle_params['screen_time'] > 8:
        alerts.append(("Critical", "Critical Alert: Excessive screen time!"))
    elif lifestyle_params['screen_time'] > 4:
        alerts.append(("Moderate", "Moderate Alert: High screen time."))

    return alerts


if st.button("View Alerts"):
    alerts = get_parameter_alerts(physical_score, mental_score, lifestyle_score, physical_params, mental_params, lifestyle_params)
    if alerts:
        for level, message in alerts:
            color = "orange" if level == "Moderate" else "red"
            st.markdown(f"<p style='color:{color}'>{level} Alert: {message}</p>", unsafe_allow_html=True)

        if any(level == "Critical" for level, _ in alerts):
            st.error("Your critical health condition has been notified to the Qurocare clinic. A health specialist will connect with you shortly.")
            
            # Placeholder for real notification system (Email/SMS)
            admin_email = "care@qurocare.com"
            admin_number = "+916363594949"
            st.write(f"Notification sent to Admin: {admin_email}, {admin_number}")
            # Here you can integrate an actual email/SMS sending API (like SMTP or Twilio)
    else:
        st.success("No alerts. Your health scores are within normal range.")

