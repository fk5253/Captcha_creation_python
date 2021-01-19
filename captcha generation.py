#generate image captcha
from captcha.image import ImageCaptcha
image= ImageCaptcha()

image_data=image.generate('Fakhruddin')
image.write('Fakhruddin' , 'Captcha.png')

#generate voice captcha

from captcha.audio import AudioCaptcha

audio=AudioCaptcha()
audio_data=audio.generate('12345')
audio.write('12345' , 'audio.wav')