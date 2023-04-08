# Latest version in release notes is current version

## Version 0.0.11

<storng>Added:</strong>
<ul><li>Up to 0.0.10, two kinds of questions were abled.</li>
<ul><li>Started with short-answer question and conveyed to multiple choice question with one of prepared mechanisms.</li>
<li>Started with multiple choice questions.</li></ul>
<li>What is added is a way to stay in short-answer question as:</li>
  
  ```python
  
answer = [{'choices':None, 'ans': ans}]
  
  ```
  <li>This answering form is different from the one of</li>
  
  ```python
  
  answer=[{'choices':None, 'ans':vA+vB, 'fn': 'variation0_int'}]
  
  ```
  <li> This is about <a href="https://github.com/generateNscore/htmlfilesforquiz/wiki#2-specifying-method-of-converting-a-short-answer-to-a-set-of-choices">Specifying method of convering short-answer to a set of choices.</a></li></ul></ul>
