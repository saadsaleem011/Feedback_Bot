# Analysis APIs

This project provides an API to analyze apartment data and generate insights using the Cohere AI platform. It allows users to upload a JSON file containing apartment details and request feedback or analysis based on various criteria.

---

## Features

- **Upload JSON file**: Upload apartment data for analysis.
- **Generate Insights**: Get feedback for:
  - The top unit based on features and details.
  - Units with significant price decreases.
  - Best building deals in a specific neighborhood.
- **AI-powered feedback**: Uses Cohere's AI model to provide detailed insights.

---

## Prerequisites

1. Python 3.10
2. Django framework installed
3. Cohere API Key (required to connect to the Cohere platform)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Cohere API key to the Django settings:
   ```python
   COHERE_API_KEY = '<your_cohere_api_key>'
   ```

4. Run the Django server:
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### 1. **Upload File**
   **URL**: `/upload_file/`  
   **Method**: POST  
   **Description**: Upload a JSON file containing apartment data.

   **Request**:
   - File: A `.json` file containing apartment details.

   **Response**:
   - Success:
     ```json
     {
       "message": "File uploaded",
       "data": [<uploaded_data>]
     }
     ```
   - Error:
     ```json
     {
       "error": "No file found"
     }
     ```

---

### 2. **Top Unit**
   **URL**: `/top_unit/`  
   **Method**: GET  
   **Description**: Identify the best unit based on features and details.

   **Response**:
   ```json
   {
     "feedback": "<AI_generated_feedback>"
   }
   ```

---

### 3. **Unit Price History**
   **URL**: `/unit_price_history/`  
   **Method**: GET  
   **Description**: Highlight units with significant price decreases.

   **Response**:
   ```json
   {
     "feedback": "<AI_generated_feedback>"
   }
   ```

---

### 4. **Building Deals**
   **URL**: `/building_deals/`  
   **Method**: GET  
   **Description**: Identify the best building deals in a specific neighborhood.

   **Query Parameter**:
   - `neighborhood`: The neighborhood to analyze.

   **Response**:
   ```json
   {
     "feedback": "<AI_generated_feedback>"
   }
   ```

   **Error**:
   ```json
   {
     "error": "neighborhood parameter required"
   }
   ```

---

## Example JSON Format

Below is an example of the JSON file structure expected by the API:

```json
[
  {
    "unit_id": 1,
    "name": "Apartment Name",
    "address": "123 Main St",
    "city": "Chicago",
    "description": "Beautiful apartment with modern amenities.",
    "neighborhood": "Downtown",
    "parking": "Yes",
    "washer_dryer": "Yes",
    "balcony": "Yes",
    "pet_policy": "Allowed with fee"
  },
  ...
]
```

---

## Dependencies

- **Django**: Web framework used to create the API.
- **Cohere Python SDK**: Connects to the Cohere platform to generate insights.

---

## Error Handling

- Returns `400 Bad Request` for:
  - Missing JSON file in the upload.
  - Missing required query parameters in endpoints.
  - Invalid or corrupted JSON file format.



## License

This project is licensed under the [MIT License](LICENSE).

---
