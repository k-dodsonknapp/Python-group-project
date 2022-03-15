import React from "react";
import { NavLink } from "react-router-dom"
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllProjects } from "../../store/project";
import './projectExplore.css'
import Carousel, { CarouselItem } from "../Carousel";


const ProjectExplore = () => {
    const dispatch = useDispatch();
    const projects = useSelector(state => Object.values(state.projects));
    console.log(projects[0].views, "PPPPPPPPPPP")

    useEffect(() => {
        dispatch(getAllProjects());
    }, [dispatch]);

    const explore = "Explore >"

    return (
        <div className="explorePage">
            <div className="slideshow-container">
                <img src="https://media.istockphoto.com/photos/colorful-background-of-pastel-powder-explosionrainbow-color-dust-on-picture-id1180542165?k=20&m=1180542165&s=612x612&w=0&h=43hlhk8qdGYP4V-u3AAxD3kPDRIzHjMNWpr-VdBQ2Js=" alt=""></img>
                {/* <Carousel>
                    <CarouselItem>item 1</CarouselItem>
                    <CarouselItem>item 2</CarouselItem>
                    <CarouselItem>item 3</CarouselItem>
                </Carousel> */}
            </div>
            <div className="content-container">
                <div className="content">
                    <h2>Instructions STEP-BY-STEP</h2>
                    <p>
                    We make it easy to learn how to make anything, one step at a time. From the stovetop to the workshop, you are sure to be inspired by the awesome projects that are shared everyday.
                    </p>
                </div>
                <div className="content">
                    <h2>MADE by THE COMMUNITY </h2>
                    <p>
                    Step-by-Steps are created by you. No matter who you are, we all have secret skills to share. Come join our community of curious makers, innovators, teachers, and life long learners who love to share what they make.
                    </p>
                </div>
                <div id="place" className="content">
                    <h2>A PLACE</h2>
                    <p>
                    Making things. We can't prove it, but we know it to be true. Find your place, and join one of the friendliest online communities anywhere.
                    </p>
                </div>
            </div>
            <ul>
                <div id="explore-sign">
                    <h2>{explore}</h2>
                </div>
                {projects?.map(project => (
                    <div className="allProjectsMap" key={project.id}>
                        <li className="eachProject">
                            <a href={`/projects/${project.id}`}>
                                <div className="projectImage">
                                    <img src={`${project.titleImage}`} alt="" />
                                </div>
                            </a>
                            <div className="info-container">
                                <div className="title-by">
                                    <div>
                                        <p>{project?.title} by <NavLink to={`/users/${project.userId}`}>
                                            {project.username}
                                        </NavLink>  in <NavLink to={`/category/${project.category}`}>
                                                {project?.category}
                                            </NavLink>
                                        </p>
                                    </div>
                                    <div className="likes-views">
                                        <p>❤ 5  👁 105</p>
                                    </div>
                                </div>
                            </div>
                        </li>
                    </div>
                ))}
            </ul>
        </div >
    )
}

export default ProjectExplore;
