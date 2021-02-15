# First Python ML Project + Docker

### My Struggles with Docker

"Use Docker, it's the future for delivering applications. It containerizes your application so that anyone, regardleses of their OS or previously installed packages, will be able to run your program." —the voice in my head

I've gone through maybe 10 hours of Docker tutorial content (at 2x speed) and none of them answered all my questions (and yes, I can understand things at 2x speed because I normally watch at 2.5-3x speed :/). Here is me answering the questions I had so that your brain doesn't overflow with stackoverflow articles:

### Why do 95% (estimate) of dockerfiles start with a Linux-based OS?

"This is a python project, why in the world would I want Linux?" was the question in my head whenever I watched a tutorial on Docker. Wouldn't a Python project require a Python layer?? Through tutorial-hell, I realized, hey, how do I actually run my files through a Docker container? It was at that point did I realize the need for an operating system: to mimic the terminal. When you have an OS + python installed, you can run "python < file name >" to run the python script. This is impossible (as far as I know) to do if you install a Python image instead. 

