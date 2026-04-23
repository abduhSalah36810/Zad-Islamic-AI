from sentence_transformers import SentenceTransformer
import os

# 1. عرف اسم الموديل اللي انت لسه محمله
model_name = 'intfloat/multilingual-e5-large'

# 2. حدد المكان اللي عايز تحفظه فيه (مثلاً فولدر جوه مشروعك)
save_path = './app/models/weights/e5-large'

# تأكد إن الفولدر موجود
os.makedirs(save_path, exist_ok=True)

# 3. تحميل الموديل (هنا هيقراه من الـ Cache مش من النت لأنه موجود)
model = SentenceTransformer(model_name)

# 4. الحفظ النهائي في الفولدر بتاعك
model.save(save_path)

print(f"✅ تم حفظ الموديل بنجاح في: {save_path}")
print("دلوقتي تقدر تقفل النت وتستخدمه من المسار ده.")