# Treasury Data App Dev
`App` + Api for Supplemental Treasury Insights with enterprise cloud integrations capabilties. We also provide consulting services to further enhance your insights both development and rich SME treasury knowledge

## Services Offered
- Web App for Users
- API for Developers
- Consulting services for development & years of Treasury SME resources
    - GPT style Treasury AI (Development Phase) for AI Consulting

Deployments on `Google Cloud Run`
- `App`: https://treasury-data.app/
- `API`: https://treasury-data-app-dev-backend-ypo22oeifq-uc.a.run.app/docs

## Features
- `App`: Data Visualizations + Analysis of Supplemental Treasury Specific Insights
- `Api`: Developer Integration of Treasury Specific Insights

## Integrations
Custom Alchemy of Machine Learning Models to create thoughtful `insights` & `predictions`
- `h20.ai`: Based ML known for speed on JVMs
- `Hugging Face`: Largest provider of `Transformers` for specific modeling techniques
- `QuantumAI`: Using quantum computing for simulations from `Google's Cirq` framework

Cloud Providers: We toggle between major cloud providers via `Terraform` for effciency
- [x] Google Cloud Platform
- [x] AWS
- [x] Azure

## Tech Stack

Pure Python baby! For nimble development, keeping the frontend and backend in one language increases efficieny. chatGPT also has ton of Python data it's trained on ;) I think I could also get a shoutout from Streamlit from this guy, https://www.youtube.com/@andfanilo so good PR.

```mermaid
graph LR
    A[Terraform] -->|Provision Cloud| B(Streamlit App)
    B -->|API Request| C(FastAPI Backend)
    C -->|AWS Storage| D[Amazon S3 Bucket]
    C -->|Azure Storage| E[Azure Blob]
    C -->|GCP| F[Google Cloud Bucket]
```

`Note`: The Streamlit app can handle the POC + MVP stage but once 100 users is hit that will need to be rewritten to Javascript (React, Vue, Svelte). I would offshore this then chatGPT to replace the frontend. 
