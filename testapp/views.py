from django.shortcuts import render, redirect

from django.views import View

from django.http.response import JsonResponse
from django.template.loader import render_to_string

from .models import Topic
from .forms import TopicForm,TopicImageForm


class IndexView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"testapp/index.html",context)

    def post(self, request, *args, **kwargs):

        data    = { "error":True }
        form    = TopicForm(request.POST)

        #ここでコメントを保存
        if not form.is_valid():
            print(form.errors)
            print("Validation Error")
            return JsonResponse(data)

        topic   = form.save()


        #ここで複数指定した画像を追記。
        images  = request.FILES.getlist("image")
        print(images)

        for image in images:

            upload_image_file   = { "image":image }
            upload_image_name   = { "topic":topic.id,"image":str(image) }

            form    = TopicImageForm(upload_image_name,upload_image_file)

            if form.is_valid():
                print("バリデーションOK")
                form.save()
            else:
                print("バリデーションNG")
                print(form.errors)

        context             = {}
        context["topics"]   = Topic.objects.all()

        data["error"]       = False
        data["content"]     = render_to_string("testapp/content.html",context,request)

        return redirect('/')

index   = IndexView.as_view()




class IndexViewAjax(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"testapp/index_ajax.html",context)

    def post(self, request, *args, **kwargs):

        data    = { "error":True }
        form    = TopicForm(request.POST)

        #ここでコメントを保存
        if not form.is_valid():
            print("Validation Error")
            return JsonResponse(data)

        topic   = form.save()


        #ここで複数指定した画像を追記。
        images  = request.FILES.getlist("image")

        for image in images:

            upload_image_file   = { "image":image }
            upload_image_name   = { "topic":topic.id,"image":str(image) }

            form    = TopicImageForm(upload_image_name,upload_image_file)

            if form.is_valid():
                print("バリデーションOK")
                form.save()
            else:
                print("バリデーションNG")
                print(form.errors)

        context             = {}
        context["topics"]   = Topic.objects.all()

        data["error"]       = False
        data["content"]     = render_to_string("testapp/content.html",context,request)

        return JsonResponse(data)

index_ajax   = IndexViewAjax.as_view()


def editorjs_plugin(request):
    
    contents = {
    }
    return render(request, 'testapp/editorjs_plugin.html', contents)
