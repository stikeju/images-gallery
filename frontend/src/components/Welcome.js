import React from 'react';
import { Button } from 'react-bootstrap';

const welcomeStyle = {
  backgroundColor: 'lightblue',
};

const Welcome = () => {
  return (
    <div style={welcomeStyle}>
      <h1>Images Gallery</h1>
      <p>
        This is simple application that retrieves photos using Unsplash API. in
        order to start enter any search term in the input field
      </p>
      <p>
        <Button variant="primary" href="http://unsplash.com" target="_blank">
          Learn more
        </Button>
      </p>
    </div>
  );
};

export default Welcome;
