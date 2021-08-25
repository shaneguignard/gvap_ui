# General Video Analytics Platform - User Interface
 A thin client interface for a general video analytics platform.


This is a web app that was built to run as a python container in either Google App Engine, or containerized and deployed into any Cloud solution.

# General Video Analytics Platform Thin Client Interface

The purpose of this project is to develop the user interface “the front end” to a general purpose video analytics system “the backend”. Typically, video analytic systems are developed as highly specific and tailored solutions. Notable differences exist between these two systems. For example, one will query the results of a video while the other stores video content and processes that content for future review. 
This system should be as efficient as possible and consist of 2 components. 
The Video Ingestion Phase; any video from a URL link or feed could be passed to the system to be indexed and prepared for querying. 
Querying the video to discover some kind of information. 

# Requirements
- Overview
- Scope
Initial Queries will focus on position and number of objects
Front end will need to communicate with backend in order to know when the video has finished being processed
The back will provide a text file output which is it’s analysis of the video
The interface should ask the user to help identify whether 2 detected objects in the video are the same or not.
The interface will allow the user to retrieve a synapsis of the video based on a question parameter.

# User Requirements
Upload Video
- Users will upload a video file
- Video will be passed to Backend for processing
- Video Library (advanced feature)
Initial assumption is that the entire system should be built offline for a single user. Therefore, the video library will exist as a master library of all previously processed videos.

- Refinement Questionnaire and Algorithm training 
“Are these 2 images the same object?”
… (more to come as the project progresses)

- Tagging an image (Advanced Feature)
# Query Video for information
- “Retrieve all frames where # of (Blank) appears”
The means of adding additional question templates should be modular, such that the future addition of questions can be implemented very easily. (Advanced Feature) 
… more questions to come as the project progresses

# High-Fidelity Prototype

- Sketch/ mock of horizontal prototype

# Upload Video page
Features: 
- Simple “Choose File” button
- Select algorithm profile [deepsort, tracktor, etc …]

Possible Future Page Features:
- Indicator icon on video file which indicates that the backend is still processing
- Estimated Time indicator
- Video upload status progress bar
- Search and re-naming videos


# Algorithm Annotation Page (optional involvement by user)

Features:
- Present comparisons of objects to confirm whether or not they are the same object being tracked throughout the video. (yes/no)
- Only one comparison at a time.
- User can opt out at any time

# Video Analysis page

Features:
- Search Query box “Get all frames with # of _____ in them?”
- Return short video clips that match the requirements of the query


# Prototype Validation
Technology Stack

- BackEnd Processing Node
- MySQL database to store and retrieve processed video data
- Local Mysql instance was created to develop schema and other database related systems before deploying to a production environment.
- Flask python webserver
A simple Flask application server will be used to route and manage the HTTP requests from the client machine. Minimal processing should be done on the web server if at all possible. 
This will only be used to redirect requests and retrieve data from database server

- Jinja2 Markup Language for Client Side
Markup Language that integrates with Flask for a more cohesive development experience
- HTML5 Canvas for video markup and manipulation
- Javascript for additional client side functionality (caching, wait-time estimates, etc ... ) 

# Implementation

- Video upload

I implemented a HTML Form element, which will send the contents of an HTML Input element of type “file”. The element, and the file enclosed can be referenced on the server side via the name provided in the “name” attribute of the same HTML Input element.

On the server side, the file is received at the url endpoint defined in the HTML Form elements “action” attribute. If the request is of type POST, then we will try to retrieve the files contained within the message. If successful, the file will be saved to the location “uploads/” with the filename provided. 

Before allowing the Web Server to send the newly uploaded video to the Backend Server, we will register and catalog the video in a database called Videos. Then, if all goes well, the users session is refreshed with a message being returned to the Client Server of type “info” to let the user know that the file was uploaded successfully. 

Currently, if anything fails in the try-block a catch-all exception is thrown, but the most common error will likely be because an invalid or improperly formatted filename was provided. If an error is caught, a message is sent to the user indicating that an error occurred, and an additional error message is logged into the Web Server.


- Video Annotations

Analysis of the videos will be returned to the Web Server from the backend as plain text files formatted as:
<frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>

These files will be saved or held in the Web Server storage, and associated with a registered video from our database. 

Object image extraction from video

Because the backend only supplies a text file that identifies the coordinates of each object within the video, it is necessary to parse through each frame of each video in order to extract or crop a list of unique objects detected within the video.

Parse Analysis file, and append to a list of objects per frame, where each frame number has an array associated with it which represents each object within the frame.
Next, the client should extract a list from the analysis of all unique objects in video
 
1. Process file passed to client from webserver frame by frame. 
2. Collect meta data from video file
3. Collect array of images of objects by ID from video
4. Present 2 images of 2 object IDs selected at random from the list of IDs in the video
5. Record whether images are the same or not from user feedback
6. HTML Form
7. Submit to database only if match is true
  <row id> <id obj1> <id obj2>

For testing purposes, the training can be accomplished by simply asking the user if any 2 random objects are the same.

In the future, the backend will present a single ID with 2 objects of uncertainty, and we will be able to use this to present which objects are of interest, rather than being of random choice.

- Video querying

The user would like to be able to ask a question about the video, and have a summarized version of the video presented to them. 

This process will be similar to the video training, except that the focus will be on building a new “video” which represents the response to a user based query/ question.

1. Collect array of number of objects in each frame of a video
2. Collect “query” from user (User selects number of objects in frame that they are interested in)
3. Filter video frames based on object count in frame
4. Play new “filtered” video by pushing frame ID from array back to it. 

# Concluding Thoughts
   This project is unfortunately not finished, but to myself or anyone else that forks this repo and would like to continue building out this project, here are some links that I found helpful while I was working on this project. It might provide some insights into how certain mechanisms work.

References and Helpful web sources
https://motchallenge.net/instructions/
<li><a href="https://pythonbasics.org/flask-upload-file/">Uploading a file with python and flask</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Manipulating_video_using_canvas">Manipulating video using HTML5 Canvas</a></li>



