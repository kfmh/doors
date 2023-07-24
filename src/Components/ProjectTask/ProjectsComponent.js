// General imports
import React, { useState } from "react";
import styled from 'styled-components'

export const Comp = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100vw;
    #projectInfo {
        margin-top: 20px;
        h5{
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
        max-width: 500px;
        margin: 10px;
        padding: 10px;
        border: 1px solid white;
        border-radius: 10px;
        button {
            background: none;
            border: 1px solid white;
            margin-top: 10px;
            width: 100%;
            height: 30px;
            border-radius: 8px;
            color: white;
            letter-spacing: 4px;
        }
        #pInfo {
            padding: 10px;
            border: 1px solid white; 
            border-radius: 10px
        }
    }
    #projectButton {
        width: 80%;
        max-width: 500px;
        margin: 10px 0 0 0;
        display: flex;
        justify-content: space-between;
        text-align: left;
        background: none;
        color: white;
        border: solid 1px white;
        border-radius: 10px;
        padding: 10px;
        cursor: pointer;
        p {
            margin: 0;
            padding: 0;
        }
    }
`

const ProjectsComp = (props) => {
    const [showProject, setShowProject] = useState('none')
    const [showBTN, setShowBTN] = useState('Block')

    function dataString(timestamp) {
        const date = new Date(timestamp.seconds * 1000 + timestamp.nanoseconds / 1000000);
        const dateString = date.toDateString(); // Get the readable date string
        return dateString;
    }

    return (
        <Comp>
            <div style={{display: `${showBTN}`}} id="projectButton" 
            onClick={() => {setShowProject(showProject === 'none' ? 'block' : 'none'); 
                            setShowBTN(showProject === 'none' ? 'none' : 'block')}}>
                <p>{props.project.projectName}</p>
                <p>"Progress Bar"</p>
            </div>

            <div id="projectInstance" key={props.project.id} style={{display: `${showProject}`}}>
                <div id="pInfo" onClick={() => {setShowProject(showProject === 'none' ? 'block' : 'none'); 
                            setShowBTN(showProject === 'none' ? 'none' : 'block')}} >

                    <div style={{display: "flex", alignItems: 'center', justifyContent: "space-evenly"}} id="projectInfo">
                        <div>
                            <h5>Project: </h5> <p>{props.project.projectName}</p>
                        </div>
                        <div>
                            <h5>Deadline:</h5><p>{dataString(props.project.deadline)}</p>
                        </div>
                    </div>
                    <div id="projectInfo">
                        <h5>Description:</h5>
                        <p>{props.project.description}</p>
                    </div>
                    <div id="projectInfo">
                        <h5>Purpose:</h5>
                        <p>{props.project.purpose}</p>
                    </div>
                    <div id="projectInfo">
                        <h5>Consequence:</h5>
                        <p>{props.project.consequence}</p>
                    </div>
                    <div style={{textAlign: 'center'}} id="projectInfo">
                    </div>
                </div>
                <button >Breakdown</button>
            </div>
        </Comp>

    );
};

export default ProjectsComp;
