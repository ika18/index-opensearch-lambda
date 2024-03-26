from typing import Any
from opensearchpy import OpenSearch, helpers


class OpenSearchClient:
    _client: OpenSearch

    def __init__(self, host: str, port: int, auth: tuple[str, str]) -> None:
        self._client = OpenSearch(
            hosts=[{"host": host, "port": port}],
            http_compress=True,  # enables gzip compression for request bodies
            http_auth=auth,
            use_ssl=True,
            verify_certs=True,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )

    def search(self):
        query = {
            "query": {"match_all": {}},
        }

        response = self._client.search(
            body=query,
            index="apps",
        )

        return response

    def index_document(self, id: int, document: dict[str, Any]):
        response = self._client.index(
            index="apps",
            body=document,
            id=id,
            refresh=True,
        )
        return response

    def bulk_documents(self, sources: list[dict[str, Any]]):
        actions = [
            {"_index": "apps", "_id": source["id"], "_source": source}
            for source in sources
        ]
        current = 0
        while current < len(actions):
            helpers.bulk(client=self._client, actions=actions[current : current + 10])
            current += 10

    def delete_document(self, id: int):
        response = self._client.delete(index="apps", id=id)
        return response
