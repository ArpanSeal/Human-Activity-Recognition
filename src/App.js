// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [acceleration, setAcceleration] = useState({
//     x: null,
//     y: null,
//     z: null,
//   });
//   const [rotationRate, setRotationRate] = useState({
//     alpha: null,
//     beta: null,
//     gamma: null,
//   });
//   const [prediction, setPrediction] = useState(null);

//   useEffect(() => {
//     if (window.DeviceMotionEvent) {
//       window.addEventListener("devicemotion", handleDeviceMotion);
//     } else {
//       alert("Device motion not supported");
//     }

//     return () => {
//       window.removeEventListener("devicemotion", handleDeviceMotion);
//     };
//   }, []);

//   const handleDeviceMotion = (event) => {
//     setAcceleration({
//       x: event.acceleration.x,
//       y: event.acceleration.y,
//       z: event.acceleration.z,
//     });

//     setRotationRate({
//       alpha: event.rotationRate.alpha,
//       beta: event.rotationRate.beta,
//       gamma: event.rotationRate.gamma,
//     });

//     console.log(
//       event.acceleration.x,
//       event.acceleration.y,
//       event.acceleration.z,
//       event.rotationRate.alpha,
//       event.rotationRate.beta,
//       event.rotationRate.gamma
//     );

//     // Send sensor data to backend for prediction
//     axios
//       .post("http://192.168.192.200:5000/predict", {
//         ax: event.acceleration.x,
//         ay: event.acceleration.y,
//         az: event.acceleration.z,
//         gx: event.rotationRate.alpha,
//         gy: event.rotationRate.beta,
//         gz: event.rotationRate.gamma,
//       })
//       .then(function (response) {
//         setPrediction(response.data.prediction);
//       })
//       .catch(function (error) {
//         console.log(error);
//       });
//   };

//   return (
//     <div className="App">
//       <h1 className="title">Collecting sensor data</h1>
//       <div className="sensor-data">
//         <h2>Acceleration</h2>
//         <ul>
//           <li>
//             <p>x:</p>
//             <p>{acceleration.x}</p>
//           </li>
//           <li>
//             <p>y:</p>
//             <p>{acceleration.y}</p>
//           </li>
//           <li>
//             <p>z:</p>
//             <p>{acceleration.z}</p>
//           </li>
//         </ul>
//       </div>
//       <div className="sensor-data">
//         <h2>Rotation rate</h2>
//         <ul>
//           <li>
//             <p>alpha:</p>
//             <p>{rotationRate.alpha}</p>
//           </li>
//           <li>
//             <p>beta:</p>
//             <p>{rotationRate.beta}</p>
//           </li>
//           <li>
//             <p>gamma:</p>
//             <p>{rotationRate.gamma}</p>
//           </li>
//         </ul>
//       </div>
//       {prediction && (
//         <div className="prediction">
//           <p>Prediction: {prediction}</p>
//         </div>
//       )}
//     </div>
//   );
// }

// export default App;

// Actual---------------------------------------------
// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [acceleration, setAcceleration] = useState({
//     x: null,
//     y: null,
//     z: null,
//   });
//   const [rotationRate, setRotationRate] = useState({
//     alpha: null,
//     beta: null,
//     gamma: null,
//   });
//   const [magnitudeRate, setMagnitudeRate] = useState({
//     amag: null,
//     gmag: null,
//   });
//   const [prediction, setPrediction] = useState(null);

//   useEffect(() => {
//     if (window.DeviceMotionEvent) {
//       window.addEventListener("devicemotion", handleDeviceMotion);
//     } else {
//       alert("Device motion not supported");
//     }

//     return () => {
//       window.removeEventListener("devicemotion", handleDeviceMotion);
//     };
//   }, []);

//   const handleDeviceMotion = (event) => {
//     const ax = event.acceleration.x;
//     const ay = event.acceleration.y;
//     const az = event.acceleration.z;
//     const gx = event.rotationRate.alpha;
//     const gy = event.rotationRate.beta;
//     const gz = event.rotationRate.gamma;

//     // Calculate magnitude of acceleration vector
//     const aMagnitude = Math.sqrt(ax ** 2 + ay ** 2 + az ** 2);

