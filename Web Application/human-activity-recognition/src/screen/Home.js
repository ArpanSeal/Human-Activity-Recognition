import React from "react";
import rfr from "../image/rfr.jpg";
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <>
      <section id="home" className="d-flex align-items-center background blue">
        <div className="container-fluid" data-aos="fade-up">
          <div className="row">
            <div
              className="col-xl-5 col-lg-6 pb-3 pt-lg-0 order-2 order-lg-1 d-flex flex-column justify-content-center"
              style={{ zIndex: 1 }}
            >
              <h1 className="text-center">
                Achieve Your Fitness Goals: Monitor Your Activities with Our Web
                App
              </h1>
              <h2 className="text-center">
                Maximize your fitness potential with real-time monitoring and
                analysis from our human activity recognition web app
              </h2>
              <div className="homeBtn">
                <div>
                  <Link
                    className="btn-get-started scrollto"
                    to="/prediction"
                  >
                    Predict Activity
                  </Link>
                </div>
                <div>
                  <Link
                    className="btn-get-started scrollto"
                    type="button"
                    to="/download"
                  >
                    Download Records
                  </Link>
                </div>
              </div>
              <div className="d-flex justify-content-center align-items-center mb-5">
                <Link
                  className="btn-get-started scrollto"
                  type="button"
                  to="/percentage"
                >
                  Activity Percentage
                </Link>
              </div>
            </div>
            <div className="spread"></div>
            <div
              className="col-xl-5 col-lg-6 order-1 order-lg-2 home-img"
              data-aos="zoom-in"
              data-aos-delay="150"
              style={{ zIndex: 1 }}
            >
              <img
                className="img-fluid animated rfrImg"
                src={rfr}
                style={{ width: "27rem", marginBottom:"3rem"}}
                alt="image"
              />
            </div>
          </div>
        </div>
      </section>
    </>
  );
}
