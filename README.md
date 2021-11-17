# ex1
OOP Task 1 - offline algorithm
Made by Amit Goffer - 205541360, Yehonatan Amosi - 209542349.
The principal of the offline Algorithm is allocating each call to an appropriate elevator according two parameters:
The first is to see if the new call can catch a ride with existing path that an elevator will perform.
Prerequisite: the time it will take the elevator to perform the call if inserted - must be greater than each call activation time, otherwise, calls might be inserted and executed too early.
For example: the elevator current stations are 0, 2, 5. and the call is 3 -> 4. so, the call's stations can be added to the existing path - 0, 2, 3, 4, 5.
The algorithm will check each possible insertion for the time it will take the elevator to do the call if added, and will allocate the call to the elevator that do the path that will yield the fastest result.
If no possible insertions are found, the algorithm will do its 'plan b', which is to insert the call's station at the end of the path.
 it will check the time it will take for every elevator to each its existing station, and then to do the newest call.
Then it will select the elevator which will yield the quickest result.
Example: elevator stations - 3,5,1. call - 6 -> 7. after the insertion the stations of the elevator will be 3,5,1,6,7 .
With those 2 stages - we will ensure that each call, in turn, will get the quickest executing time.
![Uml_of_the_class](https://user-images.githubusercontent.com/76455181/142285981-62b8df08-02d5-44c2-a242-30c42d0ed6c0.jpeg)
