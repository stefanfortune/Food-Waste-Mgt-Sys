import os
import google.generativeai as genai


def create_chatbot():
  # 1. Configuration
  #genai.configure(api_key=os.getenv("AIzaSyCzCdZUrHBtTjlj8yPB_K1LRC5wPB-CY9c"))
  genai.configure(api_key='AIzaSyCzCdZUrHBtTjlj8yPB_K1LRC5wPB-CY9c')
  genaration_config ={"temperature": 0.9, "top_p":1, "max_output_tokens": 2048}
  # 2. Initialise Model
  model = genai.GenerativeModel("gemini-pro", generation_config=genaration_config)

  #3. Generate content  
  response = model.generate_content(["how do i store beans"])
  print(response.text)

#if __name__ == "__main__":
create_chatbot()
