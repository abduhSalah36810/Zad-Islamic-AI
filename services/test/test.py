# from app.models.Embedding.factory import get_embedding_model

# model = get_embedding_model()

# q1 = "ما حكم الصلاة بدون وضوء؟"
# q2 = "هل يجوز الصلاة بلا طهارة؟"

# v1 = model.embed_query(q1)
# v2 = model.embed_query(q2)

# # لازم similarity تكون عالية

# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# # الموديل بيخرج Vectors، لازم نحولهم لـ 2D Array عشان sklearn تفهمهم
# # [v1] يعني بنخليها صف واحد
# sim = cosine_similarity([v1], [v2])[0][0]

# print(f"Similarity Score: {sim:.4f}")

# if sim > 0.85:
#     print("الجملتان تعطيان نفس المعنى تقريباً (High Similarity)")
# else:
#     print("الجملتان مختلفتان في المعنى")

import torch
from sentence_transformers import SentenceTransformer, util
import os

# 1. إعداد الأسئلة (نفس المعنى بكلمات مختلفة)
queries = [
    ("ما حكم الصلاة بدون وضوء؟", "هل تصح الصلاة بلا طهارة؟"),
    ("كيفية إخراج زكاة المال؟", "ما هو مقدار النصاب في الزكاة؟"), # جملتين مرتبطين بس مش متطابقين
    ("متى يبدأ وقت صلاة الفجر؟", "طريقة عمل البيتزا بالخضروات") # جملتين ملهومش علاقة ببعض تماماً
]

def check_consistency(paths):
    for q_pair in queries:
        print(f"\nالأسئلة: '{q_pair[0]}' VS '{q_pair[1]}'")
        print("-" * 50)
        
        results = {}
        for name, path in paths.items():
            if not os.path.exists(path):
                print(f"⚠️ الموديل {name} غير موجود في المسار المحدد.")
                continue
                
            model = SentenceTransformer(path)
            
            # إضافة الـ prefix الخاص بـ E5 لضمان أدق نتيجة
            emb1 = model.encode(f"query: {q_pair[0]}", convert_to_tensor=True)
            emb2 = model.encode(f"query: {q_pair[1]}", convert_to_tensor=True)
            
            # حساب الـ Cosine Similarity
            cosine_sim = util.cos_sim(emb1, emb2).item()
            results[name] = cosine_sim
            print(f"[{name}] Similarity: {cosine_sim:.4f}")

        # تحليل الفرق بين الموديلين
        if len(results) == 2:
            diff = abs(results["E5-Large"] - results["E5-Small"])
            print(f"💡 الفرق في التقدير (Difference): {diff:.4f}")
            if diff < 0.05:
                print("✅ النتيجة متسقة جداً (Highly Consistent)")
            else:
                print("⚠️ يوجد فرق بسيط في تقدير المعنى.")

# المسارات المحلية
model_paths = {
    "E5-Large": "./app/models/weights/e5-large",
    "E5-Small": "./app/models/weights/e5-small"
}

check_consistency(model_paths)