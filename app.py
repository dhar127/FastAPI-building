from fastapi import FastAPI
app=FastAPI()
@app.get("/predict")
def check_username(username:str):
    if username==username[::-1]:
        return f"Congratulations {username}! You have a palindromic username!"
    else:
        return f"Hello {username}, your username is not a palindrome."

