# Final-Project-Traffic-policing-system
Traffic policing system is a project done under the SMART INDAI HACKATHON (https://www.sih.gov.in/) which help to maipulate the traffic at junction and reduce waiting time.

# Project youtube link and  ppt mention above as cctv.pdf
https://youtu.be/6sm9HWDmUig

# Note!! This is only a prototype and not the full project the hardware interface and futher development is not included in this repository .

Traffic policing system which will help to manipulate traffic signal with help of CCTV attached at junction and will also help to check which vehicles are violating traffic rules.This system can predict accident and protest can give alert to associated authority with details about scale of impact and location of that event.The vehicles can be categorised as car , truck , motorbike , train and emergency vehicles(Ambulance and Fire vehicle). The count of each category of vehicle will be counted and the side with max counted of vehicle will go green till minimum number of vehicles(like 2 or 3 vehicles ) or maximum time limit is reached this both paraments can be decided according to width and frequency of traffic of that area . The count will be based on priority like the truck will be given highest and the motorbike the lowest priority. 

This system can be integrated in the existing system. We can also use Hikey a powerful ARM-based computers like raspberry pi .This will also help to reduce any time delay which can be created by cloud computing. The system operator can select particular area for selection ,this will help in way that we need not have to change the direction and arrangement of existing CCTV’s it will simply avoid all the other vehicles not in the range and the system can be easily scalable. 

Emergency vehicle can reach to desired location in less time and this can be life saver, so whenever a Emergency vehicle is detected in any lane then regardless of traffic it will give green signal to that lane. This system will detect accident and protest on junction or in any area where CCTV’s are present. When count of people is detected high and density is also high then it can be predicted as a protest or rallies. The user can be benefited in many ways like the waiting time at the signal can be reduced exponentially. 

If protest are predicted then police can reach location in less time and the situation can be handled efficiently. Whenever a accident is detected an alert (system based alert call with location of via SMS) will be send to nearest hospital ambulance and associated authority .The location can be given with help of GPS at that location. The detection of holes and speed breakers can be done by recognition of satellite imaging.And the can be updated on google map which will help the traveller to drive safely.


# How to run

Download this repository and run real_time_counting.py file

select RIO(region of interest) and press q to continue 

start1.py is sample file of jetson nano which can be run when there is interface with the hardware (jetson nona)

Refer https://www.tensorflow.org/install/pip to install Tensorflow 
