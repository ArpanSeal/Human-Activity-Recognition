import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Chart from "chart.js/auto";

export default function Download() {
  const [data, setData] = useState([]);
  const [chart, setChart] = useState(null);

  useEffect(() => {
    if (window.DeviceMotionEvent) {
      window.addEventListener("devicemotion", handleDeviceMotion);
    } else {
      alert("Device motion not supported");
    }

    return () => {
      window.removeEventListener("devicemotion", handleDeviceMotion);
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

  const handleDeviceMotion = (event) => {
    const ax = event.acceleration.x;
    const ay = event.acceleration.y;
    const az = event.acceleration.z;
    const gx = event.rotationRate.alpha;
    const gy = event.rotationRate.beta;
    const gz = event.rotationRate.gamma;

    // Calculate magnitude of acceleration vector
    const aMagnitude = Math.sqrt(ax ** 2 + ay ** 2 + az ** 2);

    // Calculate magnitude of rotation rate vector
    const gMagnitude = Math.sqrt(gx ** 2 + gy ** 2 + gz ** 2);

    // Add new features to the newData object
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

    setData((prevData) => [...prevData, newData]);
  };

  const downloadCSV = () => {
    const headers = [
      "ax",
      "ay",
      "az",
      "gx",
      "gy",
      "gz",
      "aMagnitude",
      "gMagnitude",
    ];
    const csvData = [headers, ...data.map((item) => Object.values(item))];

    const blob = new Blob([csvData.map((row) => row.join(",")).join("\n")], {
      type: "text/csv;charset=utf-8;",
    });

    if (navigator.msSaveBlob) {
      navigator.msSaveBlob(blob, "sensor_data.csv");
    } else {
      const link = document.createElement("a");
      if (link.download !== undefined) {
        const url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", "sensor_data.csv");
        link.style.visibility = "hidden";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
    }
  };

  return (
    <>
      <div className="bgClass">
        <div>
          <Link className="m-3 btn btn-primary" to="/">
            <b>&larr; Back</b>
          </Link>
        </div>
        <div className="download pb-5">
          <h1 className="my-3 mb-4 fw-bold">Collecting sensor data</h1>
          <div className="container my-3">
            <canvas id="chart"></canvas>
          </div>
          <div className="m-3 downloadBox">
            <p>
              Acceleration: {JSON.stringify(data[data.length - 1]?.ax)},{" "}
              {JSON.stringify(data[data.length - 1]?.ay)},{" "}
              {JSON.stringify(data[data.length - 1]?.az)}
            </p>
            <p>
              Rotation rate: {JSON.stringify(data[data.length - 1]?.gx)},{" "}
              {JSON.stringify(data[data.length - 1]?.gy)},{" "}
              {JSON.stringify(data[data.length - 1]?.gz)}
            </p>
          </div>
          <button className="btn btn-success" onClick={downloadCSV}>
            <b>Download CSV</b>
          </button>
        </div>
      </div>
    </>
  );
}