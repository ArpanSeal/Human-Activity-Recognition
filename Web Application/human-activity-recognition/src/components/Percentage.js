import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

function Percentage() {
  const [activityData, setActivityData] = useState({});

  useEffect(() => {
    async function fetchActivityData() {
      const response = await axios.get(
        "http://192.168.188.200:5000/percentage"
      );
      setActivityData(response.data);
    }
    fetchActivityData();
  }, []);

  const getTotalCount = () => {
    if (!activityData.activity_counts) {
      return 0;
    }
    return activityData.activity_counts.Total;
  };

  const getActivityPercentage = (activity) => {
    const totalCount = getTotalCount();
    if (totalCount === 0) {
      return 0;
    }
    const activityCount = activityData.activity_counts[activity];
    return ((activityCount / totalCount) * 100).toFixed(2);
  };

  return (
    <>
      <div className="bgClass">
        <div>
          <Link className="m-3 btn btn-primary" to="/">
            <b>&larr; Back</b>
          </Link>
        </div>
        <div className="container my-2 pb-4">
          <h2 className="text-center fw-bold">Activity Percentage</h2>
          <div className="graph-container p-2">
            <div className="bar-graph my-2">
              <div className="activity-title mt-4">
                <h5>NO_ACTIVITY:</h5>
              </div>
              <div
                className="bar no_activity"
                style={{ width: getActivityPercentage("NO_ACTIVITY") + "%" }}
              ></div>
              <div className="label">{getActivityPercentage("NO_ACTIVITY")}%</div>
            </div>
            <div className="bar-graph my-2">
              <div className="activity-title mt-4">
                <h5>WALKING:</h5>
              </div>
              <div
                className="bar walking"
                style={{ width: getActivityPercentage("WALKING") + "%" }}
              ></div>
              <div className="label">{getActivityPercentage("WALKING")}%</div>
            </div>
            <div className="bar-graph my-2">
              <div className="activity-title mt-4">
                <h5>JOGGING:</h5>
              </div>
              <div
                className="bar jogging"
                style={{ width: getActivityPercentage("JOGGING") + "%" }}
              ></div>
              <div className="label">{getActivityPercentage("JOGGING")}%</div>
            </div>

            <div className="d-grid  my-4 fw-bold fs-4 justify-content-center align-items-center">
              {activityData.activity_counts && (
                <>
                <h3 className="text-center fw-bold my-4 py-2 px-3" style={{backgroundColor:"white", borderRadius:"2rem", boxShadow:"0rem 0.3rem 0.3rem 0.1rem"}}>You have used this app for {(activityData.activity_counts["Total"]/60).toFixed(2)}{" "} minutes</h3>
                  <p className="text-center">
                    You haven't done any activity for {(activityData.activity_counts["NO_ACTIVITY"]/60).toFixed(2)}{" "}
                    minutes.
                  </p>
                  <p className="text-center">
                    You have walked for {(activityData.activity_counts["WALKING"]/60).toFixed(2)}{" "}
                    minutes.
                  </p>
                  <p className="text-center">
                    You have jog for {(activityData.activity_counts["JOGGING"]/60).toFixed(2)}{" "}
                    minutes.
                  </p>
                </>
              )}
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Percentage;
