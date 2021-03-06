# Pimulator

Pimulator is a robotics simulator for the Pioneers in Engineering robotics kit. Pimulator seeks to allow students to gain experience in programming their robot with any internet-accessible computer. Students are able to execute code on this virtual robot, just as they can on a physical robot and receive the same feedback. Pimulator seeks to allow aspiring programers the ability to iterate and explore without the constraints of a single physical robot.

Pimulator is composed of two mains sections. The simulator calculates and determines the state of the robot after taking into account physics, student code, the game pad, etc. The web application facilitates communication of state between the user and the simulator.

## The Simulator

The simulator was largely developed by Wing during in Spring 2017. Wing and Scott originally released the simulator using a text based UI through repl.it for general students to use. The UI along with the robustness proved too large of a challenge to prove useful for general PiE students.

The simulator models the robot as a cart with two independently powered wheels. The simulator works

Ideally the simulator would have the flexibility for the student to add on their own other motors and sensors to interact with the world.

## The Web Application

The web application provides the UI. The web application visualizes the state of the robot by updating an SVG diagram through constant AJAX requests. The web application communicates the user intention to start and stop simulation with the simulator through buttons. 

The weba application and simulator exist in different threads and communicate through a thread-safe queue.

## Containerization

To easily deploy, develop, and run the application, pimulator is packaged in images to run in portable containers.

`pie-bot-simulator-dev` is an image that allows developers to run pimulator on identical environments. Files are mounted into the container from the developer's current directory; changes to files on the developer's computer are immediately reflected in the container. Admittedly, the requirements of the environment are sparse, predominantly Flask and Python. I have yet to upload the image to a hoster.

`gcr.io/pimulator-198909/pie-bot-simulator` is an image to run the complete pimulator on a production environment such as Google Cloud or host. Individuals need only download the image and run the image on a container to run pimulator, no cloning required.

## Deployment

Scott has deployed pimulator on Google Cloud, before removing it to not pay money.

## Future Development

* A more a e s t h e t i c UI
* Allowing user-defined student code
* Authentication to prevent randos from running Python code on our dime
* Better error messages and feedback
* Customization of the robot to include sensors and motors, etc.
        * Visual reflection of this
