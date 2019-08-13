import Jetson.GPIO as GPIO
import time
import operator

signal_pins=[0,7,8,9,10,11,17,18,22,23,24,25,4]
GPIO.setmode(GPIO.BCM)
total_time=180
r_index=0

output_pin1=7
output_pin2=8
output_pin3=9
output_pin4=10

GPIO.setup(output_pin1, GPIO.OUT)
GPIO.setup(output_pin2, GPIO.OUT)
GPIO.setup(output_pin3, GPIO.OUT)
GPIO.setup(output_pin4, GPIO.OUT)




def emergency(time):
	ambulance=0
	if ambulance==1:
		return True
	else:
	 	return False


def st():

	global output_pin1
	global output_pin2
	global output_pin3
	global output_pin4
	tm = 0
	global r_index
	signal=[['R','R','R'],['R','R','R'],['R','R','R'],['R','R','R']]
	remaining={2:0,3:0,4:0}
	while (1):
	
		time.sleep(1)
		tm=tm+1
	
		return_value=emergency(tm)
	
	
		if return_value==True:
			c5=0
			while(1):
			
				time.sleep(1)
				#tm=tm+1
				c5=c5+1
				
			
				if c5==10:
					break
		'''
		road1=[15,15,30,75,312,400,500,500,500,500]
		road2=[1,1,5,25,5,15,5,5,5,5]
		road3=[2,1,7,17,65,30,100,100,100,5]
		road4=[13,13,16,20,15,45,5,5,5,5]
		'''
		
		road1=[15 ,15 ,30 ,45 ,12 ,4  ,5 ,5 ,5 ,5]
		road2=[1 ,25  ,5  ,25 ,5  ,15 ,5 ,45 ,5 ,5]
		road3=[2 ,1   ,7  ,60 ,65 ,30 ,1 ,1 ,80 ,5]
		road4=[18 ,13 ,16 ,20 ,75 ,45 ,5 ,5 ,5 ,50]
		
		'''
		road1=[70 ,70 ,70 ,70 ,70 ,5  ,5  ,5  ,5  ,5  ,5]
		road2=[30 ,30 ,30 ,30 ,30 ,30 ,30 ,30 ,30 ,5  ,5]
		road3=[10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10]
		road4=[20 ,20 ,20 ,20 ,20 ,20 ,20 ,20 ,20 ,20 ,5]
		'''

		#if 1:	
		try:	
			road_count={1:road1[r_index],2:road2[r_index],3:road3[r_index],4:road4[r_index]}
		except:
			break


		sort_road = sorted(road_count.items(), key=operator.itemgetter(1),reverse=True)
		#print sort_road

		t = 240 * (float(sort_road[0][1]))/sum(road_count.values())

		#total_time-sum(remaining.values())<=(len(remaining)*20):
	
		if tm >= t:
			print "star"
			st1()
			break
		else:
	
			try:
				del remaining[(sort_road[0][0])]
			except:
				r=1
			
			signal=[['R','R','R'],['R','R','R'],['R','R','R'],['R','R','R']]
			signal[(sort_road[0][0])-1]=['G','G','G']
			print signal
			
			GPIO.output(output_pin1,GPIO.LOW)

			GPIO.output(output_pin2,GPIO.LOW)

			GPIO.output(output_pin3,GPIO.LOW)

			GPIO.output(output_pin4,GPIO.LOW)



			if (sort_road[0][0])==1:
				output_pin1=signal_pins[3]
			else:
				output_pin1=signal_pins[1]
				
			if (sort_road[0][0])==2:
				output_pin2=signal_pins[6]
			else:
				output_pin2=signal_pins[4]
				
			if (sort_road[0][0])==3:
				output_pin3=signal_pins[9]
			else:
				output_pin3=signal_pins[7]
				
			if (sort_road[0][0])==4:
				output_pin4=signal_pins[12]
			else:
				output_pin4=signal_pins[10]  
				

			GPIO.setup(output_pin1, GPIO.OUT)
			GPIO.setup(output_pin2, GPIO.OUT)
			GPIO.setup(output_pin3, GPIO.OUT)
			GPIO.setup(output_pin4, GPIO.OUT)




			GPIO.setup(output_pin1, GPIO.OUT)
			GPIO.setup(output_pin2, GPIO.OUT)
			GPIO.setup(output_pin3, GPIO.OUT)
			GPIO.setup(output_pin4, GPIO.OUT)

			GPIO.output(output_pin1,GPIO.HIGH)

			GPIO.output(output_pin2,GPIO.HIGH)

			GPIO.output(output_pin3,GPIO.HIGH)

			GPIO.output(output_pin4,GPIO.HIGH)

			for i in remaining:	
				remaining[i]=remaining[i]+1

			if len(remaining)==0:
				remaining={1:0,2:0,3:0,4:0}
				r_index=r_index+1
		if tm%20==0:
			t = (240 - tm) * (float(sort_road[0][1]))/sum(road_count.values())
			r_index=r_index+1
		


		#print sum(remaining.values())

	

		print remaining


