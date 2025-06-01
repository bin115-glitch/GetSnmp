import mysql.connector
import json

def import_json_to_oid(json_file, power_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",  # Thay đổi nếu cần
        database="power"
    )
    cursor = connection.cursor()
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        for key, value in data.items():
            name = value["name"]
            value_key = value["oid"]
            value_type = value.get("valueType", "String")
            cursor.execute(
                "INSERT INTO oid (name, value_key, value_type, power_id) VALUES (%s, %s, %s, %s)",
                (name, value_key, value_type, power_id)
            )
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Imported {json_file} with power_id={power_id}")

# Import Delta (power_id=1)
import_json_to_oid("src/oid_Delta.json", 1)

# Import Enatel (power_id=2)
import_json_to_oid("src/oid_Enatel.json", 2)