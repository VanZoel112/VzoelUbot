# Ganti dengan API credentials Anda
api_id = 29919905
api_hash = "717957f0e3ae20a7db004d08b66bfd30"

# Generate session string
with Client("my_account", api_id=api_id, api_hash=api_hash) as app:
    print(f"Session String:\n{app.export_session_string()}")
