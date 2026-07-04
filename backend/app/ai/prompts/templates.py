from enum import Enum

class PromptTemplate(Enum):
    GENERAL_ASSISTANT = "You are Ceylon Sentinel AI, a helpful enterprise assistant."
    WEATHER_ANALYSIS = "Analyze the following weather data for anomalies: {data}"
    NEWS_ANALYSIS = "Extract critical events from the following news text: {data}"
    POLICY_RECOMMENDATION = "Recommend disaster response policies for: {scenario}"
    RISK_ASSESSMENT = "Assess the infrastructure risk for: {data}"
    SUMMARIZATION = "Summarize the following report: {text}"
    TRANSLATION = "Translate the following to {language}: {text}"
    CLASSIFICATION = "Classify the following incident: {text}"
    ENTITY_EXTRACTION = "Extract named entities from: {text}"
