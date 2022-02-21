# Djnago-ninja 란

***

<br>

## 정의 

<br>

* `Django Framework` 에서 사용되는 Package로 API를 관리 할 수 있게 된다. 


<br>

## 사용시 주의 사항

* 기존에 알고 있던 `Django` 와는 다르게 `views` 함수를 짜야한다. 이유는 api/docs 를 만들어 주기 때문에 api를 쉽게 관리할 수 있고 테스트를 할 수 있다.
  * (기존)  `user/views.py`
    ```angular2python
    def home(request):
        data = Model.objects.filter(name='test')
        return render(request, 'home.html', { 'data': data })
    ```
  * (변경) `user/api/user_router`
    ```angular2html
    router = Router()
    
    @router.get('/')
    def home_api(request: HttpRequest):
        data = make_data(request.name)
        return data    
    ```

     `user/services/home_service`  
    ```angular2html
    def make_data(data):
        result = Model.object.filter(name = data)
        return result
    ```


