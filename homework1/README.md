## Homework 1
Morgan Peters, A20333151, Fall 2017 CS 445 <return>

#### Dependencies: 

##### Testing: 

- JUnit 
- Jacoco
- Mockito 

##### Implementation:  

- Maven 
- Git
- JDK 1.8 

##### How to run: 

###### Install: 

    sudo apt-get mvn 
    sudo apt-get install default-jdk 
    git clone https://github.com/morleegan/morgan_peters_CS445.git
    
###### To run on with Maven: 

    cd homework1 
    mvn -q package //complies and runs tests  
    mvn -q exec:java -Dexec.mainClass="testCreature" -Dexec.classpathScope="test" //runs TestCreature.main() 
      
###### Testing 
    mvn -q test  
    open on browser: ../target/site/jacoco/default/index.html 