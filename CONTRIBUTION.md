What you contributed: Describe your changes and why they're valuable
- I first used black to reformat the code. Then, I used pylint to add docstrings to the files, make sure there were no unneccesary elifs, and that variables weren't being redefined from outer scopes. I used flake8 to mostly adjust the lengths of line in the code, but there are other purposes to it. And I updated type hints within functions. I think these are valuable because they allow the code to be read and understood by anybody who wants to use the code, and it makes the code look prettier.   

Process: How did you approach this work? What tools did you use?
- I went step by step through each file and tried to commit every file as long as it seemed like they were all being changed unless they were simple changes that didn't affect the code that much. For example I did the type hints for most files and commited them together, but in user_management_system.py the type hints were more complicated so I commited that one separately.

Challenges: What difficulties did you encounter and how did you solve them?
- I encountered a difference in line length between flake8 and black, black wanted the print statements in one line while flake8 only wanted up to 79 characters in one line so I had to decide which to follow. I followed flake8's recommendations but I think I like the look of black's recommendations better. Sometimes it's more difficult to cut a print statement into two lines or more, but it makes more sense when writting comments.

Learning: What did you learn about open source contribution?
- I learned that open source contribution can be very useful in finding projects that are already pre-written, but they won't follow all of the coding conventions that pylint, black, and flake8 require. They also don't always use type hints to label functions so when you go back to add that it can be confusing at times.

Future work: What else could be improved in this project?
- To improve this project even more you could add the option for a computer player to the tic-tac-toe file instead of making two player. There also didn't seem to be very many error handlers or try/catch statements so if needed those could be added.