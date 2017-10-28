# Homework 3
Morgan Peters, CS 445, A20333151

## Dependencies 
### Testing: 
-JUnit 
-Jacoco
-Mockito 

### Implementation 
-Maven 
-Git
-JDK 1.8

### How to run: 
    mvn clean 
    mvn -q package 
    mvn -q exec:java -Dexec.mainClass="LampMain1" -Dexec.classpath
    mvn -q exec:java -Dexec.mainClass="LampMain2" -Dexec.classpathScope="test"
    
### Testing      
    mvn -q test  
    open on browser: ../target/site/jacoco/default/index.html 
    
