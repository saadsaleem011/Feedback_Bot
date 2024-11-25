import json
from feedback.settings import COHERE_API_KEY
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import cohere

co = cohere.Client(COHERE_API_KEY)


def create_prompt(data, analysis, neighborhood=None):
    if analysis == 'top_unit':
        prompt = "Evaluate the given units and identify the best one based on their features and details. Provide a concise explanation:"
    elif analysis == 'unit_price_history':
        prompt = "Review the units and highlight those with the largest price decreases. Focus only on the key units:"
    elif analysis == 'building_deals':
        prompt = f"Assess the units in the {neighborhood} neighborhood and identify the best building deals. Keep the feedback precise and to the point:"
    else:
        prompt = "Analyze the following units based on their details and provide relevant insights:"

    for unit in data:
        unit_info = (
            f"Unit ID: {unit['unit_id']}\n"
            f"Name: {unit['name']}\n"
            f"Address: {unit['address']}\n"
            f"City: {unit['city']}\n"
            f"Description: {unit['description']}\n"
            f"Neighborhood: {unit['neighborhood']}\n"
            f"Parking: {unit['parking']}\n"
            f"Washer Dryer: {unit['washer_dryer']}\n"
            f"Balcony: {unit['balcony']}\n"
            f"Pet Policy: {unit['pet_policy']}\n\n"
        )

        prompt += unit_info
    return prompt


def data(prompt):
    try:
        response = co.generate(
            model='command-r-plus',
            prompt=prompt,
            max_tokens=250,
            temperature=0.4,
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"


def decode_json_data(json_data):
    try:
        return json.loads(json_data)
    except json.JSONDecodeError:
        return {'error': 'Invalid JSON format'}


@csrf_exempt
@require_http_methods(["POST"])
def upload_file(request):
    global uploaded_data
    if not request.FILES.get('file'):
        return JsonResponse({'error': 'No file found'}, status=400)

    file = request.FILES['file']
    if file.name.endswith('.json'):
        file_content = file.read().decode('utf-8')
        uploaded_data = decode_json_data(file_content)
        return JsonResponse({'message': 'File uploaded', 'data': uploaded_data})
    else:
        return JsonResponse({'error': 'Error in json file'}, status=400)


def top_unit(request):
    if not uploaded_data:
        return JsonResponse({'error': 'Data not found for analysis'}, status=400)
    prompt = create_prompt(uploaded_data, 'top_unit')
    feedback = data(prompt)
    return JsonResponse({'feedback': feedback})


def unit_price_history(request):
    if not uploaded_data:
        return JsonResponse({'error': 'Data not found for analysis'}, status=400)
    prompt = create_prompt(uploaded_data, 'unit_price_history')
    feedback = data(prompt)
    return JsonResponse({'feedback': feedback})


def building_deals(request):
    if not uploaded_data:
        return JsonResponse({'error': 'Data not found for analysis'}, status=400)
    neighborhood = request.GET.get('neighborhood')
    if not neighborhood:
        return JsonResponse({'error': 'neighborhood parameter required'}, status=400)
    prompt = create_prompt(uploaded_data, 'building_deals', neighborhood=neighborhood)
    feedback = data(prompt)
    return JsonResponse({'feedback': feedback})
