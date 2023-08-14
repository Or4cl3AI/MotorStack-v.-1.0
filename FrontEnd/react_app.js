import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './design.css';

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [audio, setAudio] = useState('');

  const handleInputChange = (event) => {
    setInput(event.target.value);
  };

  const handleChatSubmit = (event) => {
    event.preventDefault();

    axios.post('/api/chat', { input })
      .then(res => {
        setResponse(res.data.text);
        setAudio(res.data.audio);
      })
      .catch(err => console.error(err));
  };

  useEffect(() => {
    const audioElement = new Audio(audio);
    audioElement.play();
  }, [audio]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to MotorStack</h1>
      </header>
      <main>
        <form onSubmit={handleChatSubmit}>
          <input type="text" value={input} onChange={handleInputChange} />
          <button type="submit">Chat</button>
        </form>
        <div className="response">
          <p>{response}</p>
        </div>
      </main>
    </div>
  );
}

export default App;