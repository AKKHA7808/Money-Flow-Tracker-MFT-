# ตัวอย่างการตั้งค่า Supabase Client สำหรับ Django
from supabase import create_client, Client

SUPABASE_URL = "https://nmtghnuxzgabgwwusfqo.supabase.co"  # Project URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5tdGdobnV4emdhYmd3d3VzZnFvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTcwNzc2NTQsImV4cCI6MjA3MjY1MzY1NH0.1eEX90-T_z7-DCao6rhPaNRGjC2No6yuBsec0YCfefg"  # API Key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
