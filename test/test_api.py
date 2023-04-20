import requests

# Define the base URL for the API
base_url = 'http://localhost:5000'

def test_high_scores():
    # Create a new high score
    data = {'name': 'Alice', 'score': 1000}
    response = requests.post(f'{base_url}/high_scores', json=data)
    assert response.status_code == 200

    response = requests.get(f'{base_url}/high_scores')
    assert response.status_code == 200
    high_scores = response.json()
    assert len(high_scores) == 4
    assert high_scores[0]['name'] == 'Alice'
    assert high_scores[0]['score'] == 1000
    assert high_scores[1]['name'] == 'Jane'
    assert high_scores[1]['score'] == 200
    assert high_scores[2]['name'] == 'John'
    assert high_scores[2]['score'] == 100
    assert high_scores[3]['name'] == 'Bob'
    assert high_scores[3]['score'] == 50

if __name__ == '__main__':
    test_high_scores()
