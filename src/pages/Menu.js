import React, { useState, useRef, useEffect } from 'react';
import BannerImage from '../assets/thesecond.webp';
import '../styles/Menu.css';

function Menu() {
  // const [text, setText] = useState('');
  // const videoRef = useRef(null);

  // useEffect(() => {
  //   if (navigator.mediaDevices && navigator.mediaDegitvices.getUserMedia) {
  //     navigator.mediaDevices.getUserMedia({ video: true })
  //       .then((stream) => {
  //         if (videoRef.current) {
  //           videoRef.current.srcObject = stream;
  //           videoRef.current.play();
  //         }
  //       });
  //   }

  //   const interval = setInterval(() => {
  //     sendFrameToBackend();
  //   }, 1000); // Send frame every second

  //   return () => clearInterval(interval);
  // }, []);

  // const sendFrameToBackend = () => {
  //   if (videoRef.current) {
  //     const canvas = document.createElement('canvas');
  //     canvas.width = videoRef.current.videoWidth;
  //     canvas.height = videoRef.current.videoHeight;
  //     const context = canvas.getContext('2d');
  //     context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
  //     const dataURL = canvas.toDataURL();

  //     fetch('http://localhost:5000/process-image', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json'
  //       },
  //       body: JSON.stringify({ image: dataURL })
  //     })
  //     .then(response => response.json())
  //     .then(data => {
  //       setText(data.text); // Assuming the backend returns a JSON with a 'text' field
  //     })
  //     .catch(error => console.error('Error:', error));
  //   }
  // };

  return (
    <div className="menu">
      <div className="background" style={{ backgroundImage: `url(${BannerImage})` }}></div>
      <div className="content">
        {/* <video ref={videoRef} width="640" height="480" style={{ display: 'none' }}></video> */}
        <canvas width="640" height="480"></canvas>
        {/* <p>{text}</p> */}
      </div>
    </div>
  );
}

export default Menu;
