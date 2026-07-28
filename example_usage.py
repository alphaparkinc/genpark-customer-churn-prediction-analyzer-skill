from client import ChurnPredictionClient

def main():
    client = ChurnPredictionClient()
    res = client.predict_churn(usage_days=2, support_tickets=5)
    print(f"Result for churn_risk: {res['churn_risk']}")

if __name__ == "__main__":
    main()
