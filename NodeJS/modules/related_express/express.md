# Express Module 

### Express 모듈은 기존의 http 모듈을 상용할 떄 불편함을 개선한 모듈로 훨씬 가독성이 좋게 API 를 개발 할 수 있다.

***


### 기본 코드

```javascript
// express 모듈 import
const express = require('NodeJS/modules/related_express/express');

// app 지정
const app = express();

// 포트 설정
app.set('port', 3000)

// req : http 요청
// res : http 응답
// 첫번째 인자는 Route 하게 될 URL 
app.get('/', (req, res) => {
    // res.send 는 여러번 보내면 안됨
    res.send('Hello');
})

// app.<method> 형식으로 사용
app.post('/about', (req, res) => {
    // 상태 코드를 넣어줄 수 도 있다.
    res.status(200).send('thsi is about')
})


// 포트를 열어주기 위한 설정 
app.listen(3000, () => {
    // 서버가 켜지면 실행되는 CALL Back 함수  
    console.log('Server is Run!!')
})

```

* 기존의 http 모듈 보다 훨씬 보기 좋고 API 를 구현 하기 간편 하다
* 위에서 아래로 router 를 확인하고 끝까지 실행이 됬음에도 매칭되는 게 없다면 
* not found 가 알아서 된다. 


***


### HTML 파일 서빙 하기

### 

```javascript
// Server.js


const express = require('NodeJS/modules/related_express/express');

// 경로 설정을 위한 path import
const path = require('NodeJS/modules/path');

const app = express();
app.set('port', 3000)

app.get('/', (req, res) => {
    // res.sendFile 을 통해 파일을 보내준다. 
    // 이때 경로는 상대 경로로 작성, 기준은 현재 파일 기준이다. 
    res.sendFile(path.join(__dirname, '<상대 경로>'))
})


app.listen(3000, () => {
    console.log('Server is Run!!')
});
```