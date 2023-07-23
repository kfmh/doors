// General imports
import React, { useState } from "react";
import styled from 'styled-components'
import LoadingAnimation from '../../Components/LoadingAnimation'

export const ProjectsComp = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    #projectInfo {
        margin-top: 20px;
        h4 {
            margin: 0;
            padding: 0;
            font-weight: 200;
        }
        p {
            margin: 0;
            padding: 0;
        }
    }
    #projectInstance {
        width: 80%;
        margin: 10px;
        padding: 10px;
        border: 1px solid white;
        border-radius: 10px;
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
                    <h1>My Projects</h1>
                    {projects.map(project => (
                        <div id="projectInstance" key={project.id}>
                            <div id="projectInfo">
                                <h4>Project: {project.projectName}</h4>
                            </div>
                            <div id="projectInfo">
                                <h4>Description:</h4>
                                <p>{project.description}</p>
                            </div>
                            <div id="projectInfo">
                                <h4>Purpose:</h4>
                                <p>{project.purpose}</p>
                            </div>
                            <div id="projectInfo">
                                <h4>Deadline:</h4>
                                <p>{dataString(project.deadline)}</p>

                            </div>
                            <div id="projectInfo">
                                <h4>Consequence:</h4>
                                <p>{project.consequence}</p>
                            </div>
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
