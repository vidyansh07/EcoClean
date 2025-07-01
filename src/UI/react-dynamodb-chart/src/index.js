import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import * as AWS from 'aws-sdk'

const configuration = new AWS.Config({
  region: 'us-east-1',
  secretAccessKey: 'Ll2rTqPZbxPaT43+6TEIQDc2arPlsCAyueIzKbQ6',
  accessKeyId: 'AKIATN4ZTIGOLAMQUK2A'
})

AWS.config.update(configuration)


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
