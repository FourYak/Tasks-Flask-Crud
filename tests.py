import pytest
import requests

# CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

# Create - Test
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])  # Armazenar o ID da tarefa criada

# Read (all) - Test
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

# Read (by id) - Test
def test_get_task():
    if tasks: # Verifica se há tarefa criada
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]

# Update (by id) - Test
def test_update_task():
    if tasks: # Verifica se há tarefa criada
        task_id = tasks[0]
        payload = {
            "title": "Tarefa atualizada",
            "description": "Descrição atualizada da tarefa",
            "completed": True
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # Nova requisição a tarefa especifica
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['title'] == payload['title']
        assert response_json['description'] == payload['description']
        assert response_json['completed'] == payload['completed']

# Delete (by id) - Test
def test_delete_task():
    if tasks: # Verifica se há tarefa criada
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # Verifica se a tarefa foi realmente deletada
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404