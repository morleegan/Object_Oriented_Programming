# Homework 1
Morgan Peters 
A20333151
Fall 2017 CS 445

Dependencies:
 Testing: 
    JUnit, jacoco and Mockito 
 Implementation:   
    Maven 

How to run: 

git clone https://github.com/morleegan/morgan_peters_CS445.git
cd homework1 

//installed: 
sudo apt-get mvn 
sudo apt-get install default-jdk 

// continue:
mvn package 
java -cp target/HomeWork1_CS445-1.0-SNAPSHOT.jar TestCreature

mvn exec:java -Dexec.mainClass="testCreature" -Dexec.classpathScope="test"

// code coverage 
open on browser: ../target/site/jacoco/default/index.html 