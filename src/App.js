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
                <Link className="text-muted" to="/percentage">
                  Activity Percentage
                </Link>
              </li>
            </ul>
          </footer>
        </div>
      </div>
    </Router>
  );
}
