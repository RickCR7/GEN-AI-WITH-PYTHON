import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hey There! My name is Akash Sen"
tokens = enc.encode(text)

print("Tokens -> ", tokens)
# Tokens [25216, 3274, 0, 3673, 1308, 382, 13232, 1229, 8675]

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 13232, 1229, 8675])
print("Decoded -> ", decoded)
