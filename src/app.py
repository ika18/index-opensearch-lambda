import json
from utils import file, reader, opensearch
import os
from typing import Any

port = int(os.environ.get("OPENSEARCH_PORT"))
host = os.environ.get("OPENSEARCH_HOST")
auth = (os.environ.get("OPENSEARCH_USERNAME"), os.environ.get("OPENSEARCH_PASSWORD"))


def convert_apps_to_documents(apps: dict[str, Any]) -> list[dict[str, Any]]:
    documents = []

    for app in apps:
        documents.append(
            {
                "id": int(app["@id"]),
                "base_vehicle_id": int(app["BaseVehicle"]["@id"]),
                "qty": int(app["Qty"]),
                "part_type_id": int(app["PartType"]["@id"]),
                "mfr_label": app["MfrLabel"],
                "position_id": int(app["Position"]["@id"]),
                "part": app["Part"],
            }
        )

    return documents


def lambda_handler(event, context):
    opensearch_client = opensearch.OpenSearchClient(host, port, auth)

    str = file.get_file_from_event(event)

    xml_reader = reader.XmlReader(str)

    apps = xml_reader.get_apps()

    apps_documents = convert_apps_to_documents(apps)

    opensearch_client.bulk_documents(apps_documents)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "success",
            }
        ),
    }
