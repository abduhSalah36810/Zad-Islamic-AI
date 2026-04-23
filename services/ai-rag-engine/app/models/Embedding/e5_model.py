from sentence_transformers import SentenceTransformer
from .base import EmbeddingModel

class E5_Embedding_Model(EmbeddingModel) : 
   def __init__(self , model_name = "intfloat/multilingual-e5-large" ) :
      self.model = SentenceTransformer(model_name)
   def embed_documents(self, texts): 
      texts = [f"passage : {t}" for t in texts]
      return self.model.encode(texts , normalize_embeddings=True).tolist()
   def embed_query(self, query):
      query = f"query : {query}"
      return self.model.encode(query , normalize_embeddings=True).tolist()
       
