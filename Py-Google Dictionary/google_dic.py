import cv2
from googlesearch import *
import webbrowser
import pytesseract as pt
pt.pytesseract.tesseract_cmd=r"C:\Users\Ajay Bhargav\AppData\Local\Tesseract-OCR\tesseract.exe"

Word=""
img=cv2.imread(r"C:\Users\Ajay Bhargav\Desktop\Open_CV\word.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
text1=pt.image_to_boxes(img)
length,breadth,_=img.shape
print(length,breadth)
for i in text1.splitlines():
    i=i.split(' ')
    Word+=i[0]
    print(i)
    ch,x1,y1,x2,y2=i[0],int(i[1]),int(i[2]),int(i[3]),int(i[4])
    cv2.rectangle(img,(x1,length-y1),(x2,length-y2),(0,0,255),2)
    cv2.putText(img,ch,(x1,length-y1+15),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
    
   #print(text1)
query=Word+" meaning"
chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
    webbrowser.open("https://google.com/search?q=%s" % query)

print(Word)
cv2.imshow("text",img)
cv2.waitKey(0)