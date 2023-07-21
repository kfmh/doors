import React from 'react';
import styled from 'styled-components'

export const Animation = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  div {
    width: 50px;
    height: 50px;
    border: 4px solid #f3f3f3;
    border-top: 4px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }
  @keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
`

const LoadingAnimation = () => {
  return (
    <Animation>
      <div></div>
    </Animation>
  );
};

export default LoadingAnimation;
