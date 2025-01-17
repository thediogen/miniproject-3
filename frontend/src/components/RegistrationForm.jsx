
function sendData(username, email, password, user_role){
    const auth_form = {
        'username': username,
        'email': email,
        'password': password,
        'role': user_role
    }

    const form_data_json = JSON.stringify(auth_form)
    let form_data = new FormData()

    // clearCookies()

    form_data.append('form_data', form_data_json)

    const options = {
        method: 'POST',
        body: form_data
    }

    let response = fetch('http://127.0.0.1:8000/registration', options)
        .then((response) => {
            console.log(response.status)
            if (response.status == 200){
                return response.json()
            }

            alert(`Registration error: Some data is invalid\n\n
                Error status: ${response.status}\n
                Error text: ${response.statusText}
            `)

            throw Error(response)
        })
        .then((data) => {
            console.log(data)
            document.cookie = `access_token=${data}`
            window.location.reload()
        })
        .catch((err) => console.log());
}

function RegistrationForm() {
    return (
        <div className="form">
            <h1>Enter all the data to create new account</h1>

            <div>
                <input type="text" id="username" placeholder="Enter your username" required/><br /><br />
                <input type="email" id="email" placeholder="Enter your email" required/><br /><br />
                <input type="password" id="password" placeholder="Enter your password" required/><br /><br />
                <select name="user_role" id="user_role">
                    <option value="user">User</option>
                    <option value="seller">Seller</option>
                    <option value="admin">Admin</option>
                </select><br /><br />

                <button onClick={() => {
                    let email = document.getElementById('email').value
                    let password = document.getElementById('password').value
                    let username = document.getElementById('username').value
                    let user_role = document.getElementById('user_role').value

                    sendData(
                        username,
                        email,
                        password,
                        user_role
                    )
                }}>Authenticate</button>
            </div>
        </div>
    )
}

export default RegistrationForm