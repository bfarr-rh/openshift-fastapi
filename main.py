from fastapi import FastAPI
import uvicorn

app = FastAPI()

def get_arg(env, default):
    return os.getenv(env) if os.getenv(env, '') is not '' else default
    
@app.get('/')
def index():
    return {'data': 'Hello FastAPI!'}

@app.get('/message')
def index():
    if get_arg('verson','') == 'v1'
        return {'data': 'FastAPI v1 is great!'}
    else
        return {'data': 'FastAPI v2 is better!'}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
