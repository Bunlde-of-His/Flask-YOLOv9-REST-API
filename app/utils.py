import base64


def save_base64_to_image(base64_string, output_path):
    try:
        image_data = base64.b64decode(base64_string)
        with open(output_path, "wb") as f:
            f.write(image_data)
    except Exception as e:
        print(f"Error saving image: {e}")
