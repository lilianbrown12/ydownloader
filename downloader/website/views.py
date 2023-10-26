from flask import Blueprint,request,render_template,redirect,url_for,flash,session
from pytube import YouTube
import werkzeug
import pytube 
import urllib
import pyttsx3


speak =pyttsx3.init()




views =Blueprint('views',__name__)

@views.route('/', methods=['GET','POST'])
def home():
    result = request.form
    
    if request.method == 'POST':
        result = request.form
        video_url = request.form.get('url')
       
       
        if video_url is not None:
            try:
                try:
                    youtube = YouTube(video_url)
                except pytube.exceptions.RegexMatchError:
                    flash('The link is not correct !!!',category='error')
                    speak.say('The link is not correct !!!')
                    speak.runAndWait()
                    return  redirect(url_for('views.home'))
                try:
                   
                    video = youtube.streams.get_highest_resolution()
                    try:
                        video.download('./videos')
                        
                        flash('Downloaded Successfelly !',category='success')
                        speak.say('Downloaded Successfelly !')
                        speak.runAndWait()
                        return render_template('index.html')
                       

                       # return  render_template('index.html',result=result)
                    
                    except werkzeug.routing.exceptions.BuildError :
                        flash('The link is not correct !!!',category='error')
                        speak.say(' The link is not correct !!!')
                        speak.runAndWait()
                        return  redirect(url_for('views.home'))
                    
                except urllib.error.URLError :
                    flash('The link is not correct !!!',category='error')
                    speak.say(' The link is not correct !!!')
                    speak.runAndWait()
                    return redirect(url_for('views.home'))
                
            except urllib.error.URLError as e: 
                    flash('Provide a good URL !!!',category='error')
                    speak.say(' The link is not correct !!!')
                    speak.runAndWait()
                    return redirect(url_for('views.home')) 
             
        return render_template('index.html',result=result)    
    return render_template('index.html',result=result)
   


@views.route('/videos', methods=['GET','POST'])
def videos():
    return render_template('videos.html')


@views.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')


@views.route('/contact', methods=['GET','POST'])
def contact():
    return render_template('contact.html')