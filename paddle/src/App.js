import React, { useState, useEffect} from 'react';
import Game from './Game'

function App() {
    const [currentTime, setCurrentTime] = useState(0)
    const [counter, setCounter] = useState(0)
    useEffect(()=>{
      fetch('/time').then(res => res.json()).then(data => {
        setCurrentTime(data.time);
      });
    }, []);

    useEffect(()=>{
      fetch('/count').then(res => res.json()).then(data => {
        setCounter(data.count);
      });
    }, []);

  return (
    <div className="App">
      <p> Current time is {currentTime}, count is {counter}.</p>
      <Game width={450} height={650}/>
    </div>
  );
}

export default App;
