from django.shortcuts import render, redirect
import requests
import json
import hashlib
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['passw']
        requestJSON = {}
        requestJSON["action"] = "loginUser"
        requestJSON["email"] = email
        requestJSON["passw"] = passw
        print(requestJSON)
        r = requests.post("http://127.0.0.1:8000/login/", data = json.dumps(requestJSON), headers={"Contect-Type":"application/json"})
        print(r)
        resultCode = r.json()["resultCode"]
        resultMessage = r.json()["resultMessage"]
        data = r.json()["data"]
        print(resultMessage)

        if resultCode ==200:
            return redirect('/dashh')
        context = {
            "resultMessage": resultMessage
            }
        return render(request, "index.html", context )
    return render(request, "index.html")


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        passw = request.POST['passw']
        requestJSON={}
        requestJSON["action"] = "registerUser"
        requestJSON["fname"] = fname
        requestJSON["lname"] = lname
        requestJSON["email"] = email
        requestJSON["passw"] = hashlib.md5(hashlib.md5(passw.encode("utf-8")).hexdigest().encode("utf-8")).hexdigest()
        print(requestJSON)
        r = requests.post("http://127.0.0.1:8000/register/", data = json.dumps(requestJSON), headers={"Contect-Type":"application/json"})
      
        resultCode = r.json()["resultCode"]
        resultMessage = r.json()["resultMessage"]
        data = r.json()["data"]
        print(data)

        if resultCode == 200:
            return redirect('/')
        context={
            "resultMessage": resultMessage,
            "fname":fname,
            "lname":lname,
            "email":email}
        return render(request, "register.html", context)
    return render(request,"register.html")


def dashboard(request):
    return render(request, "dashh.html")