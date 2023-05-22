import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [acceleration, setAcceleration] = useState({
    x: null,
    y: null,
    z: null,
  });
  const [rotationRate, setRotationRate] = useState({
    alpha: null,
    beta: null,
    gamma: null,
  });
  const [magnitudeRate, setMagnitudeRate] = useState({
    amag: null,
    gmag: null,
  });
  const [prediction, setPrediction] = useState(null);

  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect(() => {
    if (window.DeviceMotionEvent) {
      window.addEventListener("devicemotion", handleDeviceMotion);
    } else {
      alert("Device motion not supported");
    }

    return () => {
      window.removeEventListener("devicemotion", handleDeviceMotion);
      clearInterval(intervalId);
    };
  }, []);

  let intervalId;

  const ax = None,
    ay = None,
    az = None,
    gx = None,
    gy = None,
    gz = None,
    aMagnitude = 0,
    gMagnitude = 0;

  const handleDeviceMotion = (event) => {
    ax = event.acceleration.x;
    ay = event.acceleration.y;
    az = event.acceleration.z;
    gx = event.rotationRate.alpha;
    gy = event.rotationRate.beta;
    gz = event.rotationRate.gamma;

    // const { acceleration, rotationRate } = event;

    // Calculate magnitude of acceleration vector
    aMagnitude = Math.sqrt(ax ** 2 + ay ** 2 + az ** 2);

    // Calculate magnitude of rotation rate vector
    gMagnitude = Math.sqrt(gx ** 2 + gy ** 2 + gz ** 2);

    setAcceleration({
      x: ax,
      y: ay,
      z: az,
    });

    setRotationRate({
      alpha: gx,
      beta: gy,
      gamma: gz,
    });

    setMagnitudeRate({
      amag: aMagnitude,
      gmag: gMagnitude,
    });

    console.log(ax, ay, az, gx, gy, gz, aMagnitude, gMagnitude);

    if (!intervalId) {
      intervalId = setInterval(collectDataAndPredict, 1000);
    }
  };

  const collectDataAndPredict = () => {
    axios
      .post("http://192.168.112.200:5000/predict", {
        ax: ax,
        ay: ay,
        az: az,
        gx: gx,
        gy: gy,
        gz: gz,
        aMagnitude: aMagnitude,
        gMagnitude: gMagnitude,
      })
      .then(function (response) {
        setPrediction(response.data.prediction);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  return (
    <div className="container my-5">
      <h1 className="text-center mb-5">Collecting sensor data</h1>
      <div className="row">
        <div className="col-md-6">
          <div className="card">
            <div className="card-header">
              <h2 className="card-title">Acceleration</h2>
            </div>
            <div className="card-body">
              <ul className="list-group">
                <li className="list-group-item">X-axis: {acceleration.x}</li>
                <li className="list-group-item">Y-axis: {acceleration.y}</li>
                <li className="list-group-item">Z-axis: {acceleration.z}</li>
              </ul>
            </div>
          </div>
        </div>
        <div className="col-md-6">
          <div className="card">
            <div className="card-header">
              <h2 className="card-title">Rotation Rate</h2>
            </div>
            <div className="card-body">
              <ul className="list-group">
                <li className="list-group-item">Alpha: {rotationRate.alpha}</li>
                <li className="list-group-item">Beta: {rotationRate.beta}</li>
                <li className="list-group-item">Gamma: {rotationRate.gamma}</li>
              </ul>
            </div>
          </div>
        </div>
        <div className="col-md-6">
          <div className="card">
            <div className="card-header">
              <h2 className="card-title">Magnitude Rate</h2>
            </div>
            <div className="card-body">
              <ul className="list-group">
                <li className="list-group-item">
                  Acceleration: {magnitudeRate.amag}
                </li>
                <li className="list-group-item">
                  Rotation: {magnitudeRate.gmag}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div className="row mt-5">
        <div className="col-md-6 mx-auto">
          <div className="card">
            <div className="card-header">
              <h2 className="card-title">Prediction</h2>
            </div>
            <div className="card-body text-center">
              <h3>{prediction}</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
