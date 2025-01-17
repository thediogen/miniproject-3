import Header from "./components/Header"
import { useEffect, useState } from "react";
import AuthenticateForm from "./components/AuthenticateForm";
import RegistrationForm from "./components/RegistrationForm";
import CreateProductForm from "./components/CreateProductForm";
import Advertisements from "./Advertisements";


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


function checkToken() {
  const cookies = document.cookie.split("; ");
  for (const cookie of cookies) {
    const [key, value] = cookie.split("=");
    if (key === 'access_token') {
        return value;
      }
    }
  return null;
}

async function getUsername(token){
  let form_data = new FormData()

  form_data.append('token', token)

  const options = {
      method: 'POST',
      body: form_data
  }

  let response = fetch('http://127.0.0.1:8000/get_user', options)
      .then((response) => {
          console.log(response.status)
          if (response.ok){
              return response.json()
          }

          alert(`Registration error: Some data is invalid\n\n
              Error status: ${response.status}\n
              Error text: ${response.statusText}
          `)

          throw Error(response)
      })
      .then((data) => {
          return data
      })
      .catch((err) => console.log());

  return await response
}


function App() {
  const [pageContent, setPageContent] = useState(null);
  const [username, setUsername] = useState(null);
  const [userType, setUserType] = useState(null);

  const contents = {
    'choose_auth': (<div>
      <h1>You are not authenticated</h1>
      <p>Ах ти Тоха, хтів не автентифікований пройти</p>

      <div>
        <a onClick={() => {setPageContent('authenticate')}}>Authenticate</a>
        <a onClick={() => {setPageContent('registration')}}>Registration</a>
      </div>
    </div>),
    'authenticate': <AuthenticateForm />,
    'registration': <RegistrationForm />,
    'default': (
      <div>
        <header>
          <h1>Hello, {username}!</h1>
          <nav>
            <a href="">Our Chat</a>
            {userType == 'seller' ? <a onClick={() => {setPageContent('create_product')}}>Create New Product</a> : ''}
            <a style={{color: 'red'}} onClick={() => {
              let choose = confirm('Are you sure you want to log out?')
              if (choose == true){
                clearCookies(); location.reload()
              }
            }}>Log Out</a>
          </nav>
        </header>
        <Advertisements />
      </div>
    ),
    'create_product': <CreateProductForm />,
  }

  useEffect(() => {

      const authentication = () => {
        let access_token = checkToken();

        if (access_token === null) {
          setPageContent('choose_auth')
        } else {
          
          let form_data = new FormData()

          form_data.append('token', access_token)

          const options = {
              method: 'POST',
              body: form_data
          }

          let response = fetch('http://127.0.0.1:8000/get_user', options)
              .then((response) => {
                  if (response.ok){
                      return response.json()
                  }

                  alert(`Registration error: Some data is invalid\n\n
                      Error status: ${response.status}\n
                      Error text: ${response.statusText}
                  `)

                  throw Error(response)
              })
              .then((data) => {
                  setUsername(data['username'])
                  setUserType(data['user_role'])
              })
              .catch((err) => console.log());
              setPageContent('default')
                }
              }

      authentication()
  }, [checkToken]);


  return contents[pageContent]
}

export default App
