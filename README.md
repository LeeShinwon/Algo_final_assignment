# Algo_final_assignment: Maze Solver

> Solution should be sum of coins collected on the way out of maze.

> S : start point  ,     G : end point  ,     X : wall<br/>


##### [INPUT]
    maze text file
##### [OUTPUT]
    LEAST coins collected

##### [My Solution]

* 7X7 maze</br>
    Solution is  6+1+3+8+4+6+4+7+3+0+5 == 47</br>
<img width="144" alt="스크린샷 2023-05-31 오후 2 29 16" src="https://github.com/LeeShinwon/Algo_final_assignment/assets/82192923/f1e64f59-d28c-4036-be7b-e003db553e51"></br>

* 11X11 maze</br>
    Solution is 6+8+6+2+4+2+3+3+9+9+0+8+3+6+9+5+2+5+1+4+1+7+0
                </br>    +7+0+2+8+1+0+1+0+9+6+5+2+3+2+8+7+7+3+2+1+5+9 == 191</br>
<img width="215" alt="image" src="https://github.com/LeeShinwon/Algo_final_assignment/assets/82192923/ec210677-78df-4423-9f92-99b0962ee165"></br>

* 31X31 maze</br>
    1616
* 101X101 maze</br>
    2480


##### [TIME & SPACE complexity]
* time</br>
    bfs-queue(deque library)</br>
    This BFS code uses the visited list variable to visit only nodes that have not been visited before.</br>
    ##### => O(N)</br>
    
* space</br>
    f:TextIOWrapper</br>
    arr:list -> n^2</br>
    line:str</br>
    visited:list[list[bool]] -> n^2</br>
    i:int</br>
    sx,sy:int</br>
    dx,dy:list[int]</br>
    x,y:int</br>
    queue:deque -> n</br>
    nx,ny:int</br>
    
    ##### => O(n^2)</br>

##### [REFERENCED LINK]
* [Python File Read](https://wikidocs.net/26)
* [BFS maze problem](https://github.com/ndb796/python-for-coding-test/blob/master/5/11.py)



##### Shinwon Lee, Riga Technical University, Algorithms and Methods of Programming,2023.05.31
