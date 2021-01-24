import axios from 'axios'
import $ from 'jquery'
import Dashboard from './models/Dashboard'
import Login from './models/Login'
import * as dashboardview from './views/dashBoardView'

const state = {};

const controlLiveData = async () => {
    state.dashboard = new Dashboard(7);
    await state.dashboard.getDetails();
    dashboardview.updateUserData(state.dashboard);
    
}
controlLiveData()

// document.querySelector('.login').addEventListener('click', e => {
//     e.preventDefault(); //it prevents the page to reload after hitting the search
//     var username = document.querySelector('.in_username').value;
//     var password = document.querySelector('.in_password').value;
//     state.login = new Login(username, password);
//     state.login.login();
    
//    // window.location.href = "http://localhost:8080/dashboard.html";
// });


// document.querySelector('.theft').addEventListener('click',async e => {
//     e.preventDefault();
//     state.dashboard = new Dashboard(7);
//     await state.dashboard.getDetails();
//     dashboardview.updateLiveData(state.dashboard);
//     dashboardview.updateUserData(state.dashboard);
//     showData();
//     showVideo();
//     showMap();

// } );
let editor;

  document.querySelector('.login').addEventListener('click', e => {
     e.preventDefault(); //it prevents the page to reload after hitting the search
     var data = CKEDITOR.instances.editor.getData();
    // var data = CKEDITOR.instances.editor.document.getBody().getText();
    var srcArray = [];
$(data).find('img').each(function(){
   var src = $(this).attr('src');
   srcArray.push(src);
});
console.log(data)
console.log(srcArray)
     var obj = {
         'data':data.replace(/<[^>]*>?/gm, '')
     }
     console.log(obj);
     document.querySelector('.test').innerHTML = obj.data;
    
});

// async function get(){
//     var api = await axios(`https://api.thingspeak.com/channels/946386/feeds.json?api_key=SU7JT9Q6J0R4S4XE`);
//     console.log(api);
// }
// get();
var i =0;
async function showData(){
    var channel = await axios(`https://api.thingspeak.com/channels/946386/feeds.json?api_key=SU7JT9Q6J0R4S4XE`);
    var channel_data = channel.data;
    console.log(channel_data.feeds.length);
    document.querySelector('.humidity').textContent = channel_data.feeds[i].field1;
    document.querySelector('.temperature').textContent = channel_data.feeds[i].field2;
    console.log(channel_data.feeds[i].field2);
    if(i < channel_data.feeds.length){
        i= i+1;
    
    }
    else{
        showVideo();        
        console.log(channel_data.feeds[i].field2);
        
    }
    var myVar = setTimeout(showData, 2000);
}

async function showVideo(){
    var video = document.querySelector(".videoElement");
 
    if (navigator.mediaDevices.getUserMedia) {       
        navigator.mediaDevices.getUserMedia({video: true})
      .then(function(stream) {
          video.srcObject = stream;
      })
      .catch(function(err0r) {
      console.log("Something went wrong!");
  });
}
}

async function showMap(){
    document.querySelector('.traffic').innerHTML = `<iframe width="500" height="200" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/946386/maps/channel_show?read_api_key=SU7JT9Q6J0R4S4XE&height=200">`;
}

  