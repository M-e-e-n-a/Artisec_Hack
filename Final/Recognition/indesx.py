from flask import Flask, render_template, request
import cv2
import face_recognition

app = Flask(__name__)

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply histogram equalization
    gray_eq = cv2.equalizeHist(gray)
    return gray_eq

def detect_faces(image_path):
    image = face_recognition.load_image_file(image_path)
    image = preprocess_image(image_path)
    face_locations = face_recognition.face_locations(image)
    return face_locations

def compare_faces(image1_path, image2_path):
    face_locations1 = detect_faces(image1_path)
    face_locations2 = detect_faces(image2_path)

    if len(face_locations1) == 0 or len(face_locations2) == 0:
        return False

    face_encodings1 = face_recognition.face_encodings(face_recognition.load_image_file(image1_path), face_locations1)
    face_encodings2 = face_recognition.face_encodings(face_recognition.load_image_file(image2_path), face_locations2)

    for face_encoding1 in face_encodings1:
        for face_encoding2 in face_encodings2:
            # Compare the face encodings
            matches = face_recognition.compare_faces([face_encoding1], face_encoding2)
            if any(matches):
                return True

    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare_faces', methods=['POST'])
def compare_faces_route():
    if 'image1' not in request.files or 'image2' not in request.files:
        return 'Please upload both image1 and image2.'

    image1 = request.files['image1']
    image2 = request.files['image2']
    
    image1_path = 'uploads/image1.jpg'
    image2_path = 'uploads/image2.jpg'
    
    image1.save(image1_path)
    image2.save(image2_path)

    same_faces = compare_faces(image1_path, image2_path)
    return render_template('result.html', same_faces=same_faces)

if __name__ == '__main__':
    app.run(debug=True)
