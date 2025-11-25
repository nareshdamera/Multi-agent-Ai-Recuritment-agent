# --- START OF FILE agents/base_agent.py ---

from typing import Dict, Any
import json
# from openai import OpenAI # No longer needed
import google.generativeai as genai
# import os # No longer needed for configuration

# ################################################################
# # EXTREME SECURITY WARNING:                                    #
# # Hardcoding API keys is insecure. Use a NEW, VALID key below. #
# # REVOKE the old key (AIzaSy...npJA) immediately.              #
# ################################################################

# --- Directly Hardcoded API Key (REPLACE THIS!!!) ---
HARDCODED_API_KEY = "AIzaSyCRPQ1gY51jmgL2fo1Hp69sE6uzQNKnpJA" # <<< PUT YOUR *NEW* VALID KEY HERE
# --------------------------------------------------

# --- Directly Hardcoded Model Name ---
HARDCODED_MODEL_NAME = "gemini-1.5-flash-latest" # Or "gemini-pro", etc.
# ------------------------------------


# Configure the Gemini client using the hardcoded key
IS_CONFIGURED_SUCCESSFULLY = False # Flag to track configuration status
try:
    if not HARDCODED_API_KEY or HARDCODED_API_KEY == "YOUR_NEW_VALID_API_KEY_HERE":
         raise ValueError("API Key is missing or still set to the placeholder value.")

    genai.configure(api_key=HARDCODED_API_KEY)
    print("✅ Gemini API configured successfully (using hardcoded key).")
    IS_CONFIGURED_SUCCESSFULLY = True # Set flag on success

except ValueError as e:
    print(f"❌ Configuration Error: {e}")
except Exception as e:
    # This might catch AuthenticationError if the key is invalid/revoked during configure itself
    print(f"❌ An unexpected error occurred during Gemini configuration (check API key validity): {e}")


class BaseAgent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions
        # Use the hardcoded model name directly
        self.model_name = HARDCODED_MODEL_NAME
        self.gemini_model = None # Initialize to None

        # Attempt to initialize the model only if configuration flag is True
        if IS_CONFIGURED_SUCCESSFULLY:
            try:
                # Directly attempt to create the model object
                self.gemini_model = genai.GenerativeModel(self.model_name)
                print(f"✅ Initialized Gemini model: {self.model_name}")

            except Exception as e:
                # Catches errors during GenerativeModel() call specifically
                # This is where errors often appear if the key is invalid/revoked
                # or lacks permissions for the model.
                print(f"❌ Failed to initialize Gemini model '{self.model_name}' (check API key validity/permissions): {e}")
                # self.gemini_model remains None
        else:
             print(f"⚠️ Skipping Gemini model initialization because configuration failed earlier.")


    async def run(self, messages: list) -> Dict[str, Any]:
        """Default run method to be overridden by child classes"""
        raise NotImplementedError("Subclasses must implement run()")

    # Method name kept as _query_ollama for compatibility based on request
    def _query_ollama(self, prompt: str) -> str:
        """
        Query the configured Google Gemini model with the given prompt.
        """
        if not self.gemini_model:
            print("❌ Gemini model was not initialized successfully in __init__. Cannot query.")
            return json.dumps({"error": "Gemini model not initialized"})

        full_prompt = f"{self.instructions}\n\n---\n\nUser Prompt:\n{prompt}"

        try:
            print(f"🤖 Querying Gemini model {self.model_name}...")
            generation_config = genai.types.GenerationConfig(
                temperature=0.7,
                max_output_tokens=2500
            )

            response = self.gemini_model.generate_content(
                full_prompt,
                generation_config=generation_config,
                )

            # --- Handling Gemini Response ---
            if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
                 content = response.candidates[0].content.parts[0].text
                 print(f"✅ Gemini Response Received (length: {len(content)})")
                 return content
            elif response.prompt_feedback and response.prompt_feedback.block_reason:
                 block_reason = response.prompt_feedback.block_reason
                 print(f"⚠️ Gemini Response Blocked: {block_reason}")
                 return json.dumps({"error": f"Content blocked by API safety settings: {block_reason}"})
            else:
                 print("⚠️ Gemini response structure unexpected or empty.")
                 try:
                     content = response.text # Fallback attempt
                     print(f"✅ Gemini Response Received (fallback, length: {len(content)})")
                     return content
                 except AttributeError:
                     print("❌ Could not extract text from Gemini response.")
                     return json.dumps({"error": "Could not extract text from Gemini response"})

        except Exception as e:
            # This might catch google.api_core.exceptions.PermissionDenied if key is bad
            print(f"❌ Error querying Gemini API (check API key validity/permissions): {str(e)}")
            # import traceback
            # print(traceback.format_exc()) # Uncomment for detailed traceback
            return json.dumps({"error": f"Gemini API query failed: {str(e)}"})

    def _parse_json_safely(self, text: str) -> Dict[str, Any]:
        """
        Safely parse JSON from text, handling potential errors and cleaning.
        """
        try:
            text = text.strip()
            if text.startswith("```json"):
                text = text[7:]
            elif text.startswith("```"):
                 text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()

            start = text.find("{")
            end = text.rfind("}")
            if start != -1 and end != -1 and end > start:
                json_str = text[start : end + 1]
                parsed = json.loads(json_str)
                print("✅ Successfully parsed JSON")
                return parsed
            else:
                 print("⚠️ No JSON object markers ({}) found in the response.")
                 return {"error": "No JSON object found in response", "raw_response": text}

        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON content: {e}")
            return {"error": f"Invalid JSON content: {e}", "raw_response": text}
        except Exception as e:
            print(f"❌ Unexpected error during JSON parsing: {e}")
            return {"error": f"Unexpected parsing error: {e}", "raw_response": text}

# --- END OF FILE agents/base_agent.py ---





# from typing import Dict, Any
# import json
# from openai import OpenAI


# class BaseAgent:
#     def __init__(self, name: str, instructions: str):
#         self.name = name
#         self.instructions = instructions
#         self.ollama_client = OpenAI(
#             base_url="http://localhost:11434/v1",
#             api_key="ollama",  # required but unused
#         )

#     async def run(self, messages: list) -> Dict[str, Any]:
#         """Default run method to be overridden by child classes"""
#         raise NotImplementedError("Subclasses must implement run()")

#     def _query_ollama(self, prompt: str) -> str:
#         """Query Ollama model with the given prompt"""
#         try:
#             response = self.ollama_client.chat.completions.create(
#                 model="llama3.2",  # Updated to llama3.2
#                 messages=[
#                     {"role": "system", "content": self.instructions},
#                     {"role": "user", "content": prompt},
#                 ],
#                 temperature=0.7,
#                 max_tokens=2000,
#             )
#             return response.choices[0].message.content
#         except Exception as e:
#             print(f"Error querying Ollama: {str(e)}")
#             raise

#     def _parse_json_safely(self, text: str) -> Dict[str, Any]:
#         """Safely parse JSON from text, handling potential errors"""
#         try:
#             # Try to find JSON-like content between curly braces
#             start = text.find("{")
#             end = text.rfind("}")
#             if start != -1 and end != -1:
#                 json_str = text[start : end + 1]
#                 return json.loads(json_str)
#             return {"error": "No JSON content found"}
#         except json.JSONDecodeError:
#             return {"error": "Invalid JSON content"}