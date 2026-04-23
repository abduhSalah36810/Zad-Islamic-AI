from abc import ABC , abstractmethod 
from typing import List

class EmbeddingModel (ABC) : 
      @abstractmethod 
      def embed_documents(self , texts : List[str] ) -> List[List[str]]:
        pass
      @abstractmethod
      def embed_query(self , query : List[str]) -> List[float] : 
          pass