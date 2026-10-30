# Customer Feedback Intelligence Agent Explainability

## Decision and Reasoning Process

The agent's decision classifies each feedback item by detected sentiment, topic, urgency, and product area before aggregating themes. Its reasoning preserves the source text that supports major findings and distinguishes direct statements from inferred themes.

## Inputs and Data Sources Used

Input data may include customer reviews, surveys, support comments, interview notes, and authorized feedback exports. Personal identifiers should be removed or protected, and the agent uses only the fields supplied for analysis.

## Outputs and Supporting Evidence

The output includes theme counts, sentiment summaries, urgent items, representative excerpts, and recommended areas for investigation. Supporting evidence consists of the relevant feedback records and aggregation counts rather than invented customer opinions.

## Limits, Constraints, and Known Issues

A limitation is that sentiment and topic classification can misread sarcasm, multilingual text, short comments, slang, or context-dependent wording. The available feedback may also be unrepresentative because of response bias or missing customer segments.

## Uncertainty and Human Review

The agent marks ambiguous classifications and low-volume themes as uncertain. Human review is required before contacting customers, publishing claims, changing policy, making product commitments, or escalating sensitive complaints.

## Implementation in This Repository

The executable implementation is in `app.py`. Its `classify(text)` function tokenizes each feedback message, compares the tokens with the declared `POSITIVE`, `NEGATIVE`, `URGENT`, and `TOPICS` rule sets, and returns sentiment, the first matched topic, urgency, and the exact matched terms as evidence.

The Streamlit path loads an uploaded CSV or `sample_data.csv`, verifies the `feedback_id` and `feedback` columns, applies `classify` to every row, displays topic and urgent-review tables, and exports `classified_feedback.csv`. It does not contact customers or change product systems; the rule terms remain visible for human interpretation.

