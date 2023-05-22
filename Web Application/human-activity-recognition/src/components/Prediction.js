import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import Chart from "chart.js/auto";

export default function Prediction() {
  const [data, setData] = useState([]);
  const [chart, setChart] = useState(null);

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

  useEffect(() => {
    if (data.length > 0) {
      if (!chart) {
        const ctx = document.getElementById("chart").getContext("2d");
        const newChart = new Chart(ctx, {
          type: "line",
          data: {
            labels: [],
            datasets: [
              {
                label: "Acceleration (x)",
                data: [],
                backgroundColor: "rgba(255, 99, 132, 0.2)",
                borderColor: "rgba(255, 99, 132, 1)",
                borderWidth: 1,
              },
              {
                label: "Acceleration (y)",
                data: [],
                backgroundColor: "rgba(54, 162, 235, 0.2)",
                borderColor: "rgba(54, 162, 235, 1)",
                borderWidth: 1,
              },
              {
                label: "Acceleration (z)",
                data: [],
                backgroundColor: "rgba(255, 206, 86, 0.2)",
                borderColor: "rgba(255, 206, 86, 1)",
                borderWidth: 1,
              },
            ],
          },
          options: {
            scales: {
              xAxes: [
                {
                  type: "time",
                  time: {
                    displayFormats: {
                      second: "h:mm:ss a",
                    },
                  },
                  scaleLabel: {
                    display: true,
                    labelString: "Time",
                  },
                },
              ],
              yAxes: [
                {
                  scaleLabel: {
                    display: true,
                    labelString: "Acceleration (m/s^2)",
                  },
                },
              ],
            },
          },
        });
        setChart(newChart);
      } else {
        chart.data.labels.push(
          new Date().toLocaleTimeString("en-US", { hour12: false })
        );
        chart.data.datasets[0].data.push(data[data.length - 1].ax);
        chart.data.datasets[1].data.push(data[data.length - 1].ay);
        chart.data.datasets[2].data.push(data[data.length - 1].az);
        chart.update();
        // Remove older data points
        if (chart.data.datasets[0].data.length > 120) {
          chart.data.labels.shift();
          chart.data.datasets[0].data.shift();
          chart.data.datasets[1].data.shift();
          chart.data.datasets[2].data.shift();
        }

        chart.update();
      }
    }
  }, [data]);

  let intervalId;

  let ax = undefined,
    ay = undefined,
    az = undefined,
    gx = undefined,
    gy = undefined,
    gz = undefined,
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

    const newData = {
      ax: ax,
      ay: ay,
      az: az,
      gx: gx,
      gy: gy,
      gz: gz,
      aMagnitude: aMagnitude,
      gMagnitude: gMagnitude,
    };

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

    setData((prevData) => [...prevData, newData]);
  };

  const collectDataAndPredict = () => {
    axios
      .post("http://192.168.155.200:5000/predict", {
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
    <>
      <div className="bgClass">
        <div>
          <Link className="m-3 btn btn-primary" to="/">
            <b>&larr; Back</b>
          </Link>
        </div>
        <div className="container pb-5">
          <h1 className="text-center my-4 fw-bold">Visualizing sensor data</h1>
          <div className="row">
            <div className="col-md-4">
              <div className="card m-2 cards">
                <div className="card-header">
                  <h2 className="card-title">Acceleration</h2>
                </div>
                <div className="card-body">
                  <ul className="list-group">
                    <li className="list-group-item">
                      X-axis: {acceleration.x}
                    </li>
                    <li className="list-group-item">
                      Y-axis: {acceleration.y}
                    </li>
                    <li className="list-group-item">
                      Z-axis: {acceleration.z}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card m-2 cards">
                <div className="card-header">
                  <h2 className="card-title">Rotation Rate</h2>
                </div>
                <div className="card-body">
                  <ul className="list-group">
                    <li className="list-group-item">
                      Alpha: {rotationRate.alpha}
                    </li>
                    <li className="list-group-item">
                      Beta: {rotationRate.beta}
                    </li>
                    <li className="list-group-item">
                      Gamma: {rotationRate.gamma}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card m-2 cards">
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
          <div className="row">
            <div className="col-md-4 mx-auto">
              <div className="card m-2 cards">
                <div className="container my-3">
                  <canvas id="chart"></canvas>
                </div>
              </div>
            </div>
          </div>
          <div className="row mt-5">
            <div className="col-md-6 mx-auto">
              <div className="card cards">
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
      </div>
    </>
  );
}