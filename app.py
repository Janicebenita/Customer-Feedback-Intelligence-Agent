from pathlib import Path
import pandas as pd
import streamlit as st

POSITIVE = {"good", "great", "excellent", "fast", "helpful", "easy", "love"}
NEGATIVE = {"bad", "poor", "slow", "broken", "difficult", "late", "unhappy", "refund"}
URGENT = {"unsafe", "fraud", "breach", "injury", "danger", "urgent"}
TOPICS = {"delivery": {"delivery", "late", "shipping"}, "product": {"product", "broken", "quality"}, "support": {"support", "agent", "response"}, "billing": {"billing", "charge", "refund", "payment"}}

def classify(text):
    words = set(str(text).lower().replace(".", "").replace(",", "").split())
    pos, neg, urgent = words & POSITIVE, words & NEGATIVE, words & URGENT
    sentiment = "Positive" if len(pos) > len(neg) else "Negative" if len(neg) > len(pos) else "Neutral/Mixed"
    matches = [(topic, words & terms) for topic, terms in TOPICS.items() if words & terms]
    topic = matches[0][0] if matches else "other"
    evidence = sorted(pos | neg | urgent | set().union(*(m[1] for m in matches)))
    return pd.Series({"sentiment": sentiment, "topic": topic, "urgency": "Urgent review" if urgent else "Standard", "evidence": ", ".join(evidence) or "No rule term matched"})

st.set_page_config(page_title="Feedback Intelligence Agent", page_icon="💬", layout="wide")
st.title("💬 Customer Feedback Intelligence Agent")
st.caption("Transparent theme detection; ambiguous language requires human review.")
uploaded = st.file_uploader("Upload feedback CSV", type="csv")
df = pd.read_csv(uploaded if uploaded else Path(__file__).with_name("sample_data.csv"))
if not {"feedback_id", "feedback"}.issubset(df.columns):
    st.error("CSV requires feedback_id and feedback columns"); st.stop()
results = pd.concat([df, df.feedback.apply(classify)], axis=1)
left, right = st.columns(2)
left.subheader("Topic summary"); left.dataframe(results.topic.value_counts().rename_axis("topic").reset_index(name="count"), hide_index=True)
right.subheader("Urgent review"); right.dataframe(results[results.urgency == "Urgent review"], hide_index=True, use_container_width=True)
st.subheader("Classified feedback"); st.dataframe(results, hide_index=True, use_container_width=True)
st.download_button("Download results", results.to_csv(index=False), "classified_feedback.csv", "text/csv")

