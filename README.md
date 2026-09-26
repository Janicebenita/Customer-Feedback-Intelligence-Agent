# Customer Feedback Intelligence Agent

A lightweight, explainable voice-of-customer agent that classifies feedback by sentiment, topic, and urgency using transparent keyword rules. It preserves source comments for human review.

## Features

- CSV upload and sample feedback
- Sentiment, topic, and urgency labels
- Theme counts and urgent-item view
- Transparent evidence column
- Downloadable classified dataset

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Expected columns: `feedback_id,feedback`.

## Architecture and flow

The app normalizes each comment, applies visible dictionaries, records matched terms, aggregates themes, and presents the result. It does not contact customers or modify service records.

## Passport

The root contains `agent.yaml`, `SOUL.md`, and `EXPLAINABILITY.md`. Category: **Marketing & sales**.

