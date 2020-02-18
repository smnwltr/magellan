def app_data(request):
    data_dict = {
        'app_name': 'Magellan',
        'contact': {
            'support': 'smn@wltr.co',
            'phone': '+49 89 1234 5678',
            'street': 'Some street 51',
            'city': 'Munich',
            'country': 'Germany',
        },
        'static_links': {
            'privacy': '/privacy/',
            'imprint': '/imprint/'
        }
    }
    return data_dict
