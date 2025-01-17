function clearCookies() {
    // Отримуємо всі cookies
    const cookies = document.cookie.split(";");
  
    // Видаляємо кожен cookie
    for (const cookie of cookies) {
      const eqPos = cookie.indexOf("=");
      const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
  
      // Встановлюємо термін дії у минуле
      document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
    }
  }

  
function sendData(email, password){
    const auth_form = {
        'email': email,
        'password': password
    }

    const form_data_json = JSON.stringify(auth_form)
    let form_data = new FormData()

    // clearCookies()

    form_data.append('form_data', form_data_json)

    const options = {
        method: 'POST',
        body: form_data
    }

    let response = fetch('http://127.0.0.1:8000/authenticate', options)
        .then((response) => {
            if (response.status == 200){
                return response.json()
            }

            alert(`Authentication error: Email or password is incorrect\n\n
                Error status: ${response.status}\n
                Error text: ${response.statusText}
            `)

            throw new Error(response)
        })
        .then((data) => {
            document.cookie = `access_token=${data['access_token']}`
            window.location.reload()
        })
        .catch((err) => console.log());
}


function AuthenticateForm() {
    return (
        <div className="form">
            <h1>Seems like you are not authenticated</h1>

            <div>
                <input type="email" id="email" placeholder="Enter your email" /><br /><br />
                <input type="password" id="password" placeholder="Enter your password" /><br /><br />

                <button onClick={() => {
                    let email = document.getElementById('email').value
                    let password = document.getElementById('password').value

                    sendData(
                        email,
                        password
                    )
                }}>Authenticate</button>
            </div>

            <a href=""></a>
        </div>
    )
}

export default AuthenticateForm
