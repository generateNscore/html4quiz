# html4quiz

## What is it?

html4quiz is a package that helps you generate question sheets with as many HTML files as you want and grade answers from text files submitted by students.

## Features
<ul>
<li><strong>Local</strong>: Everything is on your local PC, grows with your creativity, and you own everything, unlike the many quiz generators available online.</li>
<li><strong>HTML files</srong>: Question sheets in HTML files, each named with a corresponding identification number, are distributed to students over the network.</li>
<ul><li>Students use their mobile devices to read, answer questions, save answers to a text file for submission within the same HTML page, and submit the text file as directed over the network.</li>
<li>Saving answers to a file can be repeated as many times as desired.</li></ul>
<li><strong>Easy grading</stron>Grade answers in text files submitted by all students can be achieved with a few keystrokes.</li>
<li><strong>Two kinds of HTML files</strong></li>
<ol><li>First kind is to preview questions before generating sheets.</li>
<li>Second kind is the set of sheets.</li></ol>
<li><strong>Two kinds of questions</strong</li>
<ol><li>Short answr questions of requiring a number of a word.</li>
<li>Multiple choice questions whose choices are genterated randomly by one of various methods or by Python coding.</li></ol>
<li><strong>Figures</strong> as well as <strong>mathematical expressions</strong> in LaTeX format can be included in both question texts and choices.</li>
<li><strong.Randomness</strong> is controlled by users with Python scripts.</li></ul>


## Where to get it

<pre lang=sh>pip install html4quiz</pre>

<ul>
<li>The source code is currently hosted on GitHub at: <a href="https://github.com/generateNscore/html4quiz">https://github.com/generateNscore/html4quiz</a></li>
</ul>


## Dependencies
<ul><li>None</li></ul>


## Changes
<ul>
<li>Version 0.0.30</li>
<ul><li>In addition to using a user-defined function for answers, a new way to use resources saved in <a href="https://github.com/generateNscore/html4quiz/tree/main/res">html4quiz/res</a> is added.</li>
<li>For details, please look at <a href="https://generatenscore.github.io/html4quiz/Examples/Ex004/Ex004.py">Ex004.py</a></li>
<li><a href="https://generatenscore.github.io/html4quiz/Examples/Ex004/Ex004/Ex004/index.html">Previews</a></li>
</ul>
<br>


<li>Version 0.0.29</li>
<ul><li>Added an option to reuse previous work.</li>
<ul><li>When an answer of question among many in previous work whose question sheets has been distributed is found incorrect, simply setting the option <strong>True</strong> and re-running the work is all you need to do.</li>
<li>The new option, <strong>flag4Previous</strong> can be added as the last argument to the instance as:</li>
<li>If not provided, the default value of the option, False, is assumed.</li></ul>

```python

flag4Previous = True
h4q.work('exam1', 'testing', STDs, QGs, flag4Preview, flag4Choice, flag4Shuffling, resources, flag4Previous)

```

</ul>
<br>

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
</ul>


## Example shots
<ul>
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
</ul>