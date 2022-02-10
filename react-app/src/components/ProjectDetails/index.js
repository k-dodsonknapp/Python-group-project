import React from "react";
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom"
import { getOneProject } from "../../store/project";
import './Projects.css'

const ProjectDetails = () => {
    const dispatch = useDispatch()
    const { projectId } = useParams();
    const project = useSelector(state => state.projects[projectId])
    console.log(project)

    useEffect(() => {
        dispatch(getOneProject(projectId))
    }, [dispatch, projectId])

    return (
        <>
            {project &&
                <div id='project-container'>
                    {/* <h1>Hello from Project by id page</h1> */}
                    <div className='title'>{project.title}</div>
                    <div id='project-details'>By
                        <span className='username-category'>{project.owner.username}</span>
                        in<span className='username-category'>{project.category}</span>
                    </div>
                    <div className="project-image-container">
                        <img className='project-images'src={project.titleImage} alt='Completed project'></img>
                    </div>
                    <div id='overview-title'>Project Overview:
                        <p id='project-overview'>{project.overview}</p>
                    </div>
                    <ul id='supplies-title'>Supplies Needed:
                        {project.supplies.map((supply) => (
                            <>
                                <li className='supply-list'key={supply.id}>{supply.supply}</li>
                            </>
                        ))}

                    </ul>
                    <ul>
                        {project.instructions.map((instruction) => (
                            <div className="instruction-container">
                                <step className='instruction-title'>Step {instruction.stepOrder}:</step>
                                <div className='project-image-container'>
                                    <img
                                        className="instruction-image"
                                        key={instruction.id}
                                        src={instruction.photoUrl}
                                        alt={`Step ${instruction.stepOrder}`}>
                                    </img>
                                </div>
                                <li className='instructions'key={instruction.id}>{instruction.instructions}</li>
                            </div>
                        ))}
                    </ul>
                </div>
            }
        </>
    )
}

export default ProjectDetails;
