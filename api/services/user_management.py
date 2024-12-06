from atproto import Client, models
from api.config import config

def add_user_to_list(did, list_uri):
    client = Client()
    try:
        client.login(config.HANDLE, config.PASSWORD)
        add_item = client.app.bsky.graph.list.add_item(
            models.AppBskyGraphListAddItem.Data(
                list=list_uri,
                item=models.AppBskyGraphListItem.Main(
                    subject=did,
                    created_at=client.get_current_time_iso()
                )
            )
        )
        return f"User {did} added to list: {list_uri}"
    except Exception as e:
        return f"Error adding user {did} to list: {str(e)}"
