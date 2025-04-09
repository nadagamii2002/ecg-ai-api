from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import os




# إنشاء تطبيق Flask
app = Flask(__name__)

# تحميل نموذج H5 عند تشغيل الخادم
model = load_model('model/best_model.h5')
  # تأكد أن الملف موجود في هذا المسار

print("✅ هل يوجد النموذج؟", os.path.exists("model/best_model.h5"))

@app.route('/')
def home():
    return "✅ API قيد التشغيل!"

# نقطة استقبال البيانات
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # استلام البيانات بصيغة JSON
        data = request.get_json(force=True)
        ecg = data.get('ecg')  # يجب أن تحتوي على 187 قيمة

        # التحقق من صحة البيانات
        if not ecg or len(ecg) != 187:
            return jsonify({"error": "يجب إرسال 187 نقطة ECG"}), 400

        # تحويل البيانات إلى مصفوفة NumPy بالشكل المطلوب (1, 186, 1)
        input_data = np.array(ecg[:186]).reshape(1, 186, 1)

        # التنبؤ
        prediction = model.predict(input_data)
        predicted_class = int(np.argmax(prediction))

        # الرد بالنتائج
        return jsonify({
            "predicted_class": predicted_class,
            "confidence": prediction[0].tolist()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
