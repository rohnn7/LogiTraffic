import axios from 'axios'
import $ from 'jquery'
export default class Login{
    constructor(username, password){
        this.username = username;
        this.password = password;
    }
    
    getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for(var i=0; i<ca.length; i++) {
           var c = ca[i];
           while (c.charAt(0)==' ') c = c.substring(1);
           if(c.indexOf(name) == 0)
              return c.substring(name.length,c.length);
        }
        return "";
    }

    async login(){
        // const url = await axios("http://127.0.0.1:8000/api/user/login/");
        // Authorize token - df3d17c151792dc2df0fd6269230bd003a05c547
        const data = {
            "username": this.username,
            "password": this.password
        };
        console.log(data);
        let csrftoken = this.getCookie('csrftoken');
        const POST = {
            method:'POST',
            headers:{                
                "accept": "application/json,  text/plain, */*",
                "origin":'http://localhost:8080',
                'content-type':'application/json',
                'x-requested-with': 'XMLHttpRequest',
                "x-csrftoken": csrftoken,
                'Authorization':'Token df3d17c151792dc2df0fd6269230bd003a05c547',
                // 'access-control-request-header':'http://localhost:8080',
                // 'Access-Control-Request-header': 'content-type'
            },
            body:JSON.stringify(data)

        };
        
        const response = await fetch('http://127.0.0.1:8000/api/user/login/', POST);
        const js = await response.json();
        console.log(js);
        this.pk = js.pk;
        // console.log(this.pk);

        // var action = () => {
        //     console.log('success');
        // }
        
        // var reject = () => {
        //     console.log('rejected');
        // }
        // $.ajax({
        //     url: 'api/user/login/',
        //     data: data,
        //     type: 'POST',
        //     beforeSend: function (xhr, settings) {
        //         xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
        //     },
        //     contentType:"application/json; charset=utf-8",
        //     processData: false,
        //     success: action,
        //     error: reject
        // });
    }
    
}