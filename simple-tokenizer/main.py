import tiktoken;
encoder=tiktoken.encoding_for_model("gpt-4o")
text ="Hey there ! how are you doing today"
tokens=encoder.encode(text)
print("token generated for text : ",tokens);
decoded=encoder.decode(tokens);
print("decoded tokens says : ",decoded);