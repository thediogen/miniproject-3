import { useState, useEffect } from "react"


function Advertisements() {
    const [products, setProducts] = useState([])

    useEffect(() => {
        const getAdvertisements = async () => {
            fetch('http://127.0.0.1:8000/get_products')
                .then((response) => response.json())
                .then((data) => {return data})
        }

        setProducts(getAdvertisements())
    }, [])

    console.log(products)

    return (
        <h1>Hello</h1>
    )
}


export default Advertisements
