# Agent Development Kit (ADK) GDG Salvador Workshop

<img src="https://github.com/google/adk-docs/blob/main/docs/assets/agent-development-kit.png" alt="Agent Development Kit Logo" width="150">

[Agent Development Kit](https://github.com/google/adk-python) (ADK) is an open-source toolkit for building, evaluating,
and deploying AI agents.

This repository is a collection of ADK samples/tutorials to get you up to speed.

## Set Python environment

Navigate to the repository. Create and activate a Python virtual environment:

```shell
cd adk-demos
python -m venv .venv
source .venv/bin/activate
```

Install ADK:

```shell
pip install -r requirements.txt
```

## Configure Google AI or Vertex AI

Copy `dotenv` file to `.env` file and fill your Google AI or Vertex AI information.

Here's an example for Vertex AI configuration:

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-google-cloud-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

## For Google AI:

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey)
and set it in the `.env` file.

## For Vertex AI:

## Set gcloud

Check if your project is set:

```shell
gcloud config list

...
[core]
project = your-google-cloud-project-id
```

If not, set your project id:

```shell
gcloud config set core/project your-google-cloud-project-id
```

If not in Cloud Shell (i.e. running locally), authenticate:

```shell
gcloud auth application-default login
```

Enable Vertex AI API:

```shell
gcloud services enable aiplatform.googleapis.com
```

## References

- [Documentation: Agent Development Kit](https://google.github.io/adk-docs/)
- [GitHub: ADK Python repository](https://github.com/google/adk-python)
- [GitHub: ADK samples repository](https://github.com/google/adk-samples)
- [Github: ADK Demos - Mate Atamel](https://github.com/meteatamel/adk-demos)
- [Blog: From Zero to Multi-Agents: A Beginner’s Guide to Google Agent Development Kit (ADK)](https://medium.com/@sokratis.kartakis/from-zero-to-multi-agents-a-beginners-guide-to-google-agent-development-kit-adk-b56e9b5f7861)
- [GitHub: Google ADK Walkthrough: Your Step-by-Step Development Tutorial](https://github.com/sokart/adk-walkthrough/tree/main)
- [Blog: Agent Development Kit: Making it easy to build multi-agent applications](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/)
- [Awesome Google ADK](https://github.com/tsubasakong/awesome-google-adk)

---

This is not an official Google product.
This content is for educational purposes only, the code used from references is not owned by the author, and the author has any intentions to use it for commercial purposes.