//     // Calculate magnitude of rotation rate vector
//     const gMagnitude = Math.sqrt(gx ** 2 + gy ** 2 + gz ** 2);

//     setAcceleration({
//       x: ax,
//       y: ay,
//       z: az,
//     });

//     setRotationRate({
//       alpha: gx,
//       beta: gy,
//       gamma: gz,
//     });

//     setMagnitudeRate({
//       amag: aMagnitude,
//       gmag: gMagnitude,
//     });

//     console.log(ax, ay, az, gx, gy, gz, aMagnitude, gMagnitude);

//     // Send sensor data to backend for prediction
//     // axios
//     //   .post("http://192.168.235.200:5000/predict", {
//     //     ax: event.acceleration.x,
//     //     ay: event.acceleration.y,
//     //     az: event.acceleration.z,
//     //     gx: event.rotationRate.alpha,
//     //     gy: event.rotationRate.beta,
//     //     gz: event.rotationRate.gamma,
//     //   })
//     //   .then(function (response) {
//     //     setPrediction(response.data.prediction);
//     //   })
//     //   .catch(function (error) {
//     //     console.log(error);
//     //   });

//     setInterval(() => {
//       axios
//         .post("http://192.168.112.200:5000/predict", {
//           ax: ax,
//           ay: ay,
//           az: az,
//           gx: gx,
//           gy: gy,
//           gz: gz,
//           aMagnitude: aMagnitude,
//           gMagnitude: gMagnitude,
//         })
//         .then(function (response) {
//           setPrediction(response.data.prediction);
//         })
//         .catch(function (error) {
//           console.log(error);
//         });
//     }, 1000);
//   };

//   return (
//     <div className="container my-5">
//       <h1 className="text-center mb-5">Collecting sensor data</h1>
//       <div className="row">
//         <div className="col-md-6">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Acceleration</h2>
//             </div>
//             <div className="card-body">
//               <ul className="list-group">
//                 <li className="list-group-item">X-axis: {acceleration.x}</li>
//                 <li className="list-group-item">Y-axis: {acceleration.y}</li>
//                 <li className="list-group-item">Z-axis: {acceleration.z}</li>
//               </ul>
//             </div>
//           </div>
//         </div>
//         <div className="col-md-6">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Rotation Rate</h2>
//             </div>
//             <div className="card-body">
//               <ul className="list-group">
//                 <li className="list-group-item">Alpha: {rotationRate.alpha}</li>
//                 <li className="list-group-item">Beta: {rotationRate.beta}</li>
//                 <li className="list-group-item">Gamma: {rotationRate.gamma}</li>
//               </ul>
//             </div>
//           </div>
//         </div>
//         <div className="col-md-6">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Magnitude Rate</h2>
//             </div>
//             <div className="card-body">
//               <ul className="list-group">
//                 <li className="list-group-item">
//                   Acceleration: {magnitudeRate.amag}
//                 </li>
//                 <li className="list-group-item">
//                   Rotation: {magnitudeRate.gmag}
//                 </li>
//               </ul>
//             </div>
//           </div>
//         </div>
//       </div>
//       <div className="row mt-5">
//         <div className="col-md-6 mx-auto">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Prediction</h2>
//             </div>
//             <div className="card-body text-center">
//               <h3>{prediction}</h3>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// }

// export default App;

// To download the csv for train dataset -------------------------->

// import React, { useState, useEffect } from "react";
// function App() {
//   const [data, setData] = useState([]);

//   useEffect(() => {
//     if (window.DeviceMotionEvent) {
//       window.addEventListener("devicemotion", handleDeviceMotion);
//     } else {
//       alert("Device motion not supported");
//     }

//     return () => {
//       window.removeEventListener("devicemotion", handleDeviceMotion);
//     };
//   }, []);

//   const handleDeviceMotion = (event) => {
//     const ax = event.acceleration.x;
//     const ay = event.acceleration.y;
//     const az = event.acceleration.z;
//     const gx = event.rotationRate.alpha;
//     const gy = event.rotationRate.beta;
//     const gz = event.rotationRate.gamma;

