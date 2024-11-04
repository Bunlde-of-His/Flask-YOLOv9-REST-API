# Flask YOLOv9 REST API

This project is a REST API built using Flask that performs image detection using the YOLOv9 model.

## Prerequisites
- Python 3.8+
- Git
- Virtual Environment 

## Installation

### Step 1: Clone the Repository
```
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Set up a Virtual Environment 
On Ubuntu:
```
python3 -m venv venv
source venv/bin/activate
```

On Windows:
```
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```
pip install -r requirements.txt
```

### Step 4: Download YOLOv9 Model Weights
The application automatically downloads the YOLOv9 weights (`yolov9c.pt`) when it runs for the first time. 

### Step 5: Run the Application
```
python main.py
```
The API will be available at `http://localhost:5000`.

## Testing the API

### Endpoint: `/login`
- **Method**: POST
- **Auth**: Basic Authentication
  - **Username**: `admin`
  - **Password**: `password`
- **Response**: `{ "message": "Login successful" }`

### Endpoint: `/detect`
- **Method**: POST
- **Auth**: Basic Authentication
  - **Username**: `admin`
  - **Password**: `password`
- **Request Body**: JSON
  ```json
  {
    "InputBase64": "<base64-encoded JPEG image>"
  }
  ```
- **Response**: JSON with annotated image in base64 and detected object tags.

## Output Image
The application will create an output image (`output_image.jpg`) with all detected objects marked with bounding boxes, labels, and detection accuracy percentages.

## Notes
- You may use [Postman](https://www.postman.com/) or `curl` for testing the endpoints.
- Install any missing dependencies that may be required during the process.