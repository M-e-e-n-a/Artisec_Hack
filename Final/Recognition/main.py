import cv2
import face_recognition
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

# Provide the paths to your images here
image1_path = '23.jpg'
image2_path = 'reference_1.jpg'

same_faces = compare_faces(image1_path, image2_path)
if same_faces:
    print("The faces are the same.")
else:
    print("The faces are different.")