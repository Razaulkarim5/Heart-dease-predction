from pydantic import BaseModel, Field


class HeartInput(BaseModel):
    age: int = Field(..., ge=1, le=120, examples=[52])
    sex: int = Field(..., ge=0, le=1, description="1 = male, 0 = female", examples=[1])
    cp: int = Field(..., ge=0, le=3, description="Chest pain type (0-3)", examples=[0])
    trestbps: int = Field(..., ge=50, le=300, description="Resting blood pressure", examples=[125])
    chol: int = Field(..., ge=50, le=700, description="Serum cholesterol (mg/dl)", examples=[212])
    fbs: int = Field(..., ge=0, le=1, description="Fasting blood sugar > 120 mg/dl", examples=[0])
    restecg: int = Field(..., ge=0, le=2, description="Resting ECG result (0-2)", examples=[1])
    thalach: int = Field(..., ge=50, le=250, description="Max heart rate achieved", examples=[168])
    exang: int = Field(..., ge=0, le=1, description="Exercise-induced angina", examples=[0])
    oldpeak: float = Field(..., ge=0, le=10, description="ST depression", examples=[1.0])
    slope: int = Field(..., ge=0, le=2, description="Slope of peak exercise ST segment", examples=[2])
    ca: int = Field(..., ge=0, le=4, description="Major vessels colored (0-4)", examples=[2])
    thal: int = Field(..., ge=0, le=3, description="Thalassemia code (0-3)", examples=[3])


class PredictionOut(BaseModel):
    heart_disease: bool
    probability: float