def st1():
	global output_pin1
	global output_pin2
	global output_pin3
	global output_pin4
	
	tm = 0
	global r_index
	signal=[['R','R','R'],['R','R','R'],['R','R','R'],['R','R','R']]
	remaining={3:0,4:0}
	while (1):
	
		time.sleep(1)
		tm=tm+1
	
		return_value=emergency(tm)
	
	
		if return_value==True:
			c5=0
			while(1):
			
				time.sleep(1)
				#tm=tm+1
				c5=c5+1
				signal=[['R','R','R'],['G','G','G'],['R','R','R'],['R','R','R']]
				print signal
				
						
				if c5==10:
					break
		'''
		road1=[15,15,30,75,312,400,500,500,500,500]
		road2=[1,1,5,25,5,15,5,5,5,5]
		road3=[2,1,7,17,65,30,100,100,100,5]
		road4=[13,13,16,20,15,45,5,5,5,5]
		'''
		
		road1=[15 ,15 ,30 ,45 ,12 ,4  ,5 ,5 ,5 ,5]
		road2=[1 ,25  ,5  ,25 ,5  ,15 ,5 ,45 ,5 ,5]
		road3=[2 ,1   ,7  ,60 ,65 ,30 ,1 ,1 ,80 ,5]
		road4=[13 ,13 ,16 ,20 ,75 ,45 ,5 ,5 ,5 ,50]
		'''
		road1=[70 ,70 ,70 ,70 ,70 ,5  ,5  ,5  ,5  ,5  ,5]
		road2=[30 ,30 ,30 ,30 ,30 ,30 ,30 ,30 ,30 ,5  ,5]
		road3=[10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10]
		road4=[20 ,20 ,20 ,20 ,20 ,20 ,20 ,20 ,20 ,20 ,5]
		'''

		#if 1:
		try:	
			road_count={1:road1[r_index],2:road2[r_index],3:road3[r_index],4:road4[r_index]}
		except:
			break
				
		sort_road = sorted(road_count.items(), key=operator.itemgetter(1),reverse=True)
		#print sort_road

		t = 240 * (float(sort_road[0][1]))/sum(road_count.values())

		#total_time-sum(remaining.values())<=(len(remaining)*20):
	
		if tm >= t:
			print "star"
			break
		else:
	
			try:
				del remaining[(sort_road[0][0])]
			except:
				r=1
			signal=[['R','R','R'],['R','R','R'],['R','R','R'],['R','R','R']]
			signal[(sort_road[0][0])-1]=['G','G','G']
			print signal
			
			GPIO.output(output_pin1,GPIO.LOW)
            
			GPIO.output(output_pin2,GPIO.LOW)

			GPIO.output(output_pin3,GPIO.LOW)

			GPIO.output(output_pin4,GPIO.LOW)





			if (sort_road[0][0])==1:
			    output_pin1=signal_pins[3]
			else:
			    output_pin1=signal_pins[1]
			    
			if (sort_road[0][0])==2:
			    output_pin2=signal_pins[6]
			else:
			    output_pin2=signal_pins[4]
			    
			if (sort_road[0][0])==3:
			    output_pin3=signal_pins[9]
			else:
			    output_pin3=signal_pins[7]
			    
			if (sort_road[0][0])==4:
			    output_pin4=signal_pins[12]
			else:
			    output_pin4=signal_pins[10]  
			
			GPIO.setup(output_pin1, GPIO.OUT)
			GPIO.setup(output_pin2, GPIO.OUT)
			GPIO.setup(output_pin3, GPIO.OUT)
			GPIO.setup(output_pin4, GPIO.OUT)

			
			
			





			GPIO.setup(output_pin1, GPIO.OUT)
			GPIO.setup(output_pin2, GPIO.OUT)
			GPIO.setup(output_pin3, GPIO.OUT)
			GPIO.setup(output_pin4, GPIO.OUT)

			GPIO.output(output_pin1,GPIO.HIGH)

			GPIO.output(output_pin2,GPIO.HIGH)

			GPIO.output(output_pin3,GPIO.HIGH)

			GPIO.output(output_pin4,GPIO.HIGH)
			
			
			
			for i in remaining:	
				remaining[i]=remaining[i]+1

			if len(remaining)==0:
				remaining={1:0,2:0,3:0,4:0}
				r_index=r_index+1
		if tm%20==0:
			t = (240 - tm) * (float(sort_road[0][1]))/sum(road_count.values())
			r_index=r_index+1
		


		#print sum(remaining.values())

	

		print remaining


