import axios from 'axios'

export default class Dashboard{
    constructor(pk){
        this.pk = pk;
    }

    async getDetails(){
        const userDetails = await axios(`http://127.0.0.1:8000/api/user/detail/${this.pk}`);
        this.data = userDetails.data;
        const device = await axios(`http://127.0.0.1:8000/api/device/detail/${this.data.devices[0].pk}`);
        this.device_detail = device.data;
        const channel = await axios(`https://api.thingspeak.com/channels/946386/feeds.json?api_key=SU7JT9Q6J0R4S4XE`);
        this.channel_data = channel.data;
        console.log(this.channel_data);
    }
};