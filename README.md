# DeliveryProject ReadMe
This was the final project deliverable for my Data Structures and Algorithms 2 class 
at Western Governors University Computer Science Major.

The goal of this project was to create a delivery simulation where given a map of locations
in Salt Lake City, Utah, the programmer would create an optimized route under 140-miles to
deliver packages. Some packages had specific requirements such as certain packages could only be delivered
by a certain time, while other packages had to be delivered in the same truck, some packages were delayed in transit to
 the hub, etc. I used the nearest neighbor greedy algorithm to determine which locations to go to and in what order, 
all the while prioritizing packages that needed to be delivered early. There were total of 40 packages and 28 different
locations. Utilizing two different delivery trucks starting at 8:00AM I was able to deliver all packages on time within 
97-miles and by 12:59PM. I could have gotten the mileage down even more if I left the first truck out in the city,
but I decided to return it back to the HUB, since it was a more realistic thing to do.

I created a self-adjusting hashtable to store the package information which was provided in an Excel file which i converted
to a .csv file, and utilized a 2-dimensional array to store the delivery locations provided. 

The program runs with an O(N<sup>3</sup>) efficiency, and an O(N<sup>2</sup>) space complexity. 

## Future Improvements
I would like to create a similar version of this project to utilize a graph-based data structure that would hold of the
location data, and create an algorithm based around that to optimize travel and delivery. If you check my commit history
you might notice that I actually created the graph data structure, but decided implementing a greedy algorithm based around
a 2-dimensional table array would a better utilization of the time I had left to finish the project.
I would like to change the algorithm from a greedy algorithm to perhaps a branch and bound algorithm just to see what the
difference in efficiency would be. Regardless, I would like to get it below O(N<sup>3</sup>).

If  you have any questions or comments please let me know, I'd love to hear from you!

### Screenshots And Installation Instructions
If you want to check out the project for yourself, all you need to do is clone this repo, open it up and run it. 
The menu is command-line based and will show you the mileage of each truck, when items are delivered and also offers an 
interactive menu if you want to query individual results, see the status of each package at a certain time, or see when 
all packages were delivered. Linked below is a demo on YouTube and screenshots of the command line interface.

[Link to YouTube Demo](https://youtu.be/-5GINpEQm7o)

#### Menu Options
![Menu options](images/Menu%20Options.png)
#### Delivery Status for all packages
![Delivery status for all packages](images/all%20delivered%20packages.png)
#### Package Status At 10:07PM
![Package status 10:07PM](images/ten_oh_seven%20status.png)
