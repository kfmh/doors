import React, { useState } from 'react';
import styled from 'styled-components'

export const Form = styled.form`
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  #title {
    height: 30px;
    width: 180px;
    font-size: 1.1rem
  }
  #deadline {
    height: 30px;
    width: 180px;
    font-size: 1.1rem
  }
  #required {
    padding: 0;
    font-size: .8rem;
    color: pink;
  }
  div {
    margin-top: 20px;
    height: fit-content;
  }
  label {
    font-size: 1.1rem;
    text-align: left;
  }
  button {
    margin: 20px;
    max-width: 300px;
    width: 60%;
    height: 50px;
    border-radius: 10px;
    font-size: 1.1rem;
  }
`
export const StartProject = styled.div`
  display: flex;
  flex-direction: column;
  width: 100vw;
  height: 100vh;
  align-items: center;

  h2 {
    padding: 0px;
    margin: 20px 0 0 0;
  }
  textarea {
    width: 100%;
  }
`

const ProjectForm = () => {
  // const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [purpose, setPurpose] = useState('');
  const [deadline, setDeadline] = useState('');
  const [consequence, setConsequence] = useState('');
  const [title, setTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Process the form data here, e.g., send it to a server or perform any other actions
    console.log({
      description,
      purpose,
      deadline,
      consequence,
      title
    });
  };

  return (
    <StartProject>
      <h2>New Project</h2>
      <Form className="project-form" onSubmit={handleSubmit}>
        <input 
          type="text"
          id="title"
          placeholder='Project name...'
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />

        <div>
          <label htmlFor="description">Project Description <span id='required'>Required</span></label>
          <br/>
          <textarea
            rows="8" cols="40"
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="purpose">Project Purpose <span id='required'>Required</span></label>
          <br/>
          <textarea
            rows="8" cols="40"
            id="purpose"
            value={purpose}
            onChange={(e) => setPurpose(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="consequence">Consequence of missing deadline <span id='required'>Required</span></label>
          <br/>
          <textarea
            rows="8" cols="40"
            id="consequence"
            value={consequence}
            onChange={(e) => setConsequence(e.target.value)}
            required
          />
        </div>

        <div>
          <label htmlFor="deadline">Deadline Date <span id='required'>Required</span></label>
          <br/>
          <input
            type="date"
            id="deadline"
            value={deadline}
            onChange={(e) => setDeadline(e.target.value)}
            required
          />
        </div>

        <button type="submit">Start Project</button>
      </Form>
    </StartProject>
  );
};

export default ProjectForm;
