// General imports
import React, { useState } from "react";
import styled from 'styled-components'
import LoadingAnimation from '../../Components/LoadingAnimation'

export const ProjectsComp = styled.div`
    display: flex;
    flex-direction: column;
    width: 100vw;
    padding: 20px;
    
    #projectInstance {
        margin: 10px;
        padding: 10px;
        border: 1px solid white;
    }
`

const MapProjects = (props) => {
    const [projects] = useState(props.projects)
    function dataString(timestamp) {
        const date = new Date(timestamp.seconds * 1000 + timestamp.nanoseconds / 1000000);
        const dateString = date.toDateString(); // Get the readable date string
        return dateString;
    } 

    return (
        <>
        {projects.length ? ( // Check if projects is not an empty array
                <ProjectsComp>
                    <h1>My Blog Posts</h1>
                    {projects.map(project => (
                        <div id="projectInstance" key={project.id}>
                            <p>{project.projectName}</p>
                            <p>{project.description}</p>
                            <p>{project.purpose}</p>
                            <p>{dataString(project.deadline)}</p>
                            <p>{project.consequence}</p>
                        </div>
                    ))}

                </ProjectsComp>
            ) : (
                <LoadingAnimation />
            )}
        </>
    );
};

export default MapProjects;