//     // Calculate magnitude of acceleration vector
//     const aMagnitude = Math.sqrt(ax**2 + ay**2 + az**2);

//     // Calculate magnitude of rotation rate vector
//     const gMagnitude = Math.sqrt(gx**2 + gy**2 + gz**2);

//     // Add new features to the newData object
//     const newData = {
//       ax: ax,
//       ay: ay,
//       az: az,
//       gx: gx,
//       gy: gy,
//       gz: gz,
//       aMagnitude: aMagnitude,
//       gMagnitude: gMagnitude,
//     };

//     setData((prevData) => [...prevData, newData]);
//   };

//   const downloadCSV = () => {
//     const headers = ["ax", "ay", "az", "gx", "gy", "gz", "aMagnitude", "gMagnitude"];
//     const csvData = [headers, ...data.map((item) => Object.values(item))];

//     const blob = new Blob([csvData.map((row) => row.join(",")).join("\n")], { type: "text/csv;charset=utf-8;" });

//     if (navigator.msSaveBlob) {
//       navigator.msSaveBlob(blob, "sensor_data.csv");
//     } else {
//       const link = document.createElement("a");
//       if (link.download !== undefined) {
//         const url = URL.createObjectURL(blob);
//         link.setAttribute("href", url);
//         link.setAttribute("download", "sensor_data.csv");
//         link.style.visibility = "hidden";
//         document.body.appendChild(link);
//         link.click();
//         document.body.removeChild(link);
//       }
//     }
//   };

//   return (
//     <div className="App">
//       <h1>Collecting sensor data</h1>
//       <p>Acceleration: {JSON.stringify(data[data.length - 1]?.ax)}, {JSON.stringify(data[data.length - 1]?.ay)}, {JSON.stringify(data[data.length - 1]?.az)}</p>
//       <p>Rotation rate: {JSON.stringify(data[data.length - 1]?.gx)}, {JSON.stringify(data[data.length - 1]?.gy)}, {JSON.stringify(data[data.length - 1]?.gz)}</p>
//       <button onClick={downloadCSV}>Download CSV</button>
//     </div>
//   );
// }

// export default App;

// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [acceleration, setAcceleration] = useState({
//     x: null,
//     y: null,
//     z: null,
//   });
//   const [rotationRate, setRotationRate] = useState({
//     alpha: null,
//     beta: null,
//     gamma: null,
//   });
//   const [magnitudeRate, setMagnitudeRate] = useState({
//     amag: null,
//     gmag: null,
//   });
//   const [prediction, setPrediction] = useState(null);

//   // eslint-disable-next-line react-hooks/exhaustive-deps
//   useEffect(() => {
//     if (window.DeviceMotionEvent) {
//       window.addEventListener("devicemotion", handleDeviceMotion);
//     } else {
//       alert("Device motion not supported");
//     }

//     return () => {
//       window.removeEventListener("devicemotion", handleDeviceMotion);
//       clearInterval(intervalId);
//     };
//   }, []);

//   let intervalId;

//   const handleDeviceMotion = (event) => {
//     const { acceleration, rotationRate } = event;

//     // Calculate magnitude of acceleration vector
//     const aMagnitude = Math.sqrt(
//       acceleration.x ** 2 + acceleration.y ** 2 + acceleration.z ** 2
//     );

//     // Calculate magnitude of rotation rate vector
//     const gMagnitude = Math.sqrt(
//       rotationRate.alpha ** 2 + rotationRate.beta ** 2 + rotationRate.gamma ** 2
//     );

//     setAcceleration(acceleration);
//     setRotationRate(rotationRate);
//     setMagnitudeRate({
//       amag: aMagnitude,
//       gmag: gMagnitude,
//     });

//     if (!intervalId) {
//       intervalId = setInterval(collectDataAndPredict, 1000);
//     }
//   };

//   const collectDataAndPredict = () => {
//     const ax = acceleration.x;
//     const ay = acceleration.y;
//     const az = acceleration.z;
//     const gx = rotationRate.alpha;
//     const gy = rotationRate.beta;
//     const gz = rotationRate.gamma;

//     // Calculate magnitude of acceleration vector
//     const aMagnitude = Math.sqrt(ax ** 2 + ay ** 2 + az ** 2);

