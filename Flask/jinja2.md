## jinja2 언어


***

시작하기 전에 

동적 웹페이지의 종류는 3개가지가 있다. 

* CSR : Client-side rendering
  * javascript를 이용한 html작성
* SSR : Server-side rendering
  * server에서 html을 만들어 보내준다.
  * jinja2
* 복합적
  * 2개를 복합적으로 이용하는 방법
  * 서버에서 받아 ` `을 이용하여 html 붙이기

***

### 문법

* HTML 파일안에 {% python 문법 %}으로 작성을하며

* 서버에서 넘겨줄때 변수를 지정해서 보낸다. 

<br>

##### python

```angular2python
@app.route('/')
def main():
    myname = "sparta"
    return render_template("index.html", name=myname)
```

##### HTML

```angular2html
<h3>Hello, {{ name }}!</h3>
```