import React, { useState } from 'react';
import styled from 'styled-components'

export const Form = styled.form`
  div {
    margin-top: 50px;
  }
`
export const StartProject = styled.div`
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100vh;
`

const ProjectForm = () => {
  // const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [purpose, setPurpose] = useState('');
  const [deadline, setDeadline] = useState('');
  const [moreInfoText, setMoreInfoText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Process the form data here, e.g., send it to a server or perform any other actions
    console.log({
      description,
      purpose,
      deadline,
      moreInfoText
    });
  };

  return (
    <StartProject>
      <h1>Start Project</h1>
      <Form className="project-form" onSubmit={handleSubmit}>
        {/* <div>
          <label htmlFor="description">Title</label>
          <br/>
          <input 
            type="text"
            id="description"
            value={description}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div> */}
        <div>
          <label htmlFor="description">Project Description</label>
          <br/>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="purpose">Project Purpose</label>
          <br/>
          <textarea
            id="purpose"
            value={purpose}
            onChange={(e) => setPurpose(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="deadline">Deadline Date</label>
          <br/>
          <input
            type="date"
            id="deadline"
            value={deadline}
            onChange={(e) => setDeadline(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="moreInfoText">Risc of not finishing on time</label>
          <br/>
          <textarea
            id="moreInfoText"
            value={moreInfoText}
            onChange={(e) => setMoreInfoText(e.target.value)}
            required
          />
        </div>

        <button type="submit">Submit</button>
      </Form>
    </StartProject>
  );
};

export default ProjectForm;
