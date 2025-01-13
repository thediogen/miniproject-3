import Header from "./components/Header"
import { useEffect, useState } from "react";
import AuthenticateForm from "./components/AuthenticateForm";


function App() {
  const [authStatus, setAuthStatus] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
      const fetchData = async () => {
          try {
              const response = await fetch('http://127.0.0.1:8000/get_user', {method: 'GET'});
              const result = await response.json();
              setAuthStatus(result['detail']);
          } catch (error) {
              console.log('ERR')
              console.error('Error fetching data:', error);
          } finally {
              setLoading(false);
          }
      };

      fetchData();
  }, []);

  if (loading) {
      return <div>Loading...</div>;
  } else {
    console.log(authStatus)
  }

  console.log('authStatus ', authStatus)

  if (authStatus == 'You are not authenticated'){
    return <AuthenticateForm />
  } else {
    return <Header />
  }
}

export default App
