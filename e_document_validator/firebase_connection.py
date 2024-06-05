from firebase import firebase
import base64

firebase = firebase.FirebaseApplication('https://edocsverified-default-rtdb.firebaseio.com/', None)



def send_data_to_firebase(data, original_image_path, encoded_image_path):
    with open(original_image_path, "rb") as image_file:
        original_image_data = base64.b64encode(image_file.read()).decode('utf-8')

    with open(encoded_image_path, "rb") as image_file:
        encoded_image_data = base64.b64encode(image_file.read()).decode('utf-8')

    data['original_image'] = original_image_data
    data['encoded_image'] = encoded_image_data

    result = firebase.post('/documents', data)
    print(f"Data sent to Firebase: {result}")