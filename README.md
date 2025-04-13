# تطبيق التحكم في الموتور

تطبيق بسيط وسهل للتحكم في موتور عن طريق **ESP32** باستخدام **Kivy**. تقدر تشغّل الموتور، توقّفه، أو تظبّط سرعته من واجهة مريحة على موبايلك الأندرويد أو الكمبيوتر.

---

## نظرة سريعة على المشروع
التطبيق ده مقسّم لجزئين رئيسيين:
1. **تطبيق Kivy**: الواجهة اللي بتستخدمها عشان تتحكم، وهي شغالة على الأندرويد أو الكمبيوتر.
2. **كود ESP32**: الجزء اللي بيتحكم في الموتور فعليًا (لازم تنزّله على الـ ESP32 لوحده).

### ملفات المشروع
- `app.py`: القلب بتاع التطبيق، فيه كل المنطق والتحكم.
- `motor.kv`: تصميم الواجهة بتاعة التطبيق.
- `config.json`: إعدادات الاتصال بالـ ESP32.
- `buildozer.spec`: عشان تبني التطبيق للأندرويد.
- `requirements.txt`: قايمة المكتبات اللي التطبيق محتاجها.

---

## مميزات التطبيق
- واجهة سهلة ومريحة.
- تحكم في تشغيل/إيقاف الموتور بنقرة.
- ظبط سرعة الموتور زي ما تحب.
- اتصال مباشر مع الـ ESP32.
- يدعم اللغة العربية 100%.

---

## إيه اللي محتاجه عشان يشتغل؟

### لو بتشتغل على ويندوز
- Python 3.7 أو أحدث.
- Git.
- Visual Studio Code (يفضّل تستخدمه).
- Android Studio + Android SDK (لو عايز تبني تطبيق الأندرويد).

### لو على لينكس
- Python 3.7 أو أحدث.
- Git.
- Visual Studio Code (يفضّل).
- Android SDK.
- متطلبات buildozer للأندرويد:
  ```bash
  sudo apt-get install -y python3-pip build-essential git python3 python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
  ```

### المكتبات اللي لازم تتثبّت
- Kivy 2.3.1 (عشان الواجهة).
- Requests 2.31.0 (عشان الاتصال بالـ ESP32).
- buildozer 1.5.0 (عشان تبني تطبيق الأندرويد).

---

## إزاي تجهّز البيئة؟

1. **تثبيت Python**:
   - نزّل Python من [الموقع الرسمي](https://www.python.org/downloads/).
   - خلّي بالك تفعّل خيار "Add Python to PATH" وإنت بتثبّت.

2. **تجهيز المشروع**:
   ```bash
   # استنسخ المشروع
   git clone https://github.com/iui0/app.git
   cd app

   # اعمل بيئة افتراضية
   python -m venv venv

   # فعّل البيئة
   # على ويندوز:
   venv\Scripts\activate
   # على لينكس:
   source venv/bin/activate

   # نزّل المكتبات
   pip install -r requirements.txt
   ```

3. عدّل ملف `config.json` عشان تحط عنوان IP بتاع الـ ESP32.

---

## إزاي تشغّل التطبيق؟

### للتطوير
```bash
python app.py
```

### بناء تطبيق الأندرويد
1. تأكد إن buildozer متثبّت:
   ```bash
   pip install buildozer
   ```

2. لو ملف `buildozer.spec` مش موجود، اعمله:
   ```bash
   buildozer init
   ```

3. ابني التطبيق:
   ```bash
   buildozer android debug deploy run
   ```

---

## لو حصلت مشكلة؟
- **مشكلة اتصال بالـ ESP32**:
  - تأكد إن الـ ESP32 على نفس الشبكة.
  - شوف إن عنوان IP في `config.json` صح.
  - جرب المنفذ بتاع الـ ESP32 مفتوح وشغال.

- **مشاكل تطبيق الأندرويد**:
  - تأكد إن Android SDK متثبّت.
  - بص على سجلات البناء في `~/.buildozer/`.

---

## هيكل الكود
- **`app.py`**:
  ```python
  class MotorControl:  # الكلاس الرئيسي
      def __init__      # تهيئة التطبيق
      def setup_ui     # إعداد الواجهة
      def turn_on      # تشغيل الموتور
      def turn_off     # إيقاف الموتور
      def set_speed    # ظبط السرعة
  ```

- **`motor.kv`**:
  ```kivy
  <MotorControl>:     # تصميم الواجهة
      # أزرار التحكم
      # شريط السرعة
      # حالة الاتصال
  ```

---

## إعدادات التطبيق
في ملف `config.json` تقدر تعدل:
- `esp32_ip`: عنوان IP بتاع الـ ESP32.
- `esp32_port`: المنفذ (الافتراضي: 80).
- `connection_timeout`: مهلة الاتصال بالثواني.

---

## عايز تساهم معانا؟
يا ريت، التيم بيحب المساهمات!  اتّبع الخطوات دي:

### خطوات المساهمة
1. اعمل فرع جديد للميزة اللي عايز تضيفها:
   ```bash
   git checkout -b feature/اسم-الميزة
   ```

2. خلّيك ماشي مع قواعد الكود:
   - اكتب تعليقات بالعربي عشان الكل يفهم.
   - اتّبع نمط PEP 8 لكود Python.
   - وثّق أي تغييرات في الـ API.

3. اختبر التغييرات:
   - تأكد إن كل حاجة شغالة.
   - جرب على ويندوز ولينكس.
   - لو التغييرات ليها علاقة بالواجهة، اختبرها على الأندرويد.

4. اعمل Commit وPush:
   ```bash
   git add .
   git commit -m "وصف التغييرات"
   git push origin feature/اسم-الميزة
   ```

---

## وداعــــــــــــــــــــــــــــــــــــــــــــــا
# TEAM AZ 
---

