# Homework 1
Morgan Peters 
A20333151
Fall 2017 CS 445

Dependencies:
 Testing: 
    JUnit and Mockito 
 Implementation:   
    Maven 

How to run: 

git clone https://github.com/morleegan/morgan_peters_CS445.git
cd homework1 

// if you do not have maven installed: 
sudo apt-get mvn 

// continue:

mvn package 
// creates jar file 
java -cp target/HomeWork1_CS445-1.0-SNAPSHOT.jar TestCreature
// this will run the main()    
mvn clean; mvn test;
// will run just the test suit 