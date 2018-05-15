## 架构

<pre>
start
 |
 V
+--------------------+
|                    | start
|  electron          +-------------> +------------------+
|                    | sub process   |                  |
| (browser)          |               | python server    |
|                    |               |                  |
| (all html/css/js)  |               | (business logic) |
|                    |   zerorpc     |                  |
| (node.js runtime,  | <-----------> | (zeromq server)  |
|  zeromq client)    | communication |                  |
|                    |               |                  |
+--------------------+               +------------------+
</pre>

<pre>
|-- index.html
|-- main.js
|-- package.json
|-- renderer.js
|
|-- pycalc
|   |-- api.py
|   |-- calc.py
|   `-- requirements.txt
|
|-- LICENSE
`-- README.md
</pre>

## canvas坐标获取
```js
var x = event.clientX - canvas.getBoundingClientRect().left;
var y = event.clientY - canvas.getBoundingClientRect().top;

----------------

var x = event.offsetX
var y = event.offsetY
```


##Pantograph
> 通过命令行实现通信