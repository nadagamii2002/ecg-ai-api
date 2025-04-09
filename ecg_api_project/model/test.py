import requests
import json

# 🔗 رابط الخادم (غيّره حسب رابطك الحقيقي)
API_URL = "https://ecg-ai-api-1.onrender.com/predict"

# 🧪 مثال على بيانات ECG (قائمة بطول 187 أو 186 حسب النموذج)
sample_ecg_data = [0.123, 0.145, 0.166, ]  # كرر القيم أو أضف حتى 186 قيمة
  # ← ضَع 186 قيمة

# إرسال البيانات إلى الخادم
response = requests.post(API_URL, json={"ecg_data": sample_ecg_data})

# عرض النتيجة
if response.status_code == 200:
    result = response.json()
    print("✅ الاستجابة من الخادم:")
    print(result)
else:
    print(f"❌ خطأ: {response.status_code}")
    print(response.text)