tm=0
signal=[['R','R','R'],['R','R','R'],['R','R','R'],['R','R','R']]
remaining={1:0,2:0,3:0,4:0}
c=0
while (1):
	print r_index
	time.sleep(1)
	tm=tm+1
	
	return_value=emergency(tm)
	
	
	if return_value==True:
		c5=0
		while(1):
			
			time.sleep(1)
			#tm=tm+1
			c5=c5+1
			signal=[['R','R','R'],['G','G','G'],['R','R','R'],['R','R','R']]
			print signal

						
			if c5==10:
				break
	'''
	road1=[15,15,30,75,312,400,500,500,500,500]
	road2=[1,1,5,25,5,15,5,5,5,5]
	road3=[2,1,7,17,65,30,100,100,100,5]
	road4=[13,13,16,20,15,45,5,5,5,5]
	'''
	
	road1=[15 ,15 ,30 ,45 ,12 ,4  ,5 ,5 ,5 ,5]
	road2=[1 ,25  ,5  ,25 ,5  ,15 ,5 ,45 ,5 ,5]
	road3=[2 ,1   ,7  ,60 ,65 ,30 ,1 ,1 ,80 ,5]
	road4=[13 ,13 ,16 ,20 ,75 ,45 ,5 ,5 ,5 ,50]
	'''
	road1=[70 ,70 ,70 ,70 ,70 ,5  ,5  ,5  ,5  ,5  ,5]
	road2=[30 ,30 ,30 ,30 ,30 ,30 ,30 ,30 ,30 ,5  ,5]
	road3=[10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10 ,10]
	road4=[20 ,20 ,20 ,20 ,20 ,20 ,20 ,20 ,20 ,20 ,5]
	'''

	#if 1:	
	try:	
		road_count={1:road1[r_index],2:road2[r_index],3:road3[r_index],4:road4[r_index]}
	except:
		break


	sort_road = sorted(road_count.items(), key=operator.itemgetter(1),reverse=True)
	print sort_road

	t = 240 * (float(sort_road[0][1]))/sum(road_count.values())

	#total_time-sum(remaining.values())<=(len(remaining)*20):
	
	if tm >= t:
		print "star"
		st()
		break
	else:
	
		try:
			del remaining[(sort_road[0][0])]
		except:
			r=1
		
		signal=[['R','R','R'],['R','R','R'],['R','R','R'],['R','R','R']]
		signal[(sort_road[0][0])-1]=['G','G','G']
		print signal
		
		GPIO.output(output_pin1,GPIO.LOW)

		GPIO.output(output_pin2,GPIO.LOW)

		GPIO.output(output_pin3,GPIO.LOW)

		GPIO.output(output_pin4,GPIO.LOW)


		
		if (sort_road[0][0])==1:
			output_pin1=signal_pins[3]
		else:
			output_pin1=signal_pins[1]
			
		if (sort_road[0][0])==2:
			output_pin2=signal_pins[6]
		else:
			output_pin2=signal_pins[4]
			
		if (sort_road[0][0])==3:
			output_pin3=signal_pins[9]
		else:
			output_pin3=signal_pins[7]
			
		if (sort_road[0][0])==4:
			output_pin4=signal_pins[12]
		else:
			output_pin4=signal_pins[10]  

		


		
		
		
		GPIO.setup(output_pin1, GPIO.OUT)
		GPIO.setup(output_pin2, GPIO.OUT)
		GPIO.setup(output_pin3, GPIO.OUT)
		GPIO.setup(output_pin4, GPIO.OUT)








		GPIO.setup(output_pin1, GPIO.OUT)
		GPIO.setup(output_pin2, GPIO.OUT)
		GPIO.setup(output_pin3, GPIO.OUT)
		GPIO.setup(output_pin4, GPIO.OUT)

		GPIO.output(output_pin1,GPIO.HIGH)

		GPIO.output(output_pin2,GPIO.HIGH)

		GPIO.output(output_pin3,GPIO.HIGH)

		GPIO.output(output_pin4,GPIO.HIGH)
		
		for i in remaining:	
			remaining[i]=remaining[i]+1

		if len(remaining)==0:
			remaining={1:0,2:0,3:0,4:0}
			r_index=r_index+1
	if tm%20==0:
		t = (240 - tm) * (float(sort_road[0][1]))/sum(road_count.values())
		r_index=r_index+1
		
	


	#print sum(remaining.values())

	

	print remaining

print "d"
outpin_pin2=signal_pins[4]
GPIO.output(output_pin1,GPIO.LOW)

GPIO.output(output_pin2,GPIO.LOW)

GPIO.output(output_pin3,GPIO.LOW)

GPIO.output(output_pin4,GPIO.LOW)
	

	
 #DT20195620818 
