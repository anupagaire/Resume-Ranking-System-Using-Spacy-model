# 📄 Resume Ranking System Using SpaCy
A **Resume Ranking System** built with **SpaCy**, an advanced NLP library, to rank resumes based on job descriptions by analyzing PDF resumes. This system leverages **MongoDB** for efficient data storage and retrieval, making it ideal for recruiters and HR professionals to streamline candidate selection.

## 🚀 Features
- 📑 **NLP-Powered Resume Parsing**: Extracts and analyzes key information from PDF resumes using SpaCy.
- 🔍 **Job Description Matching**: Ranks resumes based on relevance to job descriptions.
- 💾 **MongoDB Integration**: Stores resume data and job descriptions securely.
- 🔐 **Google OAuth Authentication**: Secure access to the system via Google credentials.

<img width="368" height="188" alt="image" src="https://github.com/user-attachments/assets/74b61deb-c7cf-4195-ac39-8dc343833aa5" />
<img width="368" height="188" alt="image" src="https://github.com/user-attachments/assets/5a1831f8-2ef8-4112-b628-b85c1bee39c7" />
<img width="368" height="188" alt="image" src="https://github.com/user-attachments/assets/21534cd6-ccec-48b4-8a14-bb4c37cc2cf9" />
<img width="263" height="262" alt="image" src="https://github.com/user-attachments/assets/ec74a59f-8291-4045-9c37-c80c32312b89" />

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





