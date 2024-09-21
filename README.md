# Use an official OpenJDK runtime as a parent image
FROM openjdk:11-jre-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the jar file from the target folder into the container
COPY target/spring-boot-microservice-0.0.1-SNAPSHOT.jar /app/microservice.jar

# Expose the port your Spring Boot application will run on
EXPOSE 8080

# Run the jar file
ENTRYPOINT ["java", "-jar", "/app/microservice.jar"]



docker build -t spring-boot-microservice:latest .
docker run -p 8080:8080 spring-boot-microservice:latest
docker run -d -p 8080:8080 spring-boot-microservice:latest









FROM oracle-jdk:11-stable


WORKDIR /app


COPY macs-profile-rest-service-1.0.0-SNAPSHOT.jar /app/microservice.jar


EXPOSE 8080

# Run the JAR file
ENTRYPOINT ["java", "-jar", "/app/microservice.jar"]
