from django.shortcuts import render, redirect
from Face_Detection.detection import FaceRecognition
from .forms import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
faceRecognition = FaceRecognition()


def home(request):
    return render(request, 'faceDetection/home.html')

def userNotFound(request):
    return render(request, 'faceDetection/userNotFound.html')


def register(request):
    if request.method == "POST":
        form = ResgistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("IN HERE")
            messages.success(request, "SuccessFully registered")
            addFace(request.POST['face_id'])
            messageSend = "SuccessFully registered"
            # msg = 1
            data = {
                'message' : messageSend
            }
            return render(request, 'faceDetection/home.html', context=data)

        else:
            messages.error(request, "Account registered failed")
    else:
        form = ResgistrationForm()

    return render(request, 'faceDetection/register.html', {'form': form})


def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('home')


def login(request):
    face_id = faceRecognition.recognizeFace()
    if (face_id!= 0):
        print(face_id)
        return redirect('dashboard', str(face_id))
    else:
        print("face not found!!!")


def dashboard(request, face_id):
    try:
        face_id = int(face_id)
        print(face_id)

        data = {
            'user': UserProfile.objects.get(face_id=face_id)
        }
        return render(request, 'faceDetection/profile.html', context=data)
    except ObjectDoesNotExist:
        return redirect('userNotFound')

def logout(request):
    messageSend = "Successfully logout"
    data = {
                'messageLogout' : messageSend
            }
    return redirect('home', data)
    # return render(request, 'faceDetection/home.html', context=data)


        