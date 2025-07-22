# 📄 Resume Ranking System Using SpaCy
A **Resume Ranking System** built with **SpaCy**, an advanced NLP library, to rank resumes based on job descriptions by analyzing PDF resumes. This system leverages **MongoDB** for efficient data storage and retrieval, making it ideal for recruiters and HR professionals to streamline candidate selection.

## 🚀 Features
- 📑 **NLP-Powered Resume Parsing**: Extracts and analyzes key information from PDF resumes using SpaCy.
- 🔍 **Job Description Matching**: Ranks resumes based on relevance to job descriptions.
- 💾 **MongoDB Integration**: Stores resume data and job descriptions securely.
- 🔐 **Google OAuth Authentication**: Secure access to the system via Google credentials.

## 📋 Prerequisites

Before running the project, ensure the following dependencies are installed:

### Install Required Libraries
The required libraries are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt

🛠️ Setup Instructions
1. **Build the Resume and Job Description Model**
Follow the steps in resume.ipynb to create and train the SpaCy model.
Run the notebook in Google Colab with your data in JSON format.
Ensure your dataset includes resumes and job descriptions for training.
2. **Configure Google OAuth**
Add the Google OAuth client secret JSON file for authentication.
Name the file client_secret.json and place it in the project root directory.
Refer to Google's OAuth documentation for setup details

<img src="https://github.com/user-attachments/assets/0717dc4f-80be-439d-b025-19daaf86d7b5" alt="Resume Upload Interface" style="width: 180px; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"> <img src="https://github.com/user-attachments/assets/05944902-586d-4d4a-a8a1-9b78e25ada50" alt="Ranking Dashboard" style="width: 180px; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"> <img src="https://github.com/user-attachments/assets/75c8c172-7a4e-4ca4-8c6b-b37a15f95ed2" alt="Job Description Input" style="width: 180px; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"> <img src="https://github.com/user-attachments/assets/71072885-c134-4e28-a835-4d36c91c8c85" alt="Results Overview" style="width: 180px; height: auto; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
