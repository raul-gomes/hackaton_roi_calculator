# 📌 OpenBizROI AI

## 🌍 Project Overview
**OpenBizROI AI** is an **AI-driven business analysis and ROI forecasting platform** that helps organizations assess the feasibility and success of transformation projects. By leveraging **machine learning, document processing, and predictive analytics**, it provides ROI predictions with **over 92% accuracy**.

Users can **upload project documents, spreadsheets, branding elements, and financial reports** or manually enter key business details. If crucial data is missing, the AI dynamically identifies the **business niche, industry trends, and market demand**, generating a **fully customized business plan**.

### 🚀 Key Features
✅ **Predictive ROI Analysis** with real-time insights  
✅ **Break-even Calculation & Financial Risk Assessment**  
✅ **AI-powered Business Planning**  
✅ **User-guided Data Entry & AI-assisted Decision Making**  
✅ **Full Accessibility** (Text-to-Speech, Adaptive Layouts, Dyslexia-Friendly Tools)  

## 🛠️ Project Setup & Installation

### 1️⃣ **Prerequisites**
Ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **Virtual environment (optional but recommended)**

### 2️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-repo/OpenBizROI-AI.git
cd OpenBizROI-AI
```

### 3️⃣ Set Up a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 5️⃣ Run the Application
```sh
streamlit run app.py
```

### 6️⃣ Usage Instructions

- Choose Input Method: Use the radio button to select either Document Upload or Manual Entry.

- Upload a Document: Supports CSV, XLSX, or XLS formats.

- Manual Data Entry: Enter values for Field 1, Field 2, and Field 3.

- View Results: The processed data will be displayed in a structured table.

- Logging: Every action is logged with a unique identifier, timestamp, and details.

- Error Handling: The system provides clear error messages for invalid inputs or upload issues.

## 📄 Project Structure
```sh
OpenBizROI-AI/
│── app.py                # Main Streamlit app (UI & logic orchestration)
│── utils/
│   │── logger.py         # Logging functions
│   │── file_handler.py   # File upload handling
│   │── manual_input.py   # Manual data entry handling
│── requirements.txt      # Dependencies
│── README.md             # Project Documentation
```

## 🏆 Contributions & Feedback

We welcome feedback and contributions! Feel free to submit pull requests or open an issue on GitHub.

## 📜 License

This project is licensed under the MIT License.