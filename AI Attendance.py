import streamlit as st
import cv2
import numpy as np
import pandas as pd
import os
from datetime import datetime
from PIL import Image

st.set_page_config(page_title="AI Attendance System", layout="wide")

if 'known_face_encodings' not in st.session_state:
    st.session_state.known_face_encodings = []
if 'known_face_names' not in st.session_state:
    st.session_state.known_face_names = []
if 'attendance_df' not in st.session_state:
    st.session_state.attendance_df = pd.DataFrame(columns=['Name', 'Time', 'Date'])

def load_faces():
    faces_folder = "registered_faces/"
    st.session_state.known_face_encodings = []
    st.session_state.known_face_names = []
    if os.path.exists(faces_folder):
        for filename in os.listdir(faces_folder):
            if filename.endswith((".jpg", ".png", ".jpeg")):
                name = os.path.splitext(filename)[0]
                image_path = os.path.join(faces_folder, filename)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                if len(encodings) > 0:
                    st.session_state.known_face_encodings.append(encodings[0])
                    st.session_state.known_face_names.append(name)

def mark_attendance(name):
    now = datetime.now()
    entry = pd.DataFrame({
        'Name': [name],
        'Time': [now.strftime("%H:%M:%S")],
        'Date': [now.strftime("%Y-%m-%d")]
    })
    st.session_state.attendance_df = pd.concat([st.session_state.attendance_df, entry], ignore_index=True)
    st.success(f"Attendance marked for {name}")

def main():
    st.title("🤖 AI Face Recognition Attendance System")
    st.markdown("---")
    load_faces()

    tab1, tab2 = st.tabs(["📷 Live Attendance", "👤 Register Face"])

    with tab1:
        st.header("Live Face Recognition Attendance")
        run = st.button("Start Camera")
        if run:
            cap = cv2.VideoCapture(0)
            stframe = st.empty()
            stop_button = st.button("Stop Camera", key="unique_stop_camera")
            while True:
                if stop_button:
                    break
                ret, frame = cap.read()
                if not ret:
                    st.error("Camera not found.")
                    break
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                    matches = face_recognition.compare_faces(st.session_state.known_face_encodings, face_encoding)
                    name = "Unknown"
                    face_distances = face_recognition.face_distance(st.session_state.known_face_encodings, face_encoding)
                    if len(face_distances) > 0:
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = st.session_state.known_face_names[best_match_index]
                            mark_attendance(name)
                    cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
                    cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0,255,0), cv2.FILLED)
                    cv2.putText(frame, name, (left+6, bottom-6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,255,255), 1)
                stframe.image(frame, channels="BGR")
            cap.release()
        st.subheader("Attendance Records")
        st.dataframe(st.session_state.attendance_df)

    with tab2:
        st.header("Register New Face")
        uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
        name = st.text_input("Enter name for registration")
        if uploaded_file and name:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            if st.button("Register Face"):
                faces_folder = "registered_faces/"
                os.makedirs(faces_folder, exist_ok=True)
                image_path = os.path.join(faces_folder, f"{name}.jpg")
                image.save(image_path)
                st.success(f"Registered {name}. You can now mark attendance.")
                load_faces()

if __name__ == "__main__":
    main()
