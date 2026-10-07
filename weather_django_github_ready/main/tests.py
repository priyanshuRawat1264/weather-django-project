from unittest.mock import Mock, patch

from django.test import TestCase

from .models import SearchHistory


class WeatherViewTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Weather App')

    def test_empty_city_shows_validation_message(self):
        response = self.client.post('/', {'city': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a city name.')

    @patch('main.views.API_KEY', 'test-api-key')
    @patch('main.views.requests.get')
    def test_successful_weather_search_is_saved(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            'name': 'New Delhi',
            'sys': {'country': 'IN'},
            'main': {'temp': 28.5, 'humidity': 58, 'pressure': 1008},
            'weather': [{'description': 'clear sky', 'icon': '01d'}],
        }
        mock_get.return_value = mock_response

        response = self.client.post('/', {'city': 'New Delhi'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Delhi')
        self.assertEqual(SearchHistory.objects.count(), 1)
        self.assertEqual(SearchHistory.objects.first().city_name, 'New Delhi')
