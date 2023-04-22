# treasury-data-app-dev
Api + App for Supplemental Treasury Insights

```mermaid
graph LR
    A[Streamlit App] -->|HTTP Request| B(FastAPI Backend)
    B -->|AWS Storage| C[Amazon S3 Bucket]
```
