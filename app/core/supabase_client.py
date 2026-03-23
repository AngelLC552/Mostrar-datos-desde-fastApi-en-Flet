from supabase import create_client, Client 
from app.core.config import config

def get_supabase()->Client:
    return create_Client(config.supabase_url, config.supasabe_key)

