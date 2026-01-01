from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from textblob import TextBlob
import uvicorn

app = FastAPI(
    title="Sentiment Scope API",
    description="A microservice for sentiment analysis using TextBlob",
    version="1.0.0"
)

class AnalysisRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The text content to analyze")

class SentimentResponse(BaseModel):
    text: str
    polarity: float
    subjectivity: float
    verdict: str

def get_verdict(polarity: float) -> str:
    if polarity > 0.1:
        return "POSITIVE"
    elif polarity < -0.1:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

@app.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(request: AnalysisRequest):
    """
    Analyze the sentiment of the provided text.
    """
    try:
        blob = TextBlob(request.text)
        sentiment = blob.sentiment
        
        return SentimentResponse(
            text=request.text,
            polarity=round(sentiment.polarity, 4),
            subjectivity=round(sentiment.subjectivity, 4),
            verdict=get_verdict(sentiment.polarity)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
