#cmd /k python "$(FULL_CURRENT_PATH)"&ECHO.&PAUSE&EXIT

#題目:光圈聚焦
#step1. rgb->hsv
#step2. 選擇聚焦點
#step3. 光圈範圍
#step4. 逐漸變暗,直至全黑

import os
import math
import colorsys
import numpy
from PIL import Image
from PIL import ImageColor


#更改副檔名
'''
for f in os.listdir('.'):
	if f.endswith('.jpg'):
		i = Image.open(f)
		fn, fext = os.path.splitext(f)
		i.save('{}.png'.format(fn))
'''

#rgb->hsv
'''
def RGB2HSV(R,G,B):
	r=R/255
	g=G/255
	b=B/255

	min_rgb=min(min(r,g),b)
	max_rgb=max(max(r,g),b)
	
	v=max_rgb
	delta=max_rgb-min_rgb
	
	if(max!=0):
		s=delta/max_rgb
		if(r==max_rgb):
			h=(g-b)/delta;
		elif(g==max):
			h=2+(b-r)/delta
		else:
			h=4+(r-g)/delta
		h*=60
		s=s*100
		v=v*100
	else:
		s=0
		h=0
'''

#hsv->rgb(圖片格式依然是rgb，hsv處理完後還需轉回去)
'''
'''


#讀黨並轉成RGB (最後輸出需要改回CMYK才能顯示圖片)
im=Image.open("C:\\Users\\Public\\Documents\\lena.png")
image=im.convert(mode='RGB')

#設定空陣列
size=width,height=image.size
buffer_r2h=numpy.zeros((size),dtype=float)
buffer_g2s=numpy.zeros((size),dtype=float)
buffer_b2v=numpy.zeros((size),dtype=float)

#設定光圈位置及大小
coordinate_point= x,y =(127,127)
range_a=60
range_b=80
range_point=150
count=0

#print(im.getpixel(coordinate))

#處理影像rgb->hsv
for i in range(width):
	for j in range(height):
		coordinate_number= i,j
		r,g,b=image.getpixel(coordinate_number)
		h,s,v=colorsys.rgb_to_hsv(r,g,b)

		#threshold_orc=(((i-x)**2)/(range_a**2))+(((j-y)**2)/(range_b**2))

		threshold=((i-x)**2+(j-y)**2)**(1/2)
		if threshold<range_point:
			#改變明度
			v=(v)*((1-threshold/range_point)**1.5)
		else:
			v=0
			
		
		#if threshold_orc < 1:
		#	count+=1
		
		
		
		buffer_r2h[i][j]=h
		buffer_g2s[i][j]=s
		buffer_b2v[i][j]=v
		#print(image.getpixel(coordinate_number))
#print(count)


#Debug用，檢查v值		
#print(buffer_b2v)

#處理影像hsv->rgb
for i in range(width):
	for j in range(height):
		h=buffer_r2h[i][j]
		s=buffer_g2s[i][j]
		v=buffer_b2v[i][j]
		r,g,b=colorsys.hsv_to_rgb(h,s,v)
		r=int(round(r))
		g=int(round(g))
		b=int(round(b))
		
		coordinate_number= i,j
		image.putpixel(coordinate_number,(r,g,b))
		
		
#轉回CMYK並輸出		
image.convert(mode='CMYK').show()



