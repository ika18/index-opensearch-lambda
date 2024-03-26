from typing import Any


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
