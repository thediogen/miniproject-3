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


function sendData(title, price){
    const auth_form = {
        'title': title,
        'price': price,
    }

    const form_data_json = JSON.stringify(auth_form)
    let form_data = new FormData()

    // clearCookies()

    let access_token = checkToken()

    form_data.append('product', form_data_json)
    form_data.append('token', access_token)

    const options = {
        method: 'POST',
        body: form_data
    }

    let response = fetch('http://127.0.0.1:8000/create_product', options)
        .then((response) => {
            if (response.ok){
                return response.json()
            }

            alert(`Error: Some data is invalid\n\n
                Error status: ${response.status}\n
                Error text: ${response.statusText}
            `)

            throw Error(response)
        })
        .then((data) => {
            console.log('Data',data)
            location.reload()
        })
        .catch((err) => console.log());
}

function CreateProductForm() {
    return (
        <div>
            <h1>provide all the required data to create new product</h1>

            <div>
                <input type="text" placeholder="Enter product's title" id="title" required/><br /><br />
                <input type="number" placeholder="Enter product's price (in hrivnas ₴)" id="price"/><br /><br />

                <button onClick={() => {
                    let title = document.getElementById('title').value
                    let price = document.getElementById('price').value

                    sendData(title, price)
                }}>Create</button>
            </div>
        </div>
    )
}

export default CreateProductForm
