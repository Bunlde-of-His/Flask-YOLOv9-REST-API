from flask import Blueprint, request, jsonify
from .auth import auth
from .utils import save_base64_to_image
import cv2
import numpy as np
import base64
from ultralytics import YOLO
from colors import PREDEFINED_COLORS, LABEL_COLORS

yolo_model = YOLO("yolov9c.pt")


def get_color_for_label(label):
    if label not in LABEL_COLORS:
        LABEL_COLORS[label] = PREDEFINED_COLORS[len(LABEL_COLORS) % len(PREDEFINED_COLORS)]
    return LABEL_COLORS[label]


detect_bp = Blueprint('detect', __name__)


@detect_bp.route('/detect', methods=['POST'])
@auth.login_required
def detect_objects():
    try:

        data = request.get_json()
        input_base64 = data.get("InputBase64")
        if not input_base64:
            return jsonify({"error": "InputBase64 is missing"}), 400

        input_image_data = base64.b64decode(input_base64)
        np_image = np.frombuffer(input_image_data, np.uint8)
        image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        results = yolo_model(image)

        tags = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = yolo_model.names[int(box.cls)]
                probability = f"{float(box.conf) * 100:.2f}%"

                color = get_color_for_label(label)

                cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
                cv2.putText(image, f"{label} {probability}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                tags.append({
                    "label": label,
                    "probability": probability,
                    "X1": x1,
                    "Y1": y1,
                    "X2": x2,
                    "Y2": y2
                })

        _, output_image = cv2.imencode('.jpg', image)
        output_base64 = base64.b64encode(output_image).decode('utf-8')

        save_base64_to_image(output_base64, "output_image.jpg")

        response = {
            "OutputBase64": output_base64,
            "Tags": tags
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
