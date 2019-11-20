# [Python教育资源大全中文版](https://github.com/wwj718/awesome-python-in-education-zh)

*[源英文版](https://github.com/quobit/awesome-python-in-education)*

*Python教育方面的资源列表*

有许多方式为本项目提交贡献. 你可以从[这儿](CONTRIBUTING.md)开始.

当前资源的遵循的协议是[CC0](LICENSE).

ps: 本列表翻译自[awesome-python-in-education](https://github.com/quobit/awesome-python-in-education),翻译的内容更新到[此次提交](https://github.com/quobit/awesome-python-in-education/commit/48eb55734e217adc6be81c68cb6ee06564be1466)，之后将定期与原项目同步

Awesome-XXX 是GitHub上知名的一组项目，其主页：[Awesome 清单](https://github.com/sindresorhus/awesome/blob/master/awesome.md)

近期我在关注编程在教育中的现状和资源，于是找到这份资源列表，其中许多项目我都在使用,对于我不熟悉的项目，我将亲手试用一遍，并给出我的评价和使用体验,也欢迎大家一起补充

## 目录

* [课程](#courses-and-lessons)
  * [交互式编程环境](#interactive-environments)
  * [慕课](#moocs)
  * [介绍和教程](#introductions-and-tutorials)
    * [数据科学](#data-science)
* [练习和游戏](#exercises-and-games)
* [参考和论坛](#reference-and-forums)
  * [教育中Python的适用性](#python-suitability-for-education)
  * [学术论文](#academic-papers)
  * [参考](#reference)
  * [邮件列表](#mailing-lists)
  * [论坛](#forums)
* [工具与库](#tools-and-libraries)
  * [游戏，图形与仿真](#games-graphics-and-simulation)
  * [可视化](#visualization)
  * [Jupyter](#jupyter)
  * [IDEs](#ides)
  * [调试器](#debuggers)
* [会议与视频](#conferences-and-videos)
* [书籍](#books) (以下是出版社的名字，不译)
  * [Coding Club books](#coding-club-books)
  * [Green Tea Press](#green-tea-press)
  * [Invent with Python series](#invent-with-python-series)
  * [Manning Publications](#manning-publications)
  * [No Starch Press](#no-starch-press)
  * [O'Reilly](#oreilly)
  * [Packt Pub](#packt-pub)
* [硬件](#hardware)
  * [树莓派](#raspberry-pi)
  * [Arduino](#arduino)
  * [BBC micro:bit](#bbc-microbit)
  * [Pyboard](#pyboard)

## 课程

### 交互式编程环境

* [通过Trinket进行积木化的编程](https://hourofpython.com/from-blocks-to-code-with-trinket/) (更多资源参见 [Hour of Python](https://hourofpython.com/)) - 通过blockly来进行积木化的编程，并生成python代码(ps:我最近就在做此类事情，blockly是非常强大的工具，我试图将这个思路拓展到硬件和AI上)
* [Python for Everybody](https://books.trinket.io/pfe/) - trinket.io 交互式书籍
* [如何像计算机科学家一样思考](http://interactivepython.org/courselib/static/thinkcspy/index.html) (更多资源参见 [Runestone Interactive](http://runestoneinteractive.org/library.html))
* [pythonroom](https://pythonroom.com/) - pythonroom让大家轻松进行计算机科学教学
* [repl.it classrooms](https://repl.it/site/classrooms) - 专门为老师准备的新工具
* [CS Principles: Big Ideas in Programming](http://interactivepython.org/runestone/static/StudentCSP/index.html): 这本电子书非常有趣,它通过Python来教你编程,让你多读代码而不是一来就让你开始写，你无需安装任何东西在浏览器里就可以开始你的编程之旅
* [CodeSkulptor](http://www.codeskulptor.org/) - 使用[skulpt](https://github.com/skulpt/skulpt)在浏览器中跑Python,你可以在其中可视化地看待代码的执行过程
* [BlockPy](http://think.cs.vt.edu/blockpy/) - 基于web的编程环境，让你能同时使用blockly积木块和代码来编程，为数据科学而生
* [Edublocks](http://edublocks.org/) - 使 Scratch 到 Python 的转化更加容易
* [Python Lectures](https://github.com/rajathkumarmp/Python-Lectures) - 在IPython Notebooks中学习Python,十分理想的学习环境
* [Learn Python](http://www.learnpython.org/) - 一个在线学习Python的电子教程，同样是只要有浏览器就行
* [Code Club Python modules](https://www.codeclubprojects.org/en-GB/python/) - 使用trinket.io来教学Python,教学案例的设计有趣而用心
* [Computer Science Circles](http://cscircles.cemc.uwaterloo.ca/) - 一本学习Python的电子教程，你将跟着教材在浏览器中做练习,可以用可视化的方式看到代码的执行过程
* [Python from scratch](https://open.cs.uwaterloo.ca/python-from-scratch/) - 一门完整的课程，包括了视频讲解和线上练习
* [以交互式的方式通过100多个练习来学习Python3](https://snakify.org/) - 
* [Codesters](https://www.codesters.com/) - 这是一个非常完整的解决方案，你可以在学校里使用它,包含了编程平台、学习管理系统和课程，另外值得一提的是里边的例子都非常有意思

### 慕课

* [大家的编程 (Python 入门)](https://www.coursera.org/learn/python) - coursera上的一门Python入门课,课程对学生没有先设要求,用户评分4.8
* [Python 交互式编程导论（第1部分）](https://www.coursera.org/learn/interactive-python-1) - coursera上的一门课,课程的第1部分中，介绍编程的基本元素（如表达式，条件和函数），然后使用这些元素创建简单的交互式应用程序
* [Python 交互式编程导论（第2部分）](https://www.coursera.org/learn/interactive-python-2) - 课程的第2部分中，将介绍更多的编程元素（如列表，词典和循环），然后使用这些元素来创建诸如21点游戏
* [Python Programming: A Concise Introduction](https://www.coursera.org/learn/python-programming-introduction) - coursera上的一门课,这门课程将展示如何安装Python并使用Spyder IDE（集成开发环境）编写和调试程序（python3.x）
* [Introduction to Computer Science and Programming Using Python](https://www.edx.org/course/introduction-computer-science-mitx-6-00-1x-9) - edx上的一门课，本课是一门计算机科学的导论课，主要教授解决真实世界中的分析问题的方法。旨在帮助没有计算机科学及编程学习经验的人，培养他们的计算思维，并且编写程序来解决一些实用的问题
* [Learn to Program Using Python](https://www.edx.org/course/learn-program-using-python-utarlingtonx-cse1309x) -edx上的一门课，本课程的练习将基于与现实问题相关的小任务。
* [CS For All: Introduction to Computer Science and Python Programming](https://www.edx.org/course/cs-all-introduction-computer-science-harveymuddx-cs005x-0) - 通过各种各样的演示和项目来对计算机科学领域有一个广泛的认识
* [编程基础：Python](https://www.udacity.com/course/programming-foundations-with-python--ud036) - udacity 上的一门课,在此入门级编程课程中，你将学习软件工程师必须掌握的一门技能——面向对象编程方法.你将编写服务器端代码，以便存储你喜爱的电影，包括电影海报和预告片网址。然后将这些数据当做网页来投放，并允许访问者评论电影和观看预告片。
* [Python Codecademy](https://www.codecademy.com/learn/python) - Codecademy是一个在线交互式网站平台，它提供免费编程课堂,有大量用户在上边做练习
* [CS 61A: The Structure and Interpretation of Computer Programs](http://cs61a.org/) - CS 61系列是对计算机科学的介绍，特别强调站在软件和程序员的角度来看机器.这门课的课程表会给你在校学习的感觉
* [Python School](https://pythonschool.net/) -  Python School 为ICT(信息通讯技术)教师提供了一种在学校教授计算机/计算机科学所需的知识和技能的途径。
* [Let’s all build a comprehensive interactive Python curriculum together](https://forum.freecodecamp.com/t/lets-all-build-a-comprehensive-interactive-python-curriculum-together/103979) - 来自FreeCodeCamp.com的一份学习资源:让我们一起构建一个全面的交互式Python课程

### 介绍和教程

* [The Hello World Program: Learn Python](https://thehelloworldprogram.com/python/) - 这一系列入门教程语言生动活泼，另外值得一提的是插图很有意思
* [Introduction to Python](http://introtopython.org/) - 一门同时为学生和教师准备的课程
* [NewCoder](http://newcoder.io/) - 以项目驱动的方式，让你在编程中获得成就感,目标是让新手只学语法时可能遇到的沮丧情绪，从而愿意继续学习
* [Python tutorial](https://pythonspot.com/) - 教程涉及很多有意思的话题:机器视觉、游戏、机器人
* [Try Python](https://www.codeschool.com/courses/try-python) - 来自 Code School的免费课程（基础）
* [Programming with Python](http://swcarpentry.github.io/python-novice-inflammation/) - from [Software Carpentry](http://software-carpentry.org/) - 学习如何编程的最好方法是做一些有用的事情，所以这个教程是围绕一个常见的科学任务：数据分析
* [Introduction to Programming with Python](http://opentechschool.github.io/python-beginners/en/index.html) - 通过解决一个个的问题来学习
* [Python Course](http://www.python-course.eu/) - 尽管市面上有丰富的教程，这篇教程试图提供更有意思的例子、图示，另外内容十分丰富详实
* [The Programming Historian](http://programminghistorian.org/lessons/) - 历史学家提供的一份教程，帮助人文主义者更好地掌握和使用数字化的工具以帮助它们的研究
* [Program Arcade Games With Python And Pygame](http://programarcadegames.com/index.php?lang=cn) - 通过使用pygame做游戏来学习python
* [Python Tutorials for Kids 13+](https://python4kids.brendanscott.com/) - 这是一个父亲为孩子写的教程，适合13+的孩子
* [Python Asynchronous I/O Walkthrough](http://pgbovine.net/python-async-io-walkthrough.htm) - Python异步I/O的学习
* [Python Tutorials and Courses Directory](https://hackr.io/tutorials/learn-python) - 透过投票的方式选出最好的线上教程
* [Python as a Second Language](https://swcarpentry.github.io/python-second-language/) - (python3/jupyter notebook) 如果你其他语言的编程经验，这篇文档就是为你准备的:使用python作为第二语言
* [A simple tutorial about effectively using pdb](https://github.com/spiside/pdb-tutorial) - 一篇教你使用pdb的教程
* [Beginning Python](http://archive.oreilly.com/oreillyschool/courses/Python1/index.html) - [Getting More out of Python](http://archive.oreilly.com/oreillyschool/courses/Python2/index.html) - [The Python Environment](http://archive.oreilly.com/oreillyschool/courses/Python3/index.html) - [Advanced Python](http://archive.oreilly.com/oreillyschool/courses/Python4/index.html) - 来自O'Reilly技术学院的4门课程
* [Testing and Continuous Integration with Python](http://katyhuff.github.io/python-testing/) - 学习使用pytest来做测试

#### 数据科学

* [A Whirlwind Tour of Python](http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp) and the [Jupyter Notebooks](https://github.com/jakevdp/WhirlwindTourOfPython) behind. -  一本电子书,内容包括包括NumPy，Pandas，Matplotlib，Scikit-learn等，在github有配套源码
* [A Crash Course in Python for Scientists](http://nbviewer.jupyter.org/gist/rpmuller/5920182) - 通过jupyter notebook来教学，特点是速成
* [Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science) - datacamp上的一门数据科学课
* [Learning Python for Data Science](http://www.datasciencecentral.com/profiles/blogs/learning-python-for-data-science) - 这是一个学习数据科学的资源列表
* [Introduction to Python for Data Science](https://www.edx.org/course/introduction-python-data-science-microsoft-dat208x-5) - edx上的一门课,你将通过Python进入数据可视化的世界，并根据实际数据创建令人惊叹的可视化
* [Programming with Python for Data Science](https://www.edx.org/course/programming-python-data-science-microsoft-dat210x-3) - edx上的一门课, 使用机器学习来做数据挖掘
* [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook) - Python数据科学手册
* [Exploratory Computing with Python](http://mbakker7.github.io/exploratory_computing_with_python/) - (jupyter notebook) 这一系列的notebook是为希望使用Python进行探索性计算，脚本编写，数据分析和可视化的科学家和工程师编写的
* [Data Carpentry: Python for Ecologists](http://www.datacarpentry.org/python-ecology-lesson/) - 这些课程可以在一天（约6小时）内完成，包括python语法、Jupyter notebook的使用、导入csv文件，pandas的使用、统计和绘图
* [Plotting and Programming in Python](http://swcarpentry.github.io/python-novice-gapminder/) - (python3/jupyter notebook) 通过绘图来学习
* [Applied Plotting, Charting & Data Representation in Python](https://www.coursera.org/learn/python-plotting) - coursera上的一门课,介绍信息可视化的基础知识，并重点使用matplotlib库进行图表制作
* [Using Python for Research](https://www.edx.org/course/using-python-research-harvardx-ph526x) - edx上的一门课，本课程弥合了Python入门和高级课程之间的差距，让你能把Python技能用到研究项目中

## 练习和游戏

* [CheckiO](https://checkio.org/) - 用户可以通过编程(Python/JavaScript)来解决游戏中的各种任务，还可以与其他开发者玩编程逻辑游戏进行比赛，来交流编程技能、经验
* [CodeAbbey](http://www.codeabbey.com/) - 网站带有online judgement，让你在做题中进步
* [Empire of Code](https://empireofcode.com/) - 这是一个战略、战术和编码混合的空间游戏。尽管可以不使用编码技能来玩游戏，但是使用代码会给你带来优势
* [Project Euler](https://projecteuler.net/) - 一系列具有挑战性的数学/计算机编程问题
* [Exercism](http://exercism.io/languages/python/) - 通过解决问题来学习编程的网站，支持丰富的编程语言(包括Python) 
* [HackerRank Challenges](https://www.hackerrank.com/domains/python/py-introduction) - 又一个通过解决问题来学习编程的网站
* [PyBites](http://pybit.es/) - 一个基于pelican的博客，经常会更新一些小练习或是教程，颇似国内的一些Python公众号
* [Practice Python](http://www.practicepython.org/) - 有笨方法学Python的味道
* [Python Challenge](http://www.pythonchallenge.com/) - 一个网页闯关游戏，通过一些提示找出下一关的网页地址，可玩性很强，尤其是和一起学习的伙伴看谁先顺着线索走下去，有探案的快感
* [Python for Fun](http://openbookproject.net/py4fun/) - 对算法和计算机科学感兴趣的小伙伴可能会喜欢它，涉及比较多的算法
* [CodingBat](http://codingbat.com/python) - 来自斯坦福大学的一名计算机科学讲师的项目，包含很多练习
* [Reeborg's world](http://reeborg.ca/index_en.html) - 通过代码操控指定的虚拟角色来学习
* [Python Koans](https://github.com/gregmalcolm/python_koans) - 通过TDD的方式来学习Python
* [Boston Python Puzzles](http://puzzles.bostonpython.com/) - 通过解决一个个有趣的谜题来学习
* [Code & Conquer](http://www.codeandconquer.co/) - 
* [CodeCombat](https://codecombat.com/) - 这是一个多人回合制策略游戏，在游戏中你可以用代码去创建你的人工智能
* [TeachCraft-Challenges](https://github.com/teachthenet/TeachCraft-Challenges) - 用于教中学和高中生的基础编程知识.学生在minecraft可以调用他们在代码中编写的法术，互相战斗
* [Slice like a Ninja](http://briandavidhall.com/slice_like_a_ninja/) - 极简的闯关游戏
* [Python Datasets: The Collection of Really Great, Interesting, Situated Datasets](https://think.cs.vt.edu/corgis/python/index.html) - (visit [CORGIS](https://think.cs.vt.edu/corgis/) for raw formats) - 来自现实世界的许多数据集，可直接在python中使用
* [Interactive Coding Challenges](https://github.com/donnemartin/interactive-coding-challenges) - 使用Python来挑战算法和数据结构
* [Pyweek Programming Challenge](https://pyweek.org/) - 你可以独自或者组团去参加挑战，挑战任务都非常有趣
* [CodingGame](https://www.codingame.com) 让程序员通过解决世界上最具挑战性的问题，学习新概念
* [CodeFights](https://codefights.com/) 这个网站目标是让编程变得有趣，在游戏中学到东西 

## 参考和论坛

### Python在教育中的适用性

* [CP4E](https://www.python.org/doc/essays/cp4e/) : 由python之父创建的一份资金申请，在其中说明了他对Python的目标
* [Python in Education: Teach, Learn, Program](http://www.oreilly.com/programming/free/python-in-education.csp) - 关于Python为何非常适合教育的免费电子书
* ['Think Python like a Computer Scientist' book Foreword](http://interactivepython.org/courselib/static/thinkcspy/FrontBackMatter/foreword.html) 像计算机科学家一样思考Python （By David Beazley）
* [Why I push for Python](http://lorenabarba.com/blog/why-i-push-for-python/) 我为何推崇python （by Lorena Barba）
* [Why Python is a Great First Language](http://blog.trinket.io/why-python/) 为什么Python是优秀的第一语言(入门语言) （by Elliott Hauser (Trinket CEO)）
* [Why Python is a great language for teaching beginners in introductory programming classes](http://pgbovine.net/python-teaching.htm) 对处在编程入门课程的初学者而言，为何python是一门优秀的语言 (by Philip Guo)
* [Python is Now the Most Popular Introductory Teaching Language at Top U.S. Universities](http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-u-s-universities/fulltext) Python现在是美国顶尖大学最热门的入门教学语言 （by Philip Guo (Communications of the ACM)）
* [Why Learn Python? Here Are 8 Data-Driven Reasons](https://dbader.org/blog/why-learn-python)：为什么学习Python？ 这里有8个数据驱动的原因 （by Elena Ruchko）
* [[Level 1] Programming: Python](http://web.archive.org/web/20160122210606/http://nzacditt.org.nz/resources/programming-and-cs/level-1-programming-python) 一份资源列表(一级/入门课程) - Archived version
* [Python as a way of thinking](http://allendowney.blogspot.com/2017/04/python-as-way-of-thinking.html) : 将python作为一种思考方式,现代编程语言（如Python）与第一代语言（如FORTRAN和C）在有质所不同，使其成为教学，学习，探索和思考的有效工具
* [Academic Papers](papers.md): 一份学术论文列表

### 参考

* [Official Python documentation](https://docs.python.org/3/) ： Python官方文档
* [Python in Education](http://pythonineducation.org/) - [git repo](https://github.com/python/pythonineducation.org) : python基金会下边的教育网站，涉及软件和硬件内容
* [Google's Python Class](https://developers.google.com/edu/python/) : Google开设的python教学班
* [The Hitchhiker’s Guide to Python](http://python-guide.org/) : Python漫游指南，极佳的资源导览，涵盖大多数编程话题，适合不时拿出来翻一翻
* [Tiny Python 3.6 Notebook](https://github.com/mattharrison/Tiny-Python-3.6-Notebook/blob/master/python.rst) :  一本小册子，方便快速参考语法
* [First Steps With Python](https://realpython.com/learn/python-first-steps/) 开启你的python之旅，手把手带你入门
* [PEP8 - Python Style Guide](http://pep8.org/) : Python编码风格指南
* [The Elements of Python Style](https://github.com/amontalenti/elements-of-python-style) : 讨论如何写出更好的代码
* [PyMOTW3](https://pymotw.com/3/) - 关于使用内置模块的教程
* [Full Stack Python](http://www.fullstackpython.com/table-of-contents.html) - [(best python resources)](https://www.fullstackpython.com/best-python-resources.html) : 一份python全栈的资源列表与引导
* [Learn X in Y minutes where X=python3](https://learnxinyminutes.com/docs/python3/) : Learn X in Y minutes系列，比较干(适合有编程基础的同学)
* [PyCrumbs - Bits and bytes of Python from the Internet](https://github.com/kirang89/pycrumbs): 资源列表
* [EduPython](http://edupython.co.uk/) - 使用blockly生成python，进而控制minecraft
* [A gallery of interesting IPython Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks) - 一些有趣的IPython Notebooks汇总
* [CS1 Python Programming Projects Archive](http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/index.php) 一门课程 基于知识共享协议发布
* [Python cheatsheet](https://www.pythonsheets.com/) python小抄
* [Python Crash Course - Cheat Sheets](http://ehmatthes.github.io/pcc/cheatsheets/README.html) 一堆的小抄
* [Algorithms implemented in python (for education)](https://github.com/TheAlgorithms/Python) python实现的各类算法(源码)
* [Algorithms](https://github.com/nryoung/algorithms) 算法的python实现
* [Minimal examples of data structures and algorithms in Python](https://github.com/keon/algorithms) 数据结构与算法的python实现(最小例子)
* [awesome-python](https://github.com/vinta/awesome-python) - python资源列表（awesome系列）
* [Python GitHub Projects](https://github.com/checkcheckzz/python-github-projects) - python资源列表
* [pycrumbs](https://github.com/kirang89/pycrumbs) - python资源列表
* [Python Reference](https://github.com/rasbt/python_reference) - python资源列表
* [Pythonidae](https://github.com/svaksha/pythonidae) - 科学计算方便的python资源
* [python-patterns](https://github.com/faif/python-patterns) - python与设计模式(很全面)
* [PyPattyrn](https://github.com/tylerlaberge/PyPattyrn) 常见设计模式的python实现
* [Python 3 Patterns, Recipes and Idioms](http://python-3-patterns-idioms-test.readthedocs.io/) 常见的设计模式，适合中级程序员
* [How to make mistakes in Python](http://www.oreilly.com/programming/free/files/how-to-make-mistakes-in-python.pdf)   从典型错误中学习
* [Python Knowledge Base](https://www.quantifiedcode.com/knowledge-base/) Python和流行的Python框架的最佳实践和反模式的集合
* [Python IAQ: Infrequently Answered Questions](http://norvig.com/python-iaq.html) 罕见问题与答案 (by Peter Norvig)
* [Anti-Patterns in Python Programming](http://lignos.org/py_antipatterns/) - Python编程中的反模式
* [DjangoGirls Introduction to Python](https://tutorial.djangogirls.org/en/python_introduction/) djangogirls项目中的python教程
* [Experiments in Python Pedagogy](https://github.com/4dsolutions/Python5) - [rendered version](http://nbviewer.jupyter.org/github/4dsolutions/Python5/tree/master/) python教学实践
* [29 common beginner Python errors on one page](http://pythonforbiologists.com/index.php/29-common-beginner-python-errors-on-one-page/) 29种常见的Python初学者错误
* [Learn Python - Udacity](https://www.udacity.com/learn/python) Udacity上的pyhton入门
* [Popular Python Recipes](http://code.activestate.com/recipes/langs/python/) 一些流行的代码片段
* [Transforming Code into Beautiful, Idiomatic Python](https://gist.github.com/JeffPaine/6213790) - 一些让代码更优雅的技巧
* [Improve your Python skills (Dan Bader's blog)](https://dbader.org/blog/) 提升你的python技巧
* [Practical Business Python](http://pbpython.com/) 一些在真实业务中使用的python代码
* [Python Lessons](http://teachwithict.weebly.com/python.html) - 来自teachwithict的6门课程

### 邮件列表

* [Python EDU-SIG](https://www.python.org/community/sigs/current/edu-sig/) - Python.org subsite
* [Python EDU-SIG](https://mail.python.org/mailman/listinfo/edu-sig) - Special Interest Group mailing list
* [Python EDU-WG](https://mail.python.org/mailman/listinfo/pythonedu-wg) - Working Group mailing list
* [Tutor](https://mail.python.org/mailman/listinfo/tutor) - (mailing list) Discussion for learning programming with Python
* [Python-list](https://mail.python.org/mailman/listinfo/python-list) - General discussion list for the Python programming language (mailing list)

### 论坛

* StackOverflow: [dashboard](http://stackoverflow.com/documentation/python) - [all topics](http://stackoverflow.com/documentation/python/topics) - [tag python](http://stackoverflow.com/questions/tagged/python) - (community website)[https://sopython.com/]
* reddit: [Python](https://www.reddit.com/r/Python/) - [Python Learning](https://www.reddit.com/r/learnpython/) - [Python tips](https://www.reddit.com/r/pythontips/) - [Pygame](https://www.reddit.com/r/pygame/)

## 工具与库

* [Your Python Trinket](https://trinket.io/python) - 将交互式的python放到网络上的任何地方
* [Python Tutor](http://pythontutor.com/) - 可视化python代码的运行
* [Skulpt](http://www.skulpt.org/) - Skulpt是一个完全基于浏览器的Python运行环境
* [SoloLearn Python 3 Tutorial](https://www.sololearn.com/Course/Python/) - python3入门，可在移动端访问 
* [Python Anywhere](https://www.pythonanywhere.com/details/education) Python Anywhere是一个基于Python语言的在线集成开发环境（IDE）和Web托管服务
* [repl.it](https://repl.it/site/languages/python3) python3的线上IDE
* [Python AST Explorer](https://python-ast-explorer.com/) python抽象语法树查看工具
* [kite](https://kite.com/) - 一款让程序员编程更智能的开发工具
* [EarSketch](https://earsketch.gatech.edu/) - 通过创作音乐来学编程
* [Ren'Py](https://www.renpy.org/) - 视觉小说引擎,允许任何人高效地编写大型视觉小说.Ren'Py几乎支持所有视觉小说所应该具有的功能，包括分支故事、储存和载入游戏、回退到之前故事的储存点、多样性的场景转换等

### 游戏，图形与仿真

* [PyGame](http://www.pygame.org/) : 专为电子游戏设计。包含图像、声音。创建在SDL基础上，允许实时电子游戏研发而无需被低级语言，如C语言或是更低级的汇编语言束缚
* [Pygame Zero](https://pygame-zero.readthedocs.io) 一个脚手架，方便创建2D游戏
* [Python Arcade Library](http://pythonhosted.org/arcade/) : 简单易学的一个2游戏框架
* [Pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home) - 一个纯python实现的跨平台游戏框架，没有额外的依赖包
* [Python Mode for Processing](http://py.processing.org/): Processing不仅仅是一种单一的语言，而是以艺术为导向的方法来学习，教学和编写代码
* [PythonTurtle](http://pythonturtle.org/) : 通过移动屏幕上的Turtle(乌龟)来学编程，有悠久的历史，PythonTurtle是完全独立的，不需要Python
* [VPython](http://vpython.org/) - VPython可以轻松创建可导航的3D演示和动画
* [Pymunk](http://www.pymunk.org/) - 2D 物理效果 library
* [PyPhysicsSandbox](https://github.com/jshaffstall/PyPhysicsSandbox) - 对 Pymunk的简单包装
* [Kivy](https://kivy.org/) - 用于开发采用自然用户界面的多点触控应用软件。它可以在Android，iOS，Linux，OS X和Windows执行
* [Panda3D](http://www.panda3d.org/) - Panda3D 是一个游戏引擎，也是一个 3D 渲染和游戏开发框架
* [gui zero](https://lawsie.github.io/guizero/) - 让孩子们能快速上手GUI编程

### 可视化

* [Bokeh](http://bokeh.pydata.org/) : 使用现代web技术来进行大数据集的可视化展示的交互环境的Python包
* [VisPy](http://vispy.org/) : Vispy 是一个高性能的交互式 2D/3D 的数据可视化库。利用图形处理器 GPU 通过 OpenGL 库来显示非常大的数据集

### Jupyter

* [Project Jupyter](http://jupyter.org/) : jupyter 是把 IPython 和 Python 解释器剥离后的产物，独立发行。jupyter 可以和 Python 之外的 程序结合，提供强大的服务
* [Jupyter Notebook cheatsheet](https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/) : jupyter Notebook的小抄(cheatsheet)，方便随时查阅常用操操作
* [IPython widgets](https://github.com/ipython/ipywidgets) : ipython notebook的插件系统
* [nbgrader](http://nbgrader.readthedocs.io/) - nbgrader是一种便于在Jupyter notebook中创建和为作业评分的工具。
* [nbval](https://github.com/computationalmodelling/nbval) -  用于检验 Jupyter notebooks 的 Py.test 插件
* [nbdime](https://nbdime.readthedocs.io/) - diff与merge Jupyter Notebooks.
* [nbscan](https://github.com/conery/nbscan) - search for and print contents of cells in Jupyter notebooks.
* [nbconvert](https://nbconvert.readthedocs.io/) - 将 Notebooks 转为其他格式(我喜欢用它来做PPT).
* [nbautoeval](https://github.com/parmentelat/nbautoeval) - 创建自动评估的练习.
* [nbtutor](https://github.com/lgpage/nbtutor) - 逐行将python代码的运行过程可视化.
* [nbtranslate](https://github.com/devrt/nbtranslate) - 使用gettext 来翻译 Jupyter notebook上的内容
* [nbTranslate](https://github.com/jfbercher/jupyter_nbTranslate) -  将notebook单元格的内容从一种语言翻译到另一种 （支持多语言）
* [jupyter-drive](https://github.com/jupyter/jupyter-drive) - Google Drive for Jupyter.
* [Jupyter tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/) Jupyte 的使用小技巧
* [Notebook Gallery](http://nb.bianp.net/sort/views/) - 优质 IPython/Jupyter Notebooks汇总
* [Custom Jupyter Notebook Themes](https://github.com/dunovank/jupyter-themes) : jupyter的其他主题
* [IPythonBlocks](http://ipythonblocks.org/) : 为学生提供可以使用Python操作的彩色块的网格,让学生练习流程控制和其他方面的程序设计,并对他们的代码正在做的即时，可视化的反馈.甚至可以动画循环，向学生展示每一步都发生了什么变化
* [Using the IPython Notebook as a Teaching Tool](https://software-carpentry.org/blog/2013/03/using-notebook-as-a-teaching-tool.html) : 将IPython Notebook用作教学工具
* [Teaching with Jupyter Notebooks](https://groups.google.com/forum/#!forum/jupyter-education) - 使用Jupyter Notebooks来教学（邮件列表）.
* [JupyterLab computational environment](https://github.com/jupyterlab/jupyterlab) - 使jupyter notebook更接近IDE
* [binder](http://mybinder.org/) - 将一个github库变为一系列的交互式notebook.
* [JupyterHub](https://github.com/jupyterhub/jupyterhub) - Jupyter notebooks的多用户系统
* [Lectures on scientific computing with Python](https://github.com/jrjohansson/scientific-python-lectures) 使用python做科学计算的讲座
* ["The world of Jupyter" —a tutorial](https://github.com/barbagroup/jupyter-tutorial) jupyter入门教程
* [List of Jupyter Notebooks by Peter Norvig](http://norvig.com/ipython/) Jupyter Notebooks的一份资源汇总
* [28 Jupyter Notebook tips, tricks and shortcuts](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/) Jupyter Notebook使用技巧

### IDEs

* [bpython](https://bpython-interpreter.org/):bpython是轻量级的Python解析器，同时包含了常见的IDE功能。功能包括语法高亮，预计参数列表、自动缩进和自动补全
* [ptpython](https://github.com/jonathanslenders/ptpython) 较ipython轻量，较bpython好用,有许多贴心的操作细节
* [Thonny, Python IDE for beginners](http://thonny.cs.ut.ee/) : 适用初学者的Python IDE （Thonny内置了Python 3.6）,轻松地安装第三方软件包
* [VIM](http://www.vim.org/) with [Python plugins](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/) : Vim是从vi发展出来的一个文本编辑器。代码补完、编译及错误跳转等方便编程的功能特别丰富，在程序员中被广泛使用。和Emacs并列成为类Unix系统用户最喜欢的编辑器(ps:我平时主要用VIM)
* [Emacs](https://www.gnu.org/software/emacs/) with [Python plugins](https://realpython.com/blog/python/emacs-the-best-python-editor/) : 具有强大的可扩展性，Emacs是黑客们关于编辑器之战的两大主角之一（另一个是VIM）
* [Sublime Text 3](http://www.sublimetext.com/3) with [Python plugins](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/):Sublime Text 是一套跨平台的文本编辑器，支持基于Python的插件，界面好看，对新手友好
* [PyCharm Edu](https://www.jetbrains.com/pycharm-edu/) - With [some courses](https://github.com/JetBrains/pycharm-courses) : -它提供了代码分析、图形化调试器，集成测试器、集成版本控制系统，并支持使用Django进行网页开发
* [Spyder](https://github.com/spyder-ide/spyder) - Spyder（前身为Pydee）是一个使用Python语言的开放源代码跨平台科学运算IDE。Spyder集成了NumPy，SciPy，Matplotlib与IPython等
* [Wingware Python IDE](https://wingware.com/) : 商业软件，调试器是类VC/eclipse
* [Ninja-IDE](http://ninja-ide.org/) : NINJA-IDE是一款开源软件（GPLv3许可），是使用Python和Qt开发
* [PyDev](http://www.pydev.org/) : 该项目实现了一个功能强大的 Eclipse插件，用户可以完全利用 Eclipse 来进行 Python 应用程序的开发和调试
* [Visual Studio Code](https://code.visualstudio.com/) with [Python plugins](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python) : Visual Studio Code 基于 Electron 开发,轻巧好用

### 调试器

* [pdb](https://docs.python.org/3/library/pdb.html) : pdb 是 python 自带的一个包，为 python 程序提供了一种交互的源代码调试功能，主要特性包括设置断点、单步调试、进入函数调试、查看当前代码、查看栈片段、动态改变变量的值等
* [ipdb](https://pypi.org/project/ipdb/):ipdb提供了自动补全
* [PuDB](https://pypi.org/project/pudb/):它在终端里融合了一个迷你图形界面.有几个面板来追踪当前的本地变量，栈，和存在的断点
* [pdb++](https://bitbucket.org/antocuni/pdb/src):扩展了pdb
* [Python Linter Online](http://pythonbuddy.com/) - 语法在线检查（在线运行）
* [PyTA](https://github.com/pyta-uoft/pyta) - 帮助学生发现和修复常见的错误
* [coala](http://coala.io/) - 发现与处理代码问题
* [wdb](https://github.com/Kozea/wdb) - 基于web的调试器（使用WebSockets）

## 会议与视频

* [Weekly Python Chat](http://www.weeklypython.chat/) - 每周一起的线上视频交流，关于python/技术/开源
* [Python in Australian Education seminar](https://2016.pycon-au.org/programme/python_in_education_seminar) (2016) : 澳大利亚教育研讨会中的Python
* [PyCon Australia 2015 Education Miniconf](https://www.youtube.com/playlist?list=PLs4CJRBY5F1I5vuApyUXp6bLWly1E-b0s) youtube 播放列表
* [Python Education Summit Schedule](https://us.pycon.org/2016/events/edusummit/schedule/) (PyCon 2016)
* [A one-day mini-conference about Python in Education](http://2016.pyconuk.org/teachers/) (PyConUK 2016)
* [PyVideo tag 'education'](http://pyvideo.org/tag/education/)
* [Khan Academy Computer Science (Python video playlist)](https://www.youtube.com/playlist?list=PL36E7A2B75028A3D6)
* [Python Programming in one video](https://www.youtube.com/watch?v=N4mEzFDjqtA) - [Learn to Program with Python](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt) Derek Banas playlist
* [CPython internals: A ten-hour codewalk through the Python interpreter source code](http://pgbovine.net/cpython-internals.htm)
* [Teaching Python: The Hard Parts](http://pyvideo.org/pycon-us-2016/elana-hashman-teaching-python-the-hard-parts-pycon-2016.html) - PyCon 2016
* [Episode 14 – Allen Downey on Teaching Computer Science with Python](https://www.podcastinit.com/episode-14-allen-downey-on-teaching-computer-science-with-python/) from [podcast.\__init__('Python')](https://www.podcastinit.com/)
* [Python For Informatics](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj4JXIwMwN1_ss1Tk8wZShEJ)
* [Python for Everybody - Exploring Information](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p)
* [sentdex youtube playlists](https://www.youtube.com/user/sentdex/playlists) or via [Python Programming](https://pythonprogramming.net/)
* [Dan Bader's youtube channel](https://dbader.org/youtube/)
* [Python 3.4 Programming Tutorials](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_)
* [Programming Foundations with Python](https://www.youtube.com/playlist?list=PLAwxTw4SYaPnYajEbZvqtcVWQ6XGhvtOW) from [Udacity](https://www.udacity.com/course/ud036)
* [PySide Video Tutorials](http://wiki.qt.io/PySide_Video_Tutorials)
* [Python Basics - Coding is for girls](https://www.youtube.com/playlist?list=PLbd_WhypdBbAMyFfKgSj27JO7CEpuIcEK)
* [Python For Beginners - Learn To Code Tutorials ](https://www.youtube.com/playlist?list=PLW_tdZJKynZXgLKQAR2g52ut4c2IpUmOv)
* [TheNewBoston Python 3 videotutorials](https://thenewboston.com/videos.php?cat=98) - also [Flask](https://thenewboston.com/videos.php?cat=362) and others
* [Build applications in Python the antitextbook](https://www.youtube.com/playlist?list=PL41psiCma00wwvtQyLFMFpzWxUYmSZwZy)
* [Socratica Python Programming Tutorials](https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-)
* [Python for Data Analysis - Pandas Cookbook](https://www.youtube.com/playlist?list=PLyBBc46Y6aAz54aOUgKXXyTcEmpMisAq3)

## 书籍

* [The Computer Science Field Guide](http://www.csfieldguide.org.nz/en/) - ([repo](https://github.com/uccser/cs-field-guide))
* [Awesome Python Books](https://github.com/Junnplus/awesome-python-books)
* [PythonBooks](http://pythonbooks.revolunet.com/)
* [Build applications in Python the antitextbook](http://github.com/thewhitetulip/build-app-with-python-antitextbook)
* [Algorithmic Problem Solving with Python](http://www.eecs.wsu.edu/~schneidj/PyBook/swan.pdf)
* [Openlibra: Python](https://openlibra.com/en/collection/search/category/python/language/english/)
* [Python Practice Book](http://anandology.com/python-practice-book/)
* [Scipy Lecture Notes](http://www.scipy-lectures.org/)
* [Natural Language Processing with Python](http://www.nltk.org/book/)
* [Problem Solving with Algorithms and Data Structures using Python](http://interactivepython.org/courselib/static/pythonds/index.html)
* [Python for Everybody - Exploring Data In Python 3](http://www.py4e.com/book)
* [Composing Programs](http://composingprograms.com/)
* [Dive into Python 3](http://getpython3.com/diveintopython3/)
* [Introduction to Programming with Python](http://opentechschool.github.io/python-beginners/en/)
* [Learn Python, Break Python - A Beginner's Guide to Programming](http://learnpythonbreakpython.com/)
* [Learn Python3 in Y minutes](https://learnxinyminutes.com/docs/python3/)
* [Non-Programmer's Tutorial for Python 3](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3)
* [The Art and Craft of Programming (Python edition)](http://troll.cs.ua.edu/ACP-PY/)
* [Program Arcade Games With Python And Pygame](http://programarcadegames.com/)
* [Python for you and me](http://pymbook.readthedocs.io/en/py3/)
* [Object-Oriented Programming in Python](http://python-textbok.readthedocs.io)
* [Violent Python. A Cookbook for Hackers, Forensic Analysts, Penetration Testers and Security Engineers](http://store.elsevier.com/Violent-Python/TJ-OConnor/isbn-9781597499576/)
* [Natural Language Processing with Python – Analyzing Text with the Natural Language Toolkit](http://www.nltk.org/book/)
* [Python for Scientists and Engineers](http://pythonforengineers.com/python-for-scientists-and-engineers/)


ps:下边是一些出版社的书，我就不翻译了，如果有同学知道对应的中文版，欢迎pr

### Coding Club books

* [Python Basics](http://www.codingclub.co.uk/book1_home.php)
* [Python Next Steps](http://www.codingclub.co.uk/book2_home.php)
* [Python: Building Big Apps](http://www.codingclub.co.uk/book3_home.php)
* [Python: Programming Art](http://www.codingclub.co.uk/book4_home.php)
* [Python: Interactive Adventures](http://www.codingclub.co.uk/book5_home.php)
* [Black Flag: A Coding Club Mission](http://www.codingclub.co.uk/black_flag.php)
* [Coding Cards](http://www.codingclub.co.uk/codecards/CC-CodeCards.pdf) [PDF]

### Green Tea Press

* [Think Python: How To Think Like a Computer Scientist, 2nd ed.](http://greenteapress.com/thinkpython2/html/)
* [Think Complexity: Exploring Complexity Science with Python, 2nd ed.](http://greenteapress.com/complexity2/html/)
* [Think DSP: Digital Signal Processing in Python](http://greenteapress.com/thinkdsp/html/)
* [Think Stats: Exploratory Data Analysis in Python, 2nd ed.](http://greenteapress.com/thinkstats2/html/)
* [Think Bayes: Bayesian Statistics in Python](http://www.greenteapress.com/thinkbayes/html/)

### Invent with Python series

* [Invent your own computer games with Python](https://inventwithpython.com/)
* [Making Games with Python & Pygame](https://inventwithpython.com/pygame/)
* [Hacking Secret Ciphers with Python](http://inventwithpython.com/hacking/)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

### Manning Publications

* [Hello! Python](https://www.manning.com/books/hello-python)
* [Hello World! 2nd ed. Computer Programming for Kids and Other Beginners](https://www.manning.com/books/hello-world-second-edition)
* [Hello Raspberry Pi!](https://www.manning.com/books/hello-raspberry-pi) - Python programming for kids and other beginners.
* [The Quick Python Book, Third Edition](https://www.manning.com/books/the-quick-python-book-third-edition)
* [Learn Programming with Python](https://www.manning.com/books/learn-programming-with-python)
* [Grokking Algorithms](https://www.manning.com/books/grokking-algorithms) - An illustrated guide for programmers and other curious people.

### No Starch Press

* [Python for Kids](https://www.nostarch.com/pythonforkids)
* [Teach Your Kids to Code](https://www.nostarch.com/teachkids)
* [Doing Math with Python: Use Programming to Explore Algebra, Statistics, Calculus, and More!](https://www.nostarch.com/doingmathwithpython)
* [Python Crash Course. A Hands-On, Project-Based Introduction to Programming](https://www.nostarch.com/pythoncrashcourse)
* [Python Playground. Geeky Projects for the Curious Programmer](https://www.nostarch.com/pythonplayground)
* [Learn to Program with Minecraft. Transform Your World with the Power of Python](https://www.nostarch.com/programwithminecraft)
* [Black Hat Python. Python Programming for Hackers and Pentesters](https://www.nostarch.com/blackhatpython)

### O'Reilly

* [Raspberry Pi Cookbook. Software and Hardware Problems and Solutions](http://shop.oreilly.com/product/0636920045182.do)
* [Head First Python, 2nd Edition](http://shop.oreilly.com/product/0636920036777.do)
* [Python for Unix and Linux System Administration](http://shop.oreilly.com/product/9780596515829.do) (2008)

### Packt Pub

* [Python Projects for Kids](https://www.packtpub.com/application-development/python-projects-kids)
* [Raspberry Pi Projects for Kids](https://www.packtpub.com/hardware-and-creative/raspberry-pi-projects-kids-second-edition)
* [Python Programming for Arduino](https://www.packtpub.com/application-development/python-programming-arduino)
* [Pro Python System Administration](http://www.apress.com/us/book/9781430226055) (2010)

## 硬件

* [Cozmo](https://developer.anki.com/) : 评价极高的一个机器人，有性格，有萌点。外形是一个小推土机，它拉着你一起玩游戏。它有一套完整的SDK，允许你通过编程来增强它

### 树莓派

* [Raspberry Pi](https://www.raspberrypi.org/)

  * [Getting Started with Minecraft Pi](https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/) : 在树莓派中开启你的Minecraft(我的世界)之旅
  * [Create a "Whac-a-block" game in Minecraft](https://www.raspberrypi.org/learning/minecraft-whac-a-block-game/) : 在Minecraft创造一个Whac-a-block游戏
  * [MagPi issues](https://www.raspberrypi.org/magpi-issues/) MagPi是一本致力于为树莓派爱好者提供建议和帮助的杂志月刊，这个链接里包含了它的历史版本

* [The Raspberry Pi Platform and Python Programming for the Raspberry Pi](https://www.coursera.org/learn/raspberry-pi-platform) : coursera上的一门课， 树莓派（Raspberry Pi）平台及其 Python 程序设计

### Arduino

* [Arduino and Python](http://playground.arduino.cc/Interfacing/Python) Arduino 与 Python(包括串口通信之类)
* [Using Python with Arduino](http://www.toptechboy.com/using-python-with-arduino-lessons/)：一个系列课程，使用Python与Arduino交互

### BBC microbit

* [The micro:bit Foundation](http://microbit.org/):micro:bit是一块开放的开发板,允许运行代码，连接任何类型硬件。你可以利用BBC micro:bit实现任何酷炫的小发明，无论是机器人还是乐器.micro:bit拥有25个可显示消息的红色LED灯；有两个可编程按钮，也可以检测动作并且告知你动作进行的方向，同时它也可以通过低功耗蓝牙模块与其它设备或因特网互联。
* [BBC micro:bit MicroPython](https://microbit-micropython.readthedocs.io):micro:bit的文档

### PyBoard

* [MicroPython](http://micropython.org/) : MicroPython是Python3的精简版实现，包括Python标准库的一个子集，运行在微控制器和约束环境下。目前支持基于32-bit的ARM处理器

### ESP32
* [MicroPython](https://github.com/micropython/micropython-esp32)
