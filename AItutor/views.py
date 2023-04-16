from django.shortcuts import render, redirect
from .models import session
from json import dumps
import openai
openai.api_key = "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"

messages = [{"role": "system", "content": "You are a AI tutor."}]

sections = ["Intro to ML training in ML","Steps in Training in ML","Data Collection in ML","Preprocessing in ML","Training in ML", "Evaluation in ML" ]

validation= [{"role": "system", "content": "You answer with either 0 or 1 only."}]

def get_response(inp):
    global messages
    messages.append(inp),
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        temperature=0
    )
    return completion.choices[0].message["content"]

def gen_prompt(s_name):
    clear(request="Hello")
    que = "Write a brief 200 word paragraph explaining "

    prompt = ""
    global messages
    match s_name:
        case "A":
            prompt += get_response(dict(role="user",content=que+sections[0]))
            messages = messages[:-1]
        case "B":
            prompt += get_response(dict(role="user",content=que+sections[1]))
            messages = messages[:-1]
        case "C":
            prompt += get_response(dict(role="user",content=que+sections[2]))
            messages = messages[:-1]
        case "D":
            prompt += get_response(dict(role="user",content=que+sections[3]))
            messages = messages[:-1]
        case "E":
            prompt += get_response(dict(role="user",content=que+sections[4]))
            messages = messages[:-1]
        case "F":
            prompt += get_response(dict(role="user",content=que+sections[5]))
            messages = messages[:-1]
        case _:
            prompt += "invalid section."
    message = session(role="assistant", content=prompt)
    message.save()

def gen_que_text(s_name):
    que = "Ask a moderate level 'yes' or 'no' question on "

    prompt = ""
    global messages
    match s_name:
        case "A":
            prompt += get_response(dict(role="user",content=que+sections[0]))
            messages = messages[:-1]
        case "B":
            prompt += get_response(dict(role="user",content=que+sections[1]))
            messages = messages[:-1]
        case "C":
            prompt += get_response(dict(role="user",content=que+sections[2]))
            messages = messages[:-1]
        case "D":
            prompt += get_response(dict(role="user",content=que+sections[3]))
            messages = messages[:-1]
        case "E":
            prompt += get_response(dict(role="user",content=que+sections[4]))
            messages = messages[:-1]
        case "F":
            prompt += get_response(dict(role="user",content=que+sections[5]))
            messages = messages[:-1]
        case _:
            prompt += "invalid section."
    message = session(role="assistant", content=prompt)
    message.save()

def evaluate():
    condition = " return either 0 or 1 only."
    que = messages[-1]["content"]
    x = dict(role="user", content="the right answer for "+que+condition)

    result = get_response(x)
    message = session(role="assistant", content=result)
    message.save()

def home(request):
    return render(request, 'home.html')

def learn(request):
    messages = session.objects.all()
    return render(request, 'learn.html', {'messages': messages})

def section_start(request, section_name):
    gen_prompt(section_name)
    gen_que_text(section_name)
    evaluate()
    messages = session.objects.all()
    return render(request,'learn.html', {'messages': messages})

def about(request):
    return render(request, 'about.html')

def send_message(request):
    content = request.POST.get('content')
    if content:
        message = session(role="user", content=content)
        message.save()
    inp = dict(role="user", content=content)
    resp = get_response(inp)
    inp = dict(role="assistant", content=resp)
    global messages
    messages.append(inp)
    if resp:
        message = session(role="assistant", content=resp)
        message.save()
    return redirect('learn')

def clear(request):
    texts = session.objects.all()
    texts.delete()
    global messages
    messages = [{"role": "system", "content": "You are a AI tutor."}]
    return redirect('learn')