//     // Calculate magnitude of rotation rate vector
//     const gMagnitude = Math.sqrt(gx ** 2 + gy ** 2 + gz ** 2);

//     console.log(ax, ay, az, gx, gy, gz, aMagnitude, gMagnitude);
//     axios
//       .post("http://192.168.112.200:5000/predict", {
//         ax: ax,
//         ay: ay,
//         az: az,
//         gx: gx,
//         gy: gy,
//         gz: gz,
//         aMagnitude: aMagnitude,
//         gMagnitude: gMagnitude,
//       })
//       .then(function (response) {
//         setPrediction(response.data.prediction);
//       })
//       .catch(function (error) {
//         console.log(error);
//       });
//   };

//   return (
//     <div className="container my-5">
//       <h1 className="text-center mb-5">Collecting sensor data</h1>
//       <div className="row">
//         <div className="col-md-6">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Acceleration</h2>
//             </div>
//             <div className="card-body">
//               <ul className="list-group">
//                 <li className="list-group-item">X-axis: {acceleration.x}</li>
//                 <li className="list-group-item">Y-axis: {acceleration.y}</li>
//                 <li className="list-group-item">Z-axis: {acceleration.z}</li>
//               </ul>
//             </div>
//           </div>
//         </div>
//         <div className="col-md-6">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Rotation Rate</h2>
//             </div>
//             <div className="card-body">
//               <ul className="list-group">
//                 <li className="list-group-item">Alpha: {rotationRate.alpha}</li>
//                 <li className="list-group-item">Beta: {rotationRate.beta}</li>
//                 <li className="list-group-item">Gamma: {rotationRate.gamma}</li>
//               </ul>
//             </div>
//           </div>
//         </div>
//         <div className="col-md-6">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Magnitude Rate</h2>
//             </div>
//             <div className="card-body">
//               <ul className="list-group">
//                 <li className="list-group-item">
//                   Acceleration: {magnitudeRate.amag}
//                 </li>
//                 <li className="list-group-item">
//                   Rotation: {magnitudeRate.gmag}
//                 </li>
//               </ul>
//             </div>
//           </div>
//         </div>
//       </div>
//       <div className="row mt-5">
//         <div className="col-md-6 mx-auto">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Prediction</h2>
//             </div>
//             <div className="card-body text-center">
//               <h3>{prediction}</h3>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// }

// export default App;

// // Maybe Final
// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [acceleration, setAcceleration] = useState({
//     x: null,
//     y: null,
//     z: null,
//   });
//   const [rotationRate, setRotationRate] = useState({
//     alpha: null,
//     beta: null,
//     gamma: null,
//   });
//   const [magnitudeRate, setMagnitudeRate] = useState({
//     amag: null,
//     gmag: null,
//   });
//   const [prediction, setPrediction] = useState(null);

//   // eslint-disable-next-line react-hooks/exhaustive-deps
//   useEffect(() => {
//     if (window.DeviceMotionEvent) {
//       window.addEventListener("devicemotion", handleDeviceMotion);
//     } else {
//       alert("Device motion not supported");
//     }

//     return () => {
//       window.removeEventListener("devicemotion", handleDeviceMotion);
//       clearInterval(intervalId);
//     };
//   }, []);

//   let intervalId;

//   let ax = undefined,
//     ay = undefined,
//     az = undefined,
//     gx = undefined,
//     gy = undefined,
//     gz = undefined,
//     aMagnitude = 0,
//     gMagnitude = 0;

//   const handleDeviceMotion = (event) => {
//     ax = event.acceleration.x;
//     ay = event.acceleration.y;
//     az = event.acceleration.z;
//     gx = event.rotationRate.alpha;
//     gy = event.rotationRate.beta;
//     gz = event.rotationRate.gamma;

//     // const { acceleration, rotationRate } = event;

//     // Calculate magnitude of acceleration vector
//     aMagnitude = Math.sqrt(ax ** 2 + ay ** 2 + az ** 2);

//     // Calculate magnitude of rotation rate vector
//     gMagnitude = Math.sqrt(gx ** 2 + gy ** 2 + gz ** 2);

