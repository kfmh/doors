// General imports
import React, { useState } from "react"
import LoadingAnimation from '../../Components/LoadingAnimation'

import ProjectsComp  from "./ProjectsComponent";


const MapProjects = (props) => {
    const [projects] = useState(props.projects)
    console.log(projects)

    return (
        <>
        {projects.length ? ( // Check if projects is not an empty array
                <>

                    <h1 style={{textAlign: "center"}}>My Projects</h1>
                    {projects.map(project => (
                        <ProjectsComp key={project.consequence} project={project}/>
                    ))}
                </>

            ) : (
                <LoadingAnimation />
            )}
        </>
    );
};

export default MapProjects;
