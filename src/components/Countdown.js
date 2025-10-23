import React, { useState, useEffect } from 'react';
import styles from './Countdown.module.css';

const Countdown = ({ targetDate }) => {
  const calculateTimeLeft = () => {
    const difference = +new Date(targetDate) - +new Date();
    let timeLeft = {};

    if (difference > 0) {
      timeLeft = {
        Days: Math.floor(difference / (1000 * 60 * 60 * 24)),
        Hours: Math.floor((difference / (1000 * 60 * 60)) % 24),
        Minutes: Math.floor((difference / 1000 / 60) % 60),
        Seconds: Math.floor((difference / 1000) % 60),
      };
    }
    return timeLeft;
  };

  const [timeLeft, setTimeLeft] = useState(calculateTimeLeft());

  useEffect(() => {
    const timer = setTimeout(() => {
      setTimeLeft(calculateTimeLeft());
    }, 1000);

    return () => clearTimeout(timer);
  });

  const timerComponents = Object.keys(timeLeft).map((interval) => {
    if (timeLeft[interval] === undefined) {
      return null;
    }

    return (
      <div key={interval} className={styles.countdownItem}>
        <span className={styles.countdownValue}>{timeLeft[interval]}</span>
        <span className={styles.countdownLabel}>{interval}</span>
      </div>
    );
  });

  const formattedTargetDate = new Date(targetDate).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric'
  });

  return (
    <div className={styles.wrapper}>
      <div className={styles.countdownContainer}>
        {timerComponents.length ? timerComponents : <span>Time's up!</span>}
      </div>
      <p className={styles.targetDateText}>
        {formattedTargetDate}
      </p>
    </div>
  );
};

export default Countdown;