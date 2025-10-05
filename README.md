# 🤖 AI Attendance System — Face Recognition  
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-ff4b4b.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A modern **AI-powered Attendance System** built using **Face Recognition** and **Streamlit UI**.  
This project detects faces in real-time using your webcam and automatically marks attendance — fast, simple, and efficient! 🚀

---

## 🌟 Features
✅ Register faces by uploading images (auto-saved in `registered_faces/`)  
✅ Real-time webcam detection using `face_recognition` + `OpenCV`  
✅ Marks attendance with Name, Time, and Date  
✅ Displays attendance table live in the app  
✅ Simple, clean, and fast **Streamlit** interface  
✅ Optional: Export attendance as CSV file  

---

## 🧰 Technologies Used
| Category | Tools / Libraries |
|-----------|-------------------|
| Frontend UI | Streamlit |
| Face Recognition | face_recognition (based on dlib) |
| Image Processing | OpenCV |
| Data Handling | Pandas, Numpy |
| Image Handling | Pillow |
| Language | Python 3.8+ |

---

## 🧭 How to Run

```bash
# Clone this repository
git clone https://github.com/Anuj-singh-codehub-official/AI-Attendance-System-Using-Face-Recognition.git

# Navigate to project folder
cd AI-Attendance-System-Using-Face-Recognition

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run "AI Attendance.py"

---

## 📁 Project Structure
├── AI Attendance.py      # Main application file
├── registered_faces/     # Folder containing saved face images
├── attendance.csv        # Attendance records
├── requirements.txt      # Dependencies
├── demo-screenshot.png   # App screenshot (upload to repo)
├── README.md             # Documentation
