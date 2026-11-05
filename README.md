# Heart Disease Prediction API (FastAPI + Docker + Render)

A FastAPI service that predicts heart disease from a scikit-learn model trained on the
[Kaggle Heart Disease dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).

## Structure
```
app/            FastAPI code (main.py, schemas.py)
model/          heart_model.joblib (trained model)
train.py        training script
Dockerfile
docker-compose.yml
requirements.txt
```

## Train the model
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# put heart.csv from Kaggle in data/
python train.py
```
Train with the pinned `requirements.txt` so the scikit-learn version matches the Docker image.

## Run with Docker
```bash
docker-compose build
docker-compose up
```
Swagger UI: http://localhost:8000/docs

## Endpoints
| Method | Path | Description |
|---|---|---|
| GET | /health | Liveness check |
| GET | /info | Model type and feature list |
| POST | /predict | Returns `heart_disease` true/false and probability |

### Example
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":52,"sex":1,"cp":0,"trestbps":125,"chol":212,"fbs":0,"restecg":1,
       "thalach":168,"exang":0,"oldpeak":1.0,"slope":2,"ca":2,"thal":3}'
```

## Deploy on Render
1. Push this repo to GitHub (commit `model/heart_model.joblib`).
2. Render -> New -> Web Service -> connect the repo.
3. Language/Environment: **Docker**; root directory/build context: repo root.
4. Deploy, then test `https://<your-service>.onrender.com/docs`.

Live URL: https://heart-dease-predction.onrender.com/docs