//     setAcceleration({
//       x: ax,
//       y: ay,
//       z: az,
//     });

//     setRotationRate({
//       alpha: gx,
//       beta: gy,
//       gamma: gz,
//     });

//     setMagnitudeRate({
//       amag: aMagnitude,
//       gmag: gMagnitude,
//     });

//     console.log(ax, ay, az, gx, gy, gz, aMagnitude, gMagnitude);

//     if (!intervalId) {
//       intervalId = setInterval(collectDataAndPredict, 1000);
//     }
//   };

//   const collectDataAndPredict = () => {
//     axios
//       .post("http://192.168.177.200:5000/predict", {
//         ax: ax,
//         ay: ay,
//         az: az,
//         gx: gx,
//         gy: gy,
//         gz: gz,
//         aMagnitude: aMagnitude,
//         gMagnitude: gMagnitude,
//       })
//       .then(function (response) {
//         setPrediction(response.data.prediction);
//       })
//       .catch(function (error) {
//         console.log(error);
//       });
//   };

//   return (
//     <div className="container my-5">
//       <h1 className="text-center mb-5">Collecting sensor data</h1>
//       <div className="row">
//         <div className="col-md-6">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Acceleration</h2>
//             </div>
//             <div className="card-body">
//               <ul className="list-group">
//                 <li className="list-group-item">X-axis: {acceleration.x}</li>
//                 <li className="list-group-item">Y-axis: {acceleration.y}</li>
//                 <li className="list-group-item">Z-axis: {acceleration.z}</li>
//               </ul>
//             </div>
//           </div>
//         </div>
//         <div className="col-md-6">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Rotation Rate</h2>
//             </div>
//             <div className="card-body">
//               <ul className="list-group">
//                 <li className="list-group-item">Alpha: {rotationRate.alpha}</li>
//                 <li className="list-group-item">Beta: {rotationRate.beta}</li>
//                 <li className="list-group-item">Gamma: {rotationRate.gamma}</li>
//               </ul>
//             </div>
//           </div>
//         </div>
//         <div className="col-md-6">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Magnitude Rate</h2>
//             </div>
//             <div className="card-body">
//               <ul className="list-group">
//                 <li className="list-group-item">
//                   Acceleration: {magnitudeRate.amag}
//                 </li>
//                 <li className="list-group-item">
//                   Rotation: {magnitudeRate.gmag}
//                 </li>
//               </ul>
//             </div>
//           </div>
//         </div>
//       </div>
//       <div className="row mt-5">
//         <div className="col-md-6 mx-auto">
//           <div className="card">
//             <div className="card-header">
//               <h2 className="card-title">Prediction</h2>
//             </div>
//             <div className="card-body text-center">
//               <h3>{prediction}</h3>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// }

// export default App;

import React from "react";
import Prediction from "./components/Prediction";
import Download from "./components/Download";
import Percentage from "./components/Percentage";
import Home from "./screen/Home";
import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import footerLogo from "./image/footerLogo.png";
import logo from "./image/logo.png";

export default function App() {
  return (
    <Router>
      <div>
        <div className="bgHead p-2">
          <img src={logo} alt="logo" className="mx-2" />
          <h2 className="text-center py-2 text-light fw-bold">
            RCC Institute of Information Technology
          </h2>
        </div>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route exact path="/prediction" element={<Prediction />} />
          <Route exact path="/download" element={<Download />} />
          <Route exact path="/percentage" element={<Percentage />} />
        </Routes>

        <div className="container">
          <footer className="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
            <div className="col-md-4 d-flex align-items-center">
              <Link
                to="/"
                className="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1"
              >
                <img src={footerLogo} alt="" />
              </Link>
              <span className="mb-3 mb-md-0 text-muted">
                HAR © 2023, Inc
              </span>
            </div>

            <ul className="nav col-md-4 justify-content-end list-unstyled d-flex">
              <li className="ms-3">
                <Link className="text-muted" to="/prediction">
                  Predict Activity
                </Link>
              </li>
              <li className="ms-3">
                <Link className="text-muted" to="/download">
                  Download Records
                </Link>
              </li>
            </ul>
          </footer>
        </div>
      </div>
    </Router>
  );
}
