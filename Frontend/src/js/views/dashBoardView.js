
export const updateLiveData =async (dashboard) => {
    
    document.querySelector('.longitude').textContent= dashboard.channel_data.channel.longitude;
    document.querySelector('.latitude').textContent = dashboard.channel_data.channel.latitude;
 
}    



export const updateUserData = dashboard => {
     const path = 'C:/Anaconda/DjangoProjects/Aztech/';
    const total_path = path + dashboard.data.user_image;
    document.querySelector('.profile_image').src =    window.open(total_path, null);;
    document.querySelector('.username').textContent = dashboard.data.username;
    document.querySelector('.name').textContent =`Name: ${ dashboard.data.first_name} ${ dashboard.data.last_name}`; 
    document.querySelector('.email').textContent =`Email: ${ dashboard.data.email} `;
    document.querySelector('.mobile').textContent =`Mobile: ${ dashboard.data.mobile} `;
    document.querySelector('.devices').textContent =`Devices owned: ${ dashboard.data.devices.length} `;
    document.querySelector('.is_active').textContent =`Active: ${ dashboard.data.is_active} `;

}