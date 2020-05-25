
const auth_link = "https://www.strava.com/oauth/token"

function getActivites(res){

    const activities_link = `https://www.strava.com/api/v3/athlete/activities?access_token=${res.access_token}`
    fetch(activities_link)
        .then((res) => console.log(res.json()))
}

function reAuthorize(){
    fetch(auth_link,{
        method: 'post',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'

        },

        body: JSON.stringify({

            client_id: '48474',
            client_secret: 'd3c732f415aed84772905b0887deb81469236c02',
            refresh_token: 'de7449ac9f12cb69a36aca9c090ffa83c02cbbe3',
            grant_type: 'refresh_token'
        })
    })
    .then(res => getActivites(res))

}

reAuthorize()
