# Building a Race <br>
Next, let's try defining a class to represent a race. Our Race class will accept a name, to denote which race it is, a list of cars in the race, and a limit of cars that can be included (you can't have an unlimited number of cars in a race, we just call that traffic). Define the Race constructor with at least the following attributes:

* name - should be defined on instantiation <br>
* driver_limit - should also be defined on instantiation<br>
* drivers - can be instantiated as an empty list <br><br><br>

## Now let's build a Driver class. This class should have the following attributes:
<br><br>
* name <br>
* age <br>
* ranking <br><br>

And the following static attribute:<br><br>

* number_of_drivers <br><br>
And be sure to update your constructor to increment the number_of_drivers by one (1) each time an instance of the class is instantiated.<br><br>

Next, add a method to the driver class called get_ranking which returns that instance's specific ranking.