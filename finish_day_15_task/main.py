
import requests
import pandas as pd

try:
    # 1. Read data from a public API
    url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(url, timeout=10)

    # 2. Check if the request was successful
    response.raise_for_status()

    data = response.json()

    # 3. Validate the input
    if not isinstance(data, list):
        raise ValueError("The data must be a list.")

    if len(data) == 0:
        raise ValueError("The data is empty.")

    # 4. Extract relevant fields
    rows = []

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("An item is not a dictionary.")

        if not all(key in item for key in
                   ["userId", "id", "title", "completed"]):
            raise ValueError("A required field is missing.")

        rows.append({
            "userId": item["userId"],
            "id": item["id"],
            "title": item["title"],
            "completed": item["completed"]
        })

    # 5. Convert data into a DataFrame
    df = pd.DataFrame(rows)

    # 6. Save the data as a CSV file
    df.to_csv("todos.csv", index=False)

    print("Success! Data saved to todos.csv")
    print(df.head())

except requests.exceptions.RequestException as error:
    print("API connection error:", error)

except (ValueError, TypeError) as error:
    print("Data validation error:", error)

except (OSError, IOError) as error:
    print("File error:", error)
