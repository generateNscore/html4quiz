# html4quiz

## What is it?

html4quiz is a package that helps you generates question sheets with as many HTML files as you want and allows you to grade answers from text files submitted by students.

## Help
<ul>
<li><a href="https://github.com/generateNscore/html4quiz/wiki">Documentation</a></li>
</ul>

## Features
<ul>
<li>Everything is on your local PC, grows with your creativity, and you own them all.</li>
<li>Question sheets in HTML files, each named with a corresponding identification number, are distributed to students over the network.</li>
<li>Students use their mobile devices to read, answer questions, save answers to a text file for submission within the same HTML page, and submit the text file as directed over the network.</li>
<li>Grading answers from text files submitted by students can be done with a few keystrokes.</li>
<li>A question begins with a short answer in a number or word.</li>
<li>Questions with numeric answers can be converted to multiple choice questions simply by flipping the flag.</li>
<li>Questions can start with multiple choice.</li>
<li>Mathematical equations in LaTeX format can be included in both question texts and choices.</li>
<li>Figures can be included in both question text and choices.</li>
<li>Question text, mathematical equations, and figures are all randomly selected for each question sheet in a controlled manner.</li>
<li>To increase your creativity, user-defined functions can be easily added.</li>
<li>Questions that require student to "play" some time to answer correctly can be created.</li>
</ul>

## Where to get it
<ul>
<li>The source code is currently hosted on GitHub at: <a href="https://github.com/generateNscore/html4quiz">https://github.com/generateNscore/html4quiz</a></li>
<br>

<pre lang=sh>pip install html4quiz</pre>

</ul>


## Dependencies
<ul><li>None</li></ul>


## Changes

<li>Version 0.0.22</li>
<ul><li>Added "res" folder to GitHub for the Javascript scripts of figures and additional data saved in JSON format.</li>
<li>Added a "getResource()" function to the package to access the data.</li>
<li>Some procedures of calling functions were removed to simplify the usages of package.</li>
</ul>
<br>
<li>Version 0.0.21</li>
<ul><li>Package name has been changed from htmlfilesforquiz to html4quiz</li>
<li>So is the name of repository in GitHub.</li></ul>
<br>
<li>Version 0.0.20</li>

<ul><li>Finallized a way to upload/download Javascript scripts saved in JSON files for figures.<a href="https://github.com/generateNscore/html4quiz/wiki#h-download-json-file-of-javascript-code-for-figure-contents">H. Download Json file of Javascript code for figure contents</a></li></ul>
<br>

<li>Version 0.0.16</li>

<ul><li>In addition to typical short-answer questions that can be answered on the screen, a new kind questions for which students are required to "play" with mouse to complete a required task to answer is added.</li>
<li>Example: <a href="https://generateNscore.github.io/html4quiz/Examples/Nk001/Nk001.py">Nk001.py</a></li>
</ul></ul>
<br>

<li>Version 0.0.11</li>

<ul><li>A way to stay in short-answer question is added as:</li>
  
```python
  
answer = [{'choices':None, 'ans': ans}]
  
```

<ul><li>This answering form is different from the one of</li></ul>
  
  ```python
  
answer = [{'choices':None, 'ans':vA+vB, 'fn': 'variation0_int'}]
  
```

<li>This is about <a href="https://github.com/generateNscore/html4quiz/wiki#2-specifying-method-of-converting-a-short-answer-to-a-set-of-choices">Specifying method of convering short-answer to a set of choices.</a></li></ul>



## Example shots

<li>A short-answer question</li>
<img src="https://generateNscore.github.io/html4quiz/img/example1-3.png">
<li>A multiple-choice question</li>
<img src="https://generateNscore.github.io/html4quiz/img/example1-6.png">
<li>A multiple-choice question with a figure</li>
<img src="https://generateNscore.github.io/html4quiz/img/example1-2.png">
<li>A question with multiple-choice figures</li>
<img src="https://generateNscore.github.io/html4quiz/img/example1-1.png">
<li>A question with equation and with multiple-choices</li>
<img src="https://generateNscore.github.io/html4quiz/img/example1-4.png">
<li>A question with equation and with multiple-choice figures</li>
<img src="https://generateNscore.github.io/html4quiz/img/example1-5.png">
