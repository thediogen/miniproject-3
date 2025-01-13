import React from "react"


function sendData(email, password){
    const auth_form = {
        'email': email,
        'password': password
    }

    const form_data_json = JSON.stringify(auth_form)
    let form_data = new FormData()

    form_data.append('form_data', form_data_json)

    const options = {
        method: 'POST',
        body: form_data
    }

    let response = fetch('http://127.0.0.1:8000/authenticate', options)
        .then((response) => response.json())
        .then((data) => {console.log(document.cookie)})
        .catch((err) => console.log(err));
}


function AuthenticateForm() {
    return (
        <div className="form">
            <h1>Seems like you are not authenticated</h1>
            <p>Ах ти Тоха, хтів не автентифікований пройти</p>

            <div>
                <input type="text" id="email" placeholder="Enter your email" /><br /><br />
                <input type="text" id="password" placeholder="Enter your password" /><br /><br />

                <button onClick={() => {
                    let email = document.getElementById('email').value
                    let password = document.getElementById('password').value

                    sendData(
                        email,
                        password
                    )
                }}>Authenticate</button>
            </div>
        </div>
    )
}

export default AuthenticateForm
