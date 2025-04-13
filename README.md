# تطبيق التحكم في الموتور

تطبيق للتحكم في موتور عبر ESP32 باستخدام Kivy. يتيح هذا التطبيق التحكم في تشغيل وإيقاف وضبط سرعة الموتور عن طريق واجهة رسومية سهلة الاستخدام.

## نظرة عامة على المشروع
هذا المشروع يتكون من جزئين رئيسيين:
1. **تطبيق Kivy**: واجهة مستخدم رسومية تعمل على الأندرويد والكمبيوتر
2. **برنامج ESP32**: يتحكم في الموتور مباشرة (يجب تثبيته على جهاز ESP32 بشكل منفصل)

### هيكل المشروع
* `app.py` - الملف الرئيسي للتطبيق، يحتوي على منطق التطبيق والتحكم
* `motor.kv` - ملف تصميم واجهة المستخدم بلغة Kivy
* `config.json` - ملف الإعدادات للاتصال بـ ESP32
* `buildozer.spec` - ملف إعدادات بناء تطبيق الأندرويد
* `requirements.txt` - قائمة المكتبات المطلوبة

## المميزات الرئيسية
* واجهة مستخدم سهلة الاستخدام
* التحكم في تشغيل/إيقاف الموتور
* التحكم في سرعة الموتور
* اتصال مباشر مع ESP32
* دعم كامل للغة العربية

## متطلبات التشغيل

### للتطوير على نظام ويندوز
* Python 3.7+
* Git
* Visual Studio Code (موصى به)
* Android Studio + Android SDK (لتطوير تطبيق الأندرويد)

### للتطوير على نظام لينكس
* Python 3.7+
* Git
* Visual Studio Code (موصى به)
* Android SDK
* buildozer متطلبات (للأندرويد):
  ```
  sudo apt-get install -y python3-pip build-essential git python3 python3-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev
  ```

### المكتبات المطلوبة
* Kivy 2.3.1 - لواجهة المستخدم
* Requests 2.31.0 - للاتصال بـ ESP32
* buildozer 1.5.0 - لبناء تطبيق الأندرويد

## إعداد بيئة التطوير

1. تثبيت Python:
   * قم بتحميل Python من [الموقع الرسمي](https://www.python.org/downloads/)
   * تأكد من تفعيل خيار "Add Python to PATH" أثناء التثبيت

2. تجهيز المشروع:

1. قم بتثبيت المتطلبات:
```
pip install -r requirements.txt
```

2. إعداد المشروع:   ```bash
   # استنساخ المشروع
   git clone https://github.com/iui0/app.git
   cd app

   # إنشاء بيئة Python افتراضية
   python -m venv venv
   
   # تفعيل البيئة الافتراضية
   # على ويندوز:
   venv\Scripts\activate
   # على لينكس:
   source venv/bin/activate

   # تثبيت المتطلبات
   pip install -r requirements.txt
   ```

3. قم بتعديل ملف config.json لتحديد عنوان IP الخاص بـ ESP32.

## التشغيل والتطوير

### تشغيل التطبيق للتطوير
```bash
python app.py
```

### بناء تطبيق الأندرويد
1. تأكد من تثبيت buildozer:
   ```bash
   pip install buildozer
   ```

2. قم بإنشاء ملف buildozer.spec (إذا لم يكن موجوداً):
   ```bash
   buildozer init
   ```

3. قم ببناء التطبيق:
   ```bash
   buildozer android debug deploy run
   ```

### تصحيح الأخطاء
- إذا واجهت مشكلة في الاتصال بـ ESP32، تأكد من:
  1. أن ESP32 متصل بنفس الشبكة
  2. عنوان IP في config.json صحيح
  3. منفذ ESP32 مفتوح ويعمل

- لمشاكل تطبيق الأندرويد:
  1. تأكد من تثبيت Android SDK
  2. راجع سجلات البناء في ~/.buildozer/

## هيكل الكود وتنظيمه
- `app.py`:
  ```python
  class MotorControl:  # الفئة الرئيسية للتطبيق
    def __init__       # تهيئة التطبيق
    def setup_ui      # إعداد واجهة المستخدم
    def turn_on       # تشغيل الموتور
    def turn_off      # إيقاف الموتور
    def set_speed     # ضبط السرعة
  ```

- `motor.kv`:
  ```kivy
  <MotorControl>:     # تصميم واجهة المستخدم
    # أزرار التحكم
    # شريط تمرير السرعة
    # حالة الاتصال
  ```

## الإعدادات
يمكنك تعديل إعدادات الاتصال في ملف `config.json`:
* `esp32_ip`: عنوان IP الخاص بـ ESP32
* `esp32_port`: المنفذ المستخدم (الافتراضي: 80)
* `connection_timeout`: مهلة الاتصال بالثواني

## المساهمة في المشروع
نرحب بمساهمات الفريق! إليك الخطوات:

### خطوات المساهمة
1. قم بإنشاء فرع (branch) جديد للميزة التي تريد إضافتها:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. اتبع معايير كتابة الكود:
   - استخدم التعليقات باللغة العربية لشرح الكود
   - اتبع نمط PEP 8 لكود Python
   - قم بتوثيق أي تغييرات في الـ API

3. اختبر التغييرات:
   - تأكد من عمل جميع الوظائف
   - اختبر على نظامي التشغيل ويندوز ولينكس
   - اختبر على الأندرويد إذا كانت التغييرات تؤثر على واجهة المستخدم

4. قم بعمل Commit وPush:
   ```bash
   git add .
   git commit -m "وصف التغييرات"
   git push origin feature/your-feature-name
   ```

### النسخ الاحتياطي والتوثيق
- يتم حفظ نسخ احتياطية يومياً على السيرفر المحلي
- التوثيق الفني الكامل متوفر في مجلد `docs/`
- أي تغييرات في الـ API يجب توثيقها في `API.md`

## الدعم والمساعدة
- للمساعدة التقنية: راجع [قسم Discussions](https://github.com/iui0/app/discussions)
- لتقارير الأخطاء: استخدم [قسم Issues](https://github.com/iui0/app/issues)
- للتواصل مع المشرف: عبر [صفحة المشروع](https://github.com/iui0/app)

## الرخصة
هذا المشروع مرخص تحت رخصة MIT.
