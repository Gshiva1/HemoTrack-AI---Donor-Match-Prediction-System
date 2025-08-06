#
import streamlit as st
import pandas as pd
import joblib

# Load the ML model and encoders
model = joblib.load("donor_match_model.pkl")
le_bg = joblib.load("encoder_blood_group.pkl")
le_avail = joblib.load("encoder_availability.pkl")
le_screened = joblib.load("encoder_screened.pkl")

# Load donor dataset
df = pd.read_csv("donor_dataset_with_match.csv")

# Streamlit UI
st.set_page_config(page_title="HemoTrack AI - Donor Matcher", layout="centered")
st.title("🩸 HemoTrack AI - Donor Match Prediction System")

# Select recipient blood group
blood_groups = le_bg.classes_
recipient_blood_group = st.selectbox("🧬 Select Recipient's Blood Group", blood_groups)

# Select matching method
mode = st.radio("🔎 Choose Match Type", [
    "Recommended Match (Based on Rules)",
    "AI-Powered Match (Smarter Prediction)"
])

# Blood group compatibility map
blood_compatibility = {
    'A+': ['A+', 'A-', 'O+', 'O-'],
    'B+': ['B+', 'B-', 'O+', 'O-'],
    'AB+': list(blood_groups),
    'O+': ['O+', 'O-'],
    'A-': ['A-', 'O-'],
    'B-': ['B-', 'O-'],
    'AB-': ['AB-', 'A-', 'B-', 'O-'],
    'O-': ['O-']
}

# Rule-based match logic
def is_match(donor):
    return (
        donor['Blood_Group'] in blood_compatibility[recipient_blood_group] and
        donor['Availability'] == 'Yes' and
        donor['Screened'] == 'Yes' and
        donor['Last_Donation_Days_Ago'] > 90
    )

# Match button
if st.button("🔍 Find Matching Donors"):
    if "Rule-Based" in mode:
        matches = df[df.apply(is_match, axis=1)]
    else:
        temp_df = df.copy()

        # Encode features
        temp_df['Blood_Group'] = le_bg.transform(temp_df['Blood_Group'])
        temp_df['Availability'] = le_avail.transform(temp_df['Availability'])
        temp_df['Screened'] = le_screened.transform(temp_df['Screened'])

        # Predict match
        X = temp_df[['Blood_Group', 'Last_Donation_Days_Ago', 'Availability', 'Screened']]
        df['ML_Predicted_Match'] = model.predict(X)
        matches = df[df['ML_Predicted_Match'] == 1]

    # Display results
    st.success(f"✅ Found {len(matches)} matching donor(s)")
    st.dataframe(matches[['Donor_ID', 'Name', 'Blood_Group', 'Location', 'Last_Donation_Days_Ago']])

    # Download results
    st.download_button(
        "📥 Download Matching Donors",
        matches.to_csv(index=False).encode('utf-8'),
        file_name="matched_donors.csv",
        mime="text/csv"
    )
