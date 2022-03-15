import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import { deleteOneProject, getOneProject } from "../../store/project";
import { addOneComment, deleteOneComment } from "../../store/comments";
import EditCommentForm from "../EditComments";
import "./Projects.css";

const ProjectDetails = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { projectId } = useParams();
  const project = useSelector((state) => state.projects[+projectId]);

  const user = useSelector((state) => state.session.user);
  const session = useSelector(state => state.session);
  // const commentState = useSelector((state) => state.comments);


  const [showCommentForm, setShowCommentForm] = useState(false);
  const [setShowCommentEditForm] = useState(false);
  const [comment, setComment] = useState('');
  // console.log("IDKDKDKDKD", comment)
  const [newComment ] = useState(0);
  const [commentId, setCommentId] = useState(0);
  
  let reversedComments = []
  if (project) {
    project.comments.map(comment => {
      return reversedComments.unshift(comment)
    })
  }

  useEffect(() => {
    addOneComment(newComment)
  }, [dispatch, newComment])

  useEffect(() => {
    dispatch(getOneProject(projectId))
  }, [dispatch, projectId])
  
  useEffect(() => {
    dispatch(getOneProject(+projectId));
  }, [dispatch, projectId]);

  const handleComment = async (e) => {
    e.preventDefault();
    const newComment = { userId: user.id, projectId, comment };
    await dispatch(addOneComment(newComment));
    await dispatch(getOneProject(projectId))
    setShowCommentForm(false)
  };


  const handleEditProjectButton = (e) => {
    e.preventDefault();
    history.push(`/projects/${projectId}/edit`)
  }

  const handleDelete = async (e) => {
    e.preventDefault();
    const projectDelete = await dispatch(deleteOneProject(projectId))
    if (projectDelete) {
      history.push('/')
    }
  }

  const handleDeleteComment = async (e) => {
    console.log(e)
    e.preventDefault();
    await dispatch(deleteOneComment(e.target.id))
    dispatch(getOneProject(projectId))
  }

  const handleShowEditForm = async (e) => {
    e.preventDefault();
    const id = e.target.id
    setCommentId(id)
    // console.log(+commentId === +id)
    setComment(project.comments.id)
    // console.log(id)
    setShowCommentEditForm(true);
  }

  // const cancel = (e) => {
  //   e.preventDefault();
  //   setShowCommentEditForm(false)
  // }

  // const handleEditComment = async (e) => {
  //   // console.log("eeeeeeeeeeeee", e.target, e.target.value)
  //   e.preventDefault();
  //   console.log("COOKMMMMMMENT",comment)

  //   // await dispatch(updateOneComment(e.target.id, newComment))
  //   // dispatch(getOneProject(projectId))
  // }

  // useEffect(() => {
  //   console.log(commentState);
  // }, [commentState]);

  return (
    <>
      {project && (
        <div id="project-container">
          <div className="title">{project.title}</div>
          <div id="project-details">
            By
            <span className="username-category">{project.owner.username}</span>
            in<span className="username-category">{project.category}</span>
            {session.user.id === project.owner.id && (
              <div className="btn-div">
                <button className="submit-comment" onClick={handleEditProjectButton}>Edit</button>
                <button className="submit-comment" onClick={handleDelete}>Delete</button>
              </div>
            )}
          </div>
          <div className="project-image-container">
            <img
              className="project-images"
              src={project.titleImage}
              alt="Completed project"
            ></img>
          </div>
          <div id="overview-title">
            Project Overview:
            <p id="project-overview">{project.overview}</p>
          </div>
          <ul id="supplies-title">
            Supplies Needed:
            {project.supplies.map((supply) => (
              <div key={supply.id}>
                <li className="supply-list" >
                  {supply.supply}
                  
                </li>
              </div>
            ))}
          </ul>
          <ul>
            {project.instructions.map((instruction) => (
              <div className="instruction-container" key={instruction.id}>
                <div className="instruction-title">
                  Step {instruction.stepOrder} {instruction.stepTitle}:
                </div>
                <div className="project-image-container">
                  <img
                    className="instruction-image"
                    key={instruction.id}
                    src={instruction.photoUrl}
                    alt={`Step ${instruction.stepOrder}`}
                  ></img>
                </div>
                <li className="instructions" key={instruction.id}>
                  {instruction.instructions}
                </li>
              </div>
            ))}
          </ul>
          {showCommentForm && (
            <form className="comment-form" onSubmit={handleComment}>
              <label className="comments-title">Leave a comment here:</label>
              <textarea
                className="comment-box"
                rows='5'
                cols='80'
                type="text"
                onChange={(e) => setComment(e.target.value)}
                value={comment}
              ></textarea>
              <button onClick={handleComment} className="submit-comment" type="submit">Submit Comment</button>
            </form>
          )}
          <ul className="comments-title">
            Comments:
            {user && (
              <button
                id="leave-comment-btn"
                onClick={(e) => setShowCommentForm(true)}
              >
                Post a comment
              </button>
            )}
            {reversedComments.map((comment) => (
              <div key={comment.id}>
                <li className="comments" >
                  {comment.comment}
                </li>
                {+comment.id === +commentId && (
                  // {showCommentEditForm && (

                  <div>
                    <EditCommentForm commentId={comment.id} projectId={projectId} />
                    {/* <button className="submit-comment" onClick={cancel}>Cancel</button> */}
                  </div>
                  // )}
                )}

                {user.id === comment.userId && (
                  <div className="comment-btn-container">
                    <button  className="submit-comment" id={comment.id} onClick={handleShowEditForm}>Edit</button>
                    <button  className="submit-comment" id={comment.id} onClick={handleDeleteComment}>Delete</button>
                  </div>
                )}
              </div>
            ))}
          </ul>
        </div>
      )}
    </>
  );
};

export default ProjectDetails;